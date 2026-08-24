import json

from django.core import mail
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient

from apps.tenants.models import Dominio
from apps.users.models import Usuario
from apps.users.tokens import make_reset_code

REGISTER_URL = '/api/users/auth/register/'
LOGIN_URL = '/api/users/auth/login/'
ME_URL = '/api/users/me/'
PASSWORD_RESET_URL = '/api/users/auth/password-reset/'
PASSWORD_RESET_VERIFY_URL = '/api/users/auth/password-reset-verify/'
PASSWORD_RESET_CONFIRM_URL = '/api/users/auth/password-reset-confirm/'


class RegisterAndAuthTests(TenantTestCase):
    """Registro, autenticación e inicio de sesión (parte móvil, HU-02).

    Corre dentro de un schema de tenant aislado (TenantTestCase), como
    corresponde a que `apps.users` es un TENANT_APP: cada centro tiene su
    propia tabla de usuarios.
    """

    def setUp(self):
        super().setUp()
        Dominio.objects.get_or_create(
            tenant=self.tenant,
            defaults={'domain': f'{self.tenant.schema_name}.test.com', 'is_primary': True},
        )
        self.client = TenantClient(self.tenant)

    def _post(self, url, payload):
        return self.client.post(
            url, data=json.dumps(payload), content_type='application/json'
        )

    def _register_payload(self, **overrides):
        payload = {
            'email': 'paciente.nuevo@test.com',
            'password': 'ClaveSegura123@',
            'first_name': 'Nuevo',
            'last_name': 'Paciente',
            'phone': '999999999',
        }
        payload.update(overrides)
        return payload

    def test_register_assigns_paciente_role_and_returns_tokens(self):
        response = self._post(REGISTER_URL, self._register_payload())

        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.assertIn('access', body)
        self.assertIn('refresh', body)
        self.assertEqual(body['user']['roles'], ['Paciente'])

        user = Usuario.objects.get(email='paciente.nuevo@test.com')
        self.assertTrue(user.roles.filter(name='Paciente').exists())

    def test_duplicate_email_returns_clean_400(self):
        self._post(REGISTER_URL, self._register_payload())
        response = self._post(REGISTER_URL, self._register_payload())

        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.json())

    def test_me_requires_authentication(self):
        response = self.client.get(ME_URL)
        self.assertEqual(response.status_code, 401)

    def test_me_returns_correct_profile(self):
        register_response = self._post(REGISTER_URL, self._register_payload())
        access_token = register_response.json()['access']

        response = self.client.get(
            ME_URL, HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body['email'], 'paciente.nuevo@test.com')
        self.assertEqual(body['first_name'], 'Nuevo')
        self.assertEqual(body['roles'], ['Paciente'])

    def test_full_register_login_me_chain(self):
        self._post(REGISTER_URL, self._register_payload(email='paciente.chain@test.com'))

        login_response = self._post(
            LOGIN_URL,
            {'email': 'paciente.chain@test.com', 'password': 'ClaveSegura123@'},
        )
        self.assertEqual(login_response.status_code, 200)
        access_token = login_response.json()['access']

        me_response = self.client.get(
            ME_URL, HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.json()['email'], 'paciente.chain@test.com')


