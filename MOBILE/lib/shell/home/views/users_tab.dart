import 'package:flutter/material.dart';
import '../../../../core/network/api_exception.dart';
import '../../../../paquetes/paquete1_admin_seguridad/services/auth_service.dart';

class UsersTab extends StatefulWidget {
  const UsersTab({super.key, required this.authService});

  final AuthService authService;

  @override
  State<UsersTab> createState() => _UsersTabState();
}

class _UsersTabState extends State<UsersTab> {
  final TextEditingController _searchController = TextEditingController();
  String _selectedRole = 'Todos';
  List<dynamic> _users = [];
  List<dynamic> _availableRoles = [];
  bool _isLoading = false;
  String? _errorMessage;

  final List<String> _roleFilters = [
    'Todos',
    'SuperAdmin',
    'AdminCentro',
    'Psicólogo',
    'Paciente',
    'Recepcionista',
  ];

  @override
  void initState() {
    super.initState();
    _loadUsers();
    _loadRoles();
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadRoles() async {
    try {
      final roles = await widget.authService.fetchRoles();
      if (mounted) setState(() => _availableRoles = roles);
    } catch (_) {}
  }

  Future<void> _loadUsers() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    try {
      final users = await widget.authService.fetchUsers(
        search: _searchController.text.trim(),
        role: _selectedRole,
      );
      if (mounted) {
        setState(() {
          _users = users;
          _isLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isLoading = false;
          _errorMessage = 'No se pudieron cargar los usuarios. Verifica tu conexión.';
        });
      }
    }
  }

