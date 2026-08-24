import json
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from apps.tenants.models import Centro, Dominio
from apps.users.models import Usuario

class CentroTenantTests(TenantTestCase):
    def setUp(self):
        super().setUp()
        Dominio.objects.get_or_create(
            tenant=self.tenant,
            defaults={'domain': f'{self.tenant.schema_name}.test.com', 'is_primary': True},
        )
        self.client = TenantClient(self.tenant)

        # Crear SuperAdmin
        self.superuser = Usuario.objects.create_superuser(
            username='superadmin@test.com',
            email='superadmin@test.com',
            password='Password123!',
            first_name='Super',
            last_name='Admin'
        )

        # Crear Usuario normal
        self.regular_user = Usuario.objects.create_user(
            username='user@test.com',
            email='user@test.com',
            password='Password123!',
            first_name='Regular',
            last_name='User'
        )

    def _get_token(self, user):
        res = self.client.post(
            '/api/users/auth/login/',
            data=json.dumps({'email': user.email, 'password': 'Password123!'}),
            content_type='application/json'
        )
        return res.json().get('access')

    def test_superuser_can_list_all_tenants(self):
        token = self._get_token(self.superuser)
        res = self.client.get('/api/tenants/', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(res.json()) >= 1)

    def test_regular_user_cannot_create_tenant(self):
        token = self._get_token(self.regular_user)
        payload = {
            'name': 'Clínica No Autorizada',
            'schema_name': 'clinica_no_auth',
            'domain_url': 'noauth.localhost'
        }
        res = self.client.post(
            '/api/tenants/',
            data=json.dumps(payload),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEqual(res.status_code, 403)
