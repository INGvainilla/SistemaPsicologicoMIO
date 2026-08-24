import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../../../paquetes/paquete1_admin_seguridad/providers/auth_provider.dart';
import '../../../../paquetes/paquete1_admin_seguridad/widgets/auth_text_field.dart';
import '../../../../paquetes/paquete1_admin_seguridad/widgets/gradient_button.dart';

class ProfileTab extends StatefulWidget {
  const ProfileTab({super.key});

  @override
  State<ProfileTab> createState() => _ProfileTabState();
}

class _ProfileTabState extends State<ProfileTab> {
  final _formKey = GlobalKey<FormState>();
  late final TextEditingController _firstNameController;
  late final TextEditingController _lastNameController;
  late final TextEditingController _phoneController;
  final _passwordController = TextEditingController();

  bool _isSaving = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    final user = context.read<AuthProvider>().currentUser;
    _firstNameController = TextEditingController(text: user?.firstName ?? '');
    _lastNameController = TextEditingController(text: user?.lastName ?? '');
    _phoneController = TextEditingController(text: user?.phone ?? '');
  }

  @override
  void dispose() {
    _firstNameController.dispose();
    _lastNameController.dispose();
    _phoneController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _save() async {
    if (!_formKey.currentState!.validate()) return;

    final authProvider = context.read<AuthProvider>();
    final user = authProvider.currentUser;
    if (user == null) return;

    setState(() {
      _isSaving = true;
      _errorMessage = null;
    });

    final success = await authProvider.updateProfile(
      id: user.id,
      firstName: _firstNameController.text.trim(),
      lastName: _lastNameController.text.trim(),
      phone: _phoneController.text.trim(),
      password: _passwordController.text.trim().isEmpty ? null : _passwordController.text,
    );

    if (!mounted) return;
    setState(() => _isSaving = false);

    if (success) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('¡Perfil actualizado con éxito!'),
          backgroundColor: Color(0xFF10B981),
        ),
      );
    } else {
      setState(() {
        _errorMessage = authProvider.errorMessage ?? 'Error al actualizar el perfil';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final authProvider = context.watch<AuthProvider>();
    final user = authProvider.currentUser;

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Form(
        key: _formKey,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: const Color(0xFFE2E8F0)),
              ),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 36,
                    backgroundColor: const Color(0xFF0B4F5C),
                    child: Text(
                      ((user?.firstName.isNotEmpty == true ? user!.firstName[0] : 'U')).toUpperCase(),
                      style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.white),
                    ),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    user?.fullName ?? 'Usuario',
                    style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF1E293B)),
                  ),
                  Text(
                    user?.email ?? '',
                    style: const TextStyle(color: Color(0xFF64748B), fontSize: 13),
                  ),
                  const SizedBox(height: 8),
                  Wrap(
                    spacing: 6,
                    children: [
                      Chip(
                        label: Text(user?.primaryRole ?? 'Usuario'),
                        backgroundColor: const Color(0xFFE0F2FE),
                        labelStyle: const TextStyle(fontSize: 11, color: Color(0xFF0369A1), fontWeight: FontWeight.w600),
                      ),
                      Chip(
                        label: Text(user?.tenantName ?? 'SIGEPSI'),
                        backgroundColor: const Color(0xFFF1F5F9),
                        labelStyle: const TextStyle(fontSize: 11, color: Color(0xFF475569)),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            const Text(
              'Editar Información Personal',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
            ),
            const SizedBox(height: 12),

            AuthTextField(
              controller: _firstNameController,
              label: 'Nombre *',
              icon: Icons.person_outline,
              validator: (val) => val == null || val.trim().isEmpty ? 'Ingresa tu nombre' : null,
            ),
            const SizedBox(height: 14),
            AuthTextField(
              controller: _lastNameController,
              label: 'Apellido *',
              icon: Icons.person_outline,
              validator: (val) => val == null || val.trim().isEmpty ? 'Ingresa tu apellido' : null,
            ),
            const SizedBox(height: 14),
            AuthTextField(
              controller: _phoneController,
              label: 'Teléfono',
              icon: Icons.phone_outlined,
              keyboardType: TextInputType.phone,
            ),
            const SizedBox(height: 14),
            AuthTextField(
              controller: _passwordController,
              label: 'Nueva Contraseña (Opcional)',
              icon: Icons.lock_outline,
              obscureText: true,
            ),
            const SizedBox(height: 4),
            const Text(
              'Deja la contraseña en blanco si deseas conservarla.',
              style: TextStyle(fontSize: 12, color: Color(0xFF94A3B8)),
            ),

            if (_errorMessage != null) ...[
              const SizedBox(height: 14),
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: const Color(0xFFFEE2E2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  _errorMessage!,
                  style: const TextStyle(color: Color(0xFFDC2626), fontSize: 13),
                ),
              ),
            ],

            const SizedBox(height: 24),
            GradientButton(
              label: 'Guardar Cambios',
              isLoading: _isSaving,
              onPressed: _save,
            ),
            const SizedBox(height: 16),

            OutlinedButton(
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 14),
                side: const BorderSide(color: Color(0xFFDC2626)),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              ),
              onPressed: () async {
                await authProvider.logout();
                if (context.mounted) {
                  Navigator.of(context).pushNamedAndRemoveUntil('/login', (_) => false);
                }
              },
              child: const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.logout, color: Color(0xFFDC2626), size: 18),
                  SizedBox(width: 8),
                  Text('Cerrar Sesión', style: TextStyle(color: Color(0xFFDC2626), fontWeight: FontWeight.bold)),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