  void _showUserFormModal([Map<String, dynamic>? userToEdit]) {
    final isEditing = userToEdit != null;
    final formKey = GlobalKey<FormState>();
    final firstNameController = TextEditingController(text: userToEdit?['first_name'] ?? '');
    final lastNameController = TextEditingController(text: userToEdit?['last_name'] ?? '');
    final emailController = TextEditingController(text: userToEdit?['email'] ?? '');
    final phoneController = TextEditingController(text: userToEdit?['phone'] ?? '');
    final passwordController = TextEditingController();
    
    // Roles seleccionados
    List<String> selectedRoleIds = [];
    if (isEditing && userToEdit['roles'] is List) {
      // Mapear por nombre o ID
      for (final r in userToEdit['roles']) {
        final rName = r.toString();
        final found = _availableRoles.firstWhere(
          (roleObj) => roleObj['name'].toString().toLowerCase() == rName.toLowerCase(),
          orElse: () => null,
        );
        if (found != null && found['id'] != null) {
          selectedRoleIds.add(found['id'].toString());
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
                            isEditing ? 'Modificar Usuario' : 'Registrar Nuevo Usuario',
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
                        controller: firstNameController,
                        decoration: const InputDecoration(
                          labelText: 'Nombre *',
                          prefixIcon: Icon(Icons.person_outline),
                          border: OutlineInputBorder(),
                        ),
                        validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: lastNameController,
                        decoration: const InputDecoration(
                          labelText: 'Apellido *',
                          prefixIcon: Icon(Icons.person_outline),
                          border: OutlineInputBorder(),
                        ),
                        validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: emailController,
                        keyboardType: TextInputType.emailAddress,
                        enabled: !isEditing,
                        decoration: const InputDecoration(
                          labelText: 'Correo electrónico *',
                          prefixIcon: Icon(Icons.mail_outline),
                          border: OutlineInputBorder(),
                        ),
                        validator: (v) => v == null || v.trim().isEmpty ? 'Requerido' : null,
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: phoneController,
                        keyboardType: TextInputType.phone,
                        decoration: const InputDecoration(
                          labelText: 'Teléfono',
                          prefixIcon: Icon(Icons.phone_outlined),
                          border: OutlineInputBorder(),
                        ),
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: passwordController,
                        obscureText: true,
                        decoration: InputDecoration(
                          labelText: isEditing ? 'Nueva Contraseña (Opcional)' : 'Contraseña *',
                          prefixIcon: const Icon(Icons.lock_outline),
                          border: const OutlineInputBorder(),
                        ),
                        validator: (v) {
                          if (!isEditing && (v == null || v.isEmpty)) return 'Requerido';
                          if (v != null && v.isNotEmpty && v.length < 8) return 'Mínimo 8 caracteres';
                          return null;
                        },
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        'Asignar Rol:',
                        style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF334155)),
                      ),
                      const SizedBox(height: 6),
                      Wrap(
                        spacing: 8,
                        children: _availableRoles.map((r) {
                          final rId = r['id'].toString();
                          final rName = r['name'].toString();
                          final isSelected = selectedRoleIds.contains(rId);
                          return FilterChip(
                            label: Text(rName),
                            selected: isSelected,
                            onSelected: (selected) {
                              setModalState(() {
                                if (selected) {
                                  selectedRoleIds = [rId]; // un rol principal
                                } else {
                                  selectedRoleIds.remove(rId);
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
                          final Map<String, dynamic> payload = {
                            'first_name': firstNameController.text.trim(),
                            'last_name': lastNameController.text.trim(),
                            'phone': phoneController.text.trim(),
                          };
                          if (!isEditing) {
                            payload['email'] = emailController.text.trim().toLowerCase();
                            payload['password'] = passwordController.text;
                          } else if (passwordController.text.isNotEmpty) {
                            payload['password'] = passwordController.text;
                          }
                          if (selectedRoleIds.isNotEmpty) {
                            payload['role_ids'] = selectedRoleIds;
                          }

                          try {
                            if (isEditing) {
                              await widget.authService.updateUser(userToEdit['id'].toString(), payload);
                            } else {
                              await widget.authService.createUser(payload);
                            }
                            if (ctx.mounted) Navigator.pop(ctx);
                            _loadUsers();
                            messenger.showSnackBar(
                              SnackBar(
                                content: Text(isEditing ? 'Usuario modificado con éxito' : 'Usuario creado con éxito'),
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
                        child: Text(isEditing ? 'Guardar Cambios' : 'Registrar Usuario'),
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

  Future<void> _confirmDeleteUser(dynamic u) async {
    final confirm = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Eliminar Usuario'),
        content: Text('¿Estás seguro de eliminar a "${u['first_name']} ${u['last_name']}" (${u['email']})?'),
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
        await widget.authService.deleteUser(u['id'].toString());
        _loadUsers();
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Usuario eliminado correctamente'), backgroundColor: Color(0xFF10B981)),
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
        icon: const Icon(Icons.person_add),
        label: const Text('Nuevo Usuario'),
        onPressed: () => _showUserFormModal(),
      ),
      body: RefreshIndicator(
        onRefresh: _loadUsers,
        child: Column(
          children: [
            // Barra de búsqueda y filtros
            Container(
              padding: const EdgeInsets.all(16),
              color: Colors.white,
              child: Column(
                children: [
                  TextField(
                    controller: _searchController,
                    decoration: InputDecoration(
                      hintText: 'Buscar por nombre o correo...',
                      prefixIcon: const Icon(Icons.search, color: Color(0xFF0B4F5C)),
                      suffixIcon: _searchController.text.isNotEmpty
                          ? IconButton(
                              icon: const Icon(Icons.clear),
                              onPressed: () {
                                _searchController.clear();
                                _loadUsers();
                              },
                            )
                          : null,
                      filled: true,
                      fillColor: const Color(0xFFF8FAFC),
                      contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 16),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: const BorderSide(color: Color(0xFFE2E8F0)),
                      ),
                    ),
                    onSubmitted: (_) => _loadUsers(),
                  ),
                  const SizedBox(height: 10),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: _roleFilters.map((role) {
                        final isSelected = _selectedRole == role;
                        return Padding(
                          padding: const EdgeInsets.only(right: 6),
                          child: ChoiceChip(
                            label: Text(role),
                            selected: isSelected,
                            selectedColor: const Color(0xFF0B4F5C),
                            labelStyle: TextStyle(
                              color: isSelected ? Colors.white : const Color(0xFF334155),
                              fontSize: 12,
                              fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                            ),
                            onSelected: (selected) {
                              if (selected) {
                                setState(() => _selectedRole = role);
                                _loadUsers();
                              }
                            },
                          ),
                        );
                      }).toList(),
                    ),
                  ),
                ],
              ),
            ),

            // Lista de Usuarios
            Expanded(
              child: _isLoading
                  ? const Center(child: CircularProgressIndicator())
                  : _errorMessage != null
                      ? Center(
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(_errorMessage!, style: const TextStyle(color: Color(0xFFDC2626))),
                              const SizedBox(height: 10),
                              ElevatedButton(onPressed: _loadUsers, child: const Text('Reintentar')),
                            ],
                          ),
                        )
                      : _users.isEmpty
                          ? const Center(
                              child: Text(
                                'No se encontraron usuarios',
                                style: TextStyle(color: Color(0xFF94A3B8), fontSize: 16),
                              ),
                            )
                          : ListView.builder(
                              padding: const EdgeInsets.fromLTRB(16, 12, 16, 80),
                              itemCount: _users.length,
                              itemBuilder: (context, index) {
                                final u = _users[index];
                                final List<String> roleNames = [];
                                if (u['roles_names'] is List && (u['roles_names'] as List).isNotEmpty) {
                                  roleNames.addAll((u['roles_names'] as List).map((r) => r.toString()));
                                } else if (u['roles_details'] is List && (u['roles_details'] as List).isNotEmpty) {
                                  for (final rd in u['roles_details']) {
                                    if (rd is Map && rd['name'] != null) {
                                      roleNames.add(rd['name'].toString());
                                    }
                                  }
                                } else if (u['roles'] is List) {
                                  for (final r in u['roles']) {
                                    final rStr = r.toString();
                                    if (rStr.length < 30) roleNames.add(rStr);
                                  }
                                }
                                if (roleNames.isEmpty) {
                                  roleNames.add(u['is_superuser'] == true ? 'SuperAdmin' : 'Usuario');
                                }
                                final isSuper = u['is_superuser'] == true ||
                                    roleNames.any((r) => r.toLowerCase().contains('superadmin'));

                                return Card(
                                  elevation: 0,
                                  margin: const EdgeInsets.only(bottom: 10),
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    side: const BorderSide(color: Color(0xFFE2E8F0)),
                                  ),
                                  child: Padding(
                                    padding: const EdgeInsets.all(14),
                                    child: Row(
                                      children: [
                                        CircleAvatar(
                                          radius: 24,
                                          backgroundColor: isSuper ? const Color(0xFFFEF3C7) : const Color(0xFFE0F2FE),
                                          child: Text(
                                            ((u['first_name'] as String?)?.isNotEmpty == true
                                                    ? u['first_name'][0]
                                                    : 'U')
                                                .toUpperCase(),
                                            style: TextStyle(
                                              fontWeight: FontWeight.bold,
                                              color: isSuper ? const Color(0xFFB45309) : const Color(0xFF0369A1),
                                            ),
                                          ),
                                        ),
                                        const SizedBox(width: 12),
                                        Expanded(
                                          child: Column(
                                            crossAxisAlignment: CrossAxisAlignment.start,
                                            children: [
                                              Text(
                                                '${u['first_name'] ?? ''} ${u['last_name'] ?? ''}'.trim().isEmpty
                                                    ? u['email'] ?? ''
                                                    : '${u['first_name']} ${u['last_name']}',
                                                style: const TextStyle(
                                                  fontWeight: FontWeight.bold,
                                                  fontSize: 15,
                                                  color: Color(0xFF1E293B),
                                                ),
                                              ),
                                              const SizedBox(height: 2),
                                              Text(
                                                u['email'] ?? '',
                                                style: const TextStyle(color: Color(0xFF64748B), fontSize: 13),
                                              ),
                                              if (u['phone'] != null && (u['phone'] as String).isNotEmpty) ...[
                                                const SizedBox(height: 2),
                                                Row(
                                                  children: [
                                                    const Icon(Icons.phone, size: 12, color: Color(0xFF94A3B8)),
                                                    const SizedBox(width: 4),
                                                    Text(
                                                      u['phone'],
                                                      style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 12),
                                                    ),
                                                  ],
                                                ),
                                              ],
                                              const SizedBox(height: 6),
                                              Wrap(
                                                spacing: 4,
                                                runSpacing: 4,
                                                children: roleNames.map((r) {
                                                  return Container(
                                                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                                                    decoration: BoxDecoration(
                                                      color: const Color(0xFFF1F5F9),
                                                      borderRadius: BorderRadius.circular(4),
                                                    ),
                                                    child: Text(
                                                      r,
                                                      style: const TextStyle(fontSize: 10, fontWeight: FontWeight.w600, color: Color(0xFF475569)),
                                                    ),
                                                  );
                                                }).toList(),
                                              ),
                                            ],
                                          ),
                                        ),
                                        PopupMenuButton<String>(
                                          icon: const Icon(Icons.more_vert, color: Color(0xFF64748B)),
                                          onSelected: (val) {
                                            if (val == 'edit') {
                                              _showUserFormModal(u);
                                            } else if (val == 'delete') {
                                              _confirmDeleteUser(u);
                                            }
                                          },
                                          itemBuilder: (context) => [
                                            const PopupMenuItem(
                                              value: 'edit',
                                              child: Row(
                                                children: [
                                                  Icon(Icons.edit, size: 18, color: Color(0xFF0284C7)),
                                                  SizedBox(width: 8),
                                                  Text('Modificar'),
                                                ],
                                              ),
                                            ),
                                            const PopupMenuItem(
                                              value: 'delete',
                                              child: Row(
                                                children: [
                                                  Icon(Icons.delete, size: 18, color: Color(0xFFDC2626)),
                                                  SizedBox(width: 8),
                                                  Text('Eliminar'),
                                                ],
                                              ),
                                            ),
                                          ],
                                        ),
                                      ],
                                    ),
                                  ),
                                );
                              },
                            ),
            ),
          ],
        ),
      ),
    );
  }
}
