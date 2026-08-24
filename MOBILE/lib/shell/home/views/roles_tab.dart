import 'package:flutter/material.dart';
import '../../../../core/network/api_exception.dart';
import '../../../../paquetes/paquete1_admin_seguridad/services/auth_service.dart';

class RolesTab extends StatefulWidget {
  const RolesTab({super.key, required this.authService});

  final AuthService authService;

  @override
  State<RolesTab> createState() => _RolesTabState();
}

class _RolesTabState extends State<RolesTab> {
  List<dynamic> _roles = [];
  List<dynamic> _permissions = [];
  bool _isLoading = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    try {
      // Cargar roles y permisos en paralelo
      final results = await Future.wait([
        widget.authService.fetchRoles(),
        widget.authService.fetchPermissions(),
      ]);
      if (mounted) {
        setState(() {
          _roles = results[0];
          _permissions = results[1];
          _isLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isLoading = false;
          _errorMessage = 'No se pudieron cargar los roles.';
        });
      }
    }
  }

  void _showRoleFormModal([Map<String, dynamic>? roleToEdit]) {
    final isEditing = roleToEdit != null;
    final formKey = GlobalKey<FormState>();
    final nameController = TextEditingController(text: roleToEdit?['name'] ?? '');
    final descController = TextEditingController(text: roleToEdit?['description'] ?? '');
    
    List<String> selectedPermIds = [];
    if (isEditing && roleToEdit['permisos'] is List) {
      for (final p in roleToEdit['permisos']) {
        if (p is Map && p['id'] != null) {
          selectedPermIds.add(p['id'].toString());
        }
      }
    }

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return StatefulBuilder(
          builder: (context, setModalState) {
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
                          Text(
                            isEditing ? 'Modificar Rol' : 'Crear Nuevo Rol',
                            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0B4F5C)),
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
                          labelText: 'Nombre del Rol *',
                          prefixIcon: Icon(Icons.security),
                          border: OutlineInputBorder(),
                        ),
                        validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: descController,
                        decoration: const InputDecoration(
                          labelText: 'Descripción',
                          prefixIcon: Icon(Icons.description_outlined),
                          border: OutlineInputBorder(),
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        'Permisos Asignados:',
                        style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF334155)),
                      ),
                      const SizedBox(height: 8),
                      if (_permissions.isEmpty)
                        const Text('Cargando permisos...')
                      else
                        Wrap(
                          spacing: 8,
                          runSpacing: 8,
                          children: _permissions.map((p) {
                            final pId = p['id'].toString();
                            final pName = p['name'].toString();
                            final isSelected = selectedPermIds.contains(pId);
                            return FilterChip(
                              label: Text(pName, style: const TextStyle(fontSize: 12)),
                              selected: isSelected,
                              onSelected: (selected) {
                                setModalState(() {
                                  if (selected) {
                                    selectedPermIds.add(pId);
                                  } else {
                                    selectedPermIds.remove(pId);
                                  }
                                });
                              },
                            );
                          }).toList(),
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

                          final messenger = ScaffoldMessenger.of(context);
                          final payload = {
                            'name': nameController.text.trim(),
                            'description': descController.text.trim(),
                            'permiso_ids': selectedPermIds,
                          };

                          try {
                            if (isEditing) {
                              await widget.authService.updateRole(roleToEdit['id'].toString(), payload);
                            } else {
                              await widget.authService.createRole(payload);
                            }
                            if (ctx.mounted) Navigator.pop(ctx);
                            _loadData();
                            messenger.showSnackBar(
                              SnackBar(
                                content: Text(isEditing ? 'Rol modificado con éxito' : 'Rol creado con éxito'),
                                backgroundColor: const Color(0xFF10B981),
                              ),
                            );
                          } on ApiException catch (err) {
                            if (ctx.mounted) {
                              ScaffoldMessenger.of(ctx).showSnackBar(
                                SnackBar(content: Text(err.message), backgroundColor: const Color(0xFFDC2626)),
                              );
                            }
                          }
                        },
                        child: Text(isEditing ? 'Guardar Cambios' : 'Crear Rol'),
                      ),
                    ],
                  ),
                ),
              ),
            );
          },
        );
      },
    );
  }

  Future<void> _confirmDeleteRole(dynamic r) async {
    final confirm = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Eliminar Rol'),
        content: Text('¿Estás seguro de eliminar el rol "${r['name']}"?'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancelar')),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: const Color(0xFFDC2626), foregroundColor: Colors.white),
            onPressed: () => Navigator.pop(ctx, true),
            child: const Text('Eliminar'),
          ),
        ],
      ),
    );

    if (confirm == true) {
      try {
        await widget.authService.deleteRole(r['id'].toString());
        _loadData();
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Rol eliminado correctamente'), backgroundColor: Color(0xFF10B981)),
          );
        }
      } on ApiException catch (e) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text(e.message), backgroundColor: const Color(0xFFDC2626)),
          );
        }
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF1F5F9),
      floatingActionButton: FloatingActionButton.extended(
        backgroundColor: const Color(0xFF0B4F5C),
        foregroundColor: Colors.white,
        icon: const Icon(Icons.add_moderator),
        label: const Text('Nuevo Rol'),
        onPressed: () => _showRoleFormModal(),
      ),
      body: RefreshIndicator(
        onRefresh: _loadData,
        child: _isLoading
            ? const Center(child: CircularProgressIndicator())
            : _errorMessage != null
                ? Center(child: Text(_errorMessage!))
                : _roles.isEmpty
                    ? const Center(child: Text('No hay roles registrados', style: TextStyle(color: Color(0xFF94A3B8))))
                    : ListView.builder(
                        padding: const EdgeInsets.fromLTRB(16, 16, 16, 80),
                        itemCount: _roles.length,
                        itemBuilder: (context, index) {
                          final r = _roles[index];
                          final perms = (r['permisos'] as List<dynamic>? ?? [])
                              .map((p) => p is Map ? p['name']?.toString() ?? '' : p.toString())
                              .where((p) => p.isNotEmpty)
                              .toList();
                          final isSystem = ['SuperAdmin', 'AdminCentro', 'Psicologo', 'Psicólogo', 'Paciente', 'Recepcionista']
                              .contains(r['name']);

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
                                        backgroundColor: Color(0xFFFEF3C7),
                                        child: Icon(Icons.shield, color: Color(0xFFD97706)),
                                      ),
                                      const SizedBox(width: 12),
                                      Expanded(
                                        child: Column(
                                          crossAxisAlignment: CrossAxisAlignment.start,
                                          children: [
                                            Text(
                                              r['name'] ?? 'Rol',
                                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                                            ),
                                            if (r['description'] != null && (r['description'] as String).isNotEmpty)
                                              Text(
                                                r['description'],
                                                style: const TextStyle(color: Color(0xFF64748B), fontSize: 13),
                                              ),
                                          ],
                                        ),
                                      ),
                                      if (!isSystem)
                                        PopupMenuButton<String>(
                                          onSelected: (val) {
                                            if (val == 'edit') {
                                              _showRoleFormModal(r);
                                            } else if (val == 'delete') {
                                              _confirmDeleteRole(r);
                                            }
                                          },
                                          itemBuilder: (ctx) => [
                                            const PopupMenuItem(value: 'edit', child: Text('Modificar')),
                                            const PopupMenuItem(
                                              value: 'delete',
                                              child: Text('Eliminar', style: TextStyle(color: Color(0xFFDC2626))),
                                            ),
                                          ],
                                        ),
                                    ],
                                  ),
                                  if (perms.isNotEmpty) ...[
                                    const SizedBox(height: 12),
                                    const Text(
                                      'Permisos:',
                                      style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF64748B)),
                                    ),
                                    const SizedBox(height: 6),
                                    Wrap(
                                      spacing: 6,
                                      runSpacing: 6,
                                      children: perms.map((p) {
                                        return Container(
                                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                                          decoration: BoxDecoration(
                                            color: const Color(0xFFF1F5F9),
                                            borderRadius: BorderRadius.circular(6),
                                          ),
                                          child: Text(
                                            p,
                                            style: const TextStyle(fontSize: 11, color: Color(0xFF334155)),
                                          ),
                                        );
                                      }).toList(),
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