class PasswordResetTests(TenantTestCase):
    """HU-10 / CU27 / RF-31: recuperación de contraseña por correo."""

    def setUp(self):
        super().setUp()
        Dominio.objects.get_or_create(
            tenant=self.tenant,
            defaults={'domain': f'{self.tenant.schema_name}.test.com', 'is_primary': True},
        )
        self.client = TenantClient(self.tenant)
        self.user = Usuario.objects.create_user(
            username='paciente@sanamente.com',
            email='paciente@sanamente.com',
            password='ClaveVieja123@',
            first_name='Ana',
        )

    def _post(self, url, payload):
        return self.client.post(
            url, data=json.dumps(payload), content_type='application/json'
        )

    def test_request_with_registered_email_sends_mail_with_code(self):
        response = self._post(PASSWORD_RESET_URL, {'email': 'paciente@sanamente.com'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('paciente@sanamente.com', mail.outbox[0].to)
        self.assertIn('código de verificación', mail.outbox[0].body.lower())

    def test_request_with_unknown_email_returns_generic_200_without_sending_mail(self):
        response = self._post(PASSWORD_RESET_URL, {'email': 'no.existe@test.com'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)

    def test_verify_with_valid_code_returns_200_without_changing_password(self):
        code = make_reset_code(self.user)

        response = self._post(PASSWORD_RESET_VERIFY_URL, {'code': code})

        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('ClaveVieja123@'))  # sin cambios

    def test_verify_with_invalid_code_returns_clean_400(self):
        response = self._post(PASSWORD_RESET_VERIFY_URL, {'code': 'codigo-invalido'})

        self.assertEqual(response.status_code, 400)
        self.assertIn('code', response.json())

    def test_verify_does_not_consume_the_code_confirm_still_works_after(self):
        code = make_reset_code(self.user)

        verify_response = self._post(PASSWORD_RESET_VERIFY_URL, {'code': code})
        self.assertEqual(verify_response.status_code, 200)

        confirm_response = self._post(
            PASSWORD_RESET_CONFIRM_URL,
            {'code': code, 'new_password': 'ClaveNueva456@'},
        )
        self.assertEqual(confirm_response.status_code, 200)

    def test_confirm_with_valid_code_updates_password(self):
        code = make_reset_code(self.user)

        response = self._post(
            PASSWORD_RESET_CONFIRM_URL,
            {'code': code, 'new_password': 'ClaveNueva456@'},
        )

        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('ClaveNueva456@'))

        login_response = self._post(
            LOGIN_URL,
            {'email': 'paciente@sanamente.com', 'password': 'ClaveNueva456@'},
        )
        self.assertEqual(login_response.status_code, 200)

    def test_confirm_with_invalid_code_returns_clean_400(self):
        response = self._post(
            PASSWORD_RESET_CONFIRM_URL,
            {'code': 'codigo-invalido', 'new_password': 'ClaveNueva456@'},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('code', response.json())

    def test_code_cannot_be_reused_after_password_already_changed(self):
        code = make_reset_code(self.user)
        self._post(PASSWORD_RESET_CONFIRM_URL, {'code': code, 'new_password': 'ClaveNueva456@'})

        reused_response = self._post(
            PASSWORD_RESET_CONFIRM_URL,
            {'code': code, 'new_password': 'OtraClave789@'},
        )

        self.assertEqual(reused_response.status_code, 400)


class RoleAndUserManagementTests(TenantTestCase):
    """Pruebas para gestión completa de roles, usuarios y control de acceso (RBAC)."""

    def setUp(self):
        super().setUp()
        Dominio.objects.get_or_create(
            tenant=self.tenant,
            defaults={'domain': f'{self.tenant.schema_name}.test.com', 'is_primary': True},
        )
        self.client = TenantClient(self.tenant)

        # Crear permisos
        from apps.users.models import Permiso, Rol
        self.perm_users = Permiso.objects.create(name='Gestionar Usuarios', codename='gestionar_usuarios')
        self.perm_roles = Permiso.objects.create(name='Gestionar Roles', codename='gestionar_roles')

        # Rol AdminCentro
        self.rol_admin = Rol.objects.create(name='AdminCentro', description='Admin de centro')
        self.rol_admin.permisos.add(self.perm_users, self.perm_roles)

        # Rol Paciente
        self.rol_paciente = Rol.objects.create(name='Paciente', description='Paciente')

        # SuperAdmin User
        self.superadmin = Usuario.objects.create_superuser(
            username='admin@sigepsi.com',
            email='admin@sigepsi.com',
            password='AdminPassword123!',
            first_name='Super',
            last_name='Admin'
        )

        # Admin Centro User
        self.admin_centro_user = Usuario.objects.create_user(
            username='jefe@centro.com',
            email='jefe@centro.com',
            password='Password123!',
            first_name='Jefe',
            last_name='Centro'
        )
        self.admin_centro_user.roles.add(self.rol_admin)

        # Paciente User
        self.paciente_user = Usuario.objects.create_user(
            username='paciente@centro.com',
            email='paciente@centro.com',
            password='Password123!',
            first_name='Juan',
            last_name='Paciente'
        )
        self.paciente_user.roles.add(self.rol_paciente)

    def _get_token(self, email, password='Password123!'):
        if email == 'admin@sigepsi.com':
            password = 'AdminPassword123!'
        res = self.client.post(
            LOGIN_URL,
            data=json.dumps({'email': email, 'password': password}),
            content_type='application/json'
        )
        return res.json().get('access')

    def test_role_creation_and_editing(self):
        token = self._get_token('admin@sigepsi.com')

        # 1. Crear nuevo rol con permisos
        create_res = self.client.post(
            '/api/users/roles/',
            data=json.dumps({
                'name': 'Terapeuta Ocupacional',
                'description': 'Especialista en terapia ocupacional',
                'permisos': [str(self.perm_users.id)]
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(create_res.status_code, 201)
        role_id = create_res.json()['id']
        self.assertEqual(len(create_res.json()['permisos_details']), 1)

        # 2. Modificar rol existente
        update_res = self.client.put(
            f'/api/users/roles/{role_id}/',
            data=json.dumps({
                'name': 'Terapeuta Ocupacional Senior',
                'description': 'Especialista senior con más permisos',
                'permisos': [str(self.perm_users.id), str(self.perm_roles.id)]
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(update_res.status_code, 200)
        self.assertEqual(update_res.json()['name'], 'Terapeuta Ocupacional Senior')
        self.assertEqual(len(update_res.json()['permisos_details']), 2)

    def test_cannot_delete_system_role(self):
        token = self._get_token('admin@sigepsi.com')
        res = self.client.delete(
            f'/api/users/roles/{self.rol_admin.id}/',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn('error', res.json())

    def test_user_update_without_changing_password(self):
        token = self._get_token('admin@sigepsi.com')
        res = self.client.put(
            f'/api/users/usuarios/{self.paciente_user.id}/',
            data=json.dumps({
                'email': 'paciente@centro.com',
                'first_name': 'Juan Modificado',
                'last_name': 'Paciente',
                'is_active': True,
                'roles': [str(self.rol_paciente.id)]
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['first_name'], 'Juan Modificado')

        # Verificar que la contraseña anterior sigue funcionando
        login_res = self.client.post(
            LOGIN_URL,
            data=json.dumps({'email': 'paciente@centro.com', 'password': 'Password123!'}),
            content_type='application/json'
        )
        self.assertEqual(login_res.status_code, 200)

    def test_paciente_cannot_manage_users(self):
        token = self._get_token('paciente@centro.com')
        res = self.client.get(
            '/api/users/usuarios/',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(res.status_code, 403)

