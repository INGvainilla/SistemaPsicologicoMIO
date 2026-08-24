import 'package:flutter/material.dart';
import '../../../../core/network/api_exception.dart';
import '../../../../paquetes/paquete1_admin_seguridad/services/auth_service.dart';

class TenantsTab extends StatefulWidget {
  const TenantsTab({super.key, required this.authService, required this.user});

  final AuthService authService;
  final dynamic user;

  @override
  State<TenantsTab> createState() => _TenantsTabState();
}

class _TenantsTabState extends State<TenantsTab> {
  List<dynamic> _tenants = [];
  bool _isLoading = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    _loadTenants();
  }

  Future<void> _loadTenants() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    try {
      final tenants = await widget.authService.fetchTenants();
      if (mounted) {
        setState(() {
          _tenants = tenants;
          _isLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isLoading = false;
          _errorMessage = 'No se pudieron cargar los centros.';
        });
      }
    }
  }

  void _showNewTenantModal() {
    final formKey = GlobalKey<FormState>();
    final nameController = TextEditingController();
    final schemaController = TextEditingController();
    final domainController = TextEditingController();
    final adminNameController = TextEditingController(text: 'Admin Centro');
    final adminEmailController = TextEditingController();
    final adminPasswordController = TextEditingController(text: 'Sigepsi2026!');

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return Padding(
          padding: EdgeInsets.only(
            left: 20,
            right: 20,
            top: 20,
            bottom: MediaQuery.of(context).viewInsets.bottom + 20,
          ),
          child: SingleChildScrollView(
            child: Form(
              key: formKey,
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text(
                        'Registrar Centro Psicológico',
                        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0B4F5C)),
                      ),
                      IconButton(
                        icon: const Icon(Icons.close),
                        onPressed: () => Navigator.pop(ctx),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  TextFormField(
                    controller: nameController,
                    decoration: const InputDecoration(
                      labelText: 'Nombre del Centro *',
                      prefixIcon: Icon(Icons.business),
                      border: OutlineInputBorder(),
                    ),
                    onChanged: (val) {
                      if (schemaController.text.isEmpty || schemaController.text.length < 5) {
                        final slug = val.toLowerCase().replaceAll(RegExp(r'[^a-z0-9]'), '_');
                        schemaController.text = slug;
                        domainController.text = '$slug.localhost';
                      }
                    },
                    validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                  ),
                  const SizedBox(height: 12),
                  TextFormField(
                    controller: schemaController,
                    decoration: const InputDecoration(
                      labelText: 'Identificador / Esquema *',
                      prefixIcon: Icon(Icons.dns),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                  ),
                  const SizedBox(height: 12),
                  TextFormField(
                    controller: domainController,
                    decoration: const InputDecoration(
                      labelText: 'Dominio *',
                      prefixIcon: Icon(Icons.link),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                  ),
                  const SizedBox(height: 16),
                  const Text('Administrador del Centro:', style: TextStyle(fontWeight: FontWeight.bold)),
                  const SizedBox(height: 8),
                  TextFormField(
                    controller: adminNameController,
                    decoration: const InputDecoration(
                      labelText: 'Nombre del Administrador *',
                      prefixIcon: Icon(Icons.person),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                  ),
                  const SizedBox(height: 12),
                  TextFormField(
                    controller: adminEmailController,
                    keyboardType: TextInputType.emailAddress,
                    decoration: const InputDecoration(
                      labelText: 'Correo del Administrador *',
                      prefixIcon: Icon(Icons.mail),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                  ),
                  const SizedBox(height: 12),
                  TextFormField(
                    controller: adminPasswordController,
                    obscureText: true,
                    decoration: const InputDecoration(
                      labelText: 'Contraseña del Administrador *',
                      prefixIcon: Icon(Icons.lock),
                      border: OutlineInputBorder(),
                    ),
                    validator: (v) => v == null || v.length < 8 ? 'Mínimo 8 caracteres' : null,
                  ),
                  const SizedBox(height: 20),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF0B4F5C),
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    ),
                    onPressed: () async {
                      if (!formKey.currentState!.validate()) return;

                      try {
                        await widget.authService.createTenant({
                          'name': nameController.text.trim(),
                          'schema_name': schemaController.text.trim().toLowerCase(),
                          'domain_url': domainController.text.trim().toLowerCase(),
                          'admin_name': adminNameController.text.trim(),
                          'admin_email': adminEmailController.text.trim().toLowerCase(),
                          'admin_password': adminPasswordController.text,
                        });
                        if (ctx.mounted) Navigator.pop(ctx);
                        _loadTenants();
                        if (mounted) {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                              content: Text('Centro registrado con éxito'),
                              backgroundColor: Color(0xFF10B981),
                            ),
                          );
                        }
                      } on ApiException catch (e) {
                        if (ctx.mounted) {
                          ScaffoldMessenger.of(ctx).showSnackBar(
                            SnackBar(content: Text(e.message), backgroundColor: const Color(0xFFDC2626)),
                          );
                        }
                      }
                    },
                    child: const Text('Crear Centro Psicológico'),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final isSuperAdmin = widget.user?.isSuperAdmin == true;

    return Scaffold(
      backgroundColor: const Color(0xFFF1F5F9),
      floatingActionButton: isSuperAdmin
          ? FloatingActionButton.extended(
              backgroundColor: const Color(0xFF0B4F5C),
              foregroundColor: Colors.white,
              icon: const Icon(Icons.add_business),
              label: const Text('Nuevo Centro'),
              onPressed: _showNewTenantModal,
            )
          : null,
      body: RefreshIndicator(
        onRefresh: _loadTenants,
        child: _isLoading
            ? const Center(child: CircularProgressIndicator())
            : _errorMessage != null
                ? Center(child: Text(_errorMessage!))
                : _tenants.isEmpty
                    ? const Center(child: Text('No hay centros registrados', style: TextStyle(color: Color(0xFF94A3B8))))
                    : ListView.builder(
                        padding: const EdgeInsets.fromLTRB(16, 16, 16, 80),
                        itemCount: _tenants.length,
                        itemBuilder: (context, index) {
                          final t = _tenants[index];
                          final domains = (t['domains'] as List<dynamic>? ?? [])
                              .map((d) => d['domain']?.toString() ?? '')
                              .join(', ');

                          return Card(
                            elevation: 0,
                            margin: const EdgeInsets.only(bottom: 12),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(14),
                              side: const BorderSide(color: Color(0xFFE2E8F0)),
                            ),
                            child: Padding(
                              padding: const EdgeInsets.all(16),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Row(
                                    children: [
                                      const CircleAvatar(
                                        backgroundColor: Color(0xFFE0F2FE),
                                        child: Icon(Icons.apartment, color: Color(0xFF0284C7)),
                                      ),
                                      const SizedBox(width: 12),
                                      Expanded(
                                        child: Column(
                                          crossAxisAlignment: CrossAxisAlignment.start,
                                          children: [
                                            Text(
                                              t['name'] ?? 'Centro',
                                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                                            ),
                                            Text(
                                              'Esquema: ${t['schema_name']}',
                                              style: const TextStyle(color: Color(0xFF64748B), fontSize: 13),
                                            ),
                                          ],
                                        ),
                                      ),
                                      Chip(
                                        label: Text(t['is_active'] == true ? 'Activo' : 'Inactivo'),
                                        backgroundColor: t['is_active'] == true
                                            ? const Color(0xFFDCFCE7)
                                            : const Color(0xFFFEE2E2),
                                        labelStyle: TextStyle(
                                          fontSize: 11,
                                          color: t['is_active'] == true
                                              ? const Color(0xFF166534)
                                              : const Color(0xFF991B1B),
                                        ),
                                      ),
                                    ],
                                  ),
                                  if (domains.isNotEmpty) ...[
                                    const SizedBox(height: 10),
                                    Row(
                                      children: [
                                        const Icon(Icons.link, size: 14, color: Color(0xFF94A3B8)),
                                        const SizedBox(width: 4),
                                        Expanded(
                                          child: Text(
                                            domains,
                                            style: const TextStyle(color: Color(0xFF0B4F5C), fontSize: 12, fontWeight: FontWeight.w500),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ],
                                ],
                              ),
                            ),
                          );
                        },
                      ),
      ),
    );
  }
}
