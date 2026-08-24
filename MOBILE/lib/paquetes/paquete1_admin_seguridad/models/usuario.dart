/// Perfil del usuario autenticado devuelto por `/users/me/` y `/users/auth/register/`.
class Usuario {
  final String id;
  final String email;
  final String firstName;
  final String lastName;
  final String phone;
  final List<String> roles;
  final List<String> permisos;
  final bool isSuperuser;
  final bool isStaff;
  final Map<String, dynamic>? tenant;

  const Usuario({
    required this.id,
    required this.email,
    required this.firstName,
    required this.lastName,
    required this.phone,
    required this.roles,
    this.permisos = const [],
    this.isSuperuser = false,
    this.isStaff = false,
    this.tenant,
  });

  String get fullName => '$firstName $lastName'.trim().isEmpty ? email : '$firstName $lastName'.trim();

  String get tenantName => tenant?['name']?.toString() ?? 'SIGEPSI';

  bool get isSuperAdmin => isSuperuser || roles.any((r) => r.toLowerCase() == 'superadmin');

  bool get isAdminCentro => isSuperAdmin || roles.any((r) => r.toLowerCase() == 'admincentro');

  bool get isPsicologo => roles.any((r) => r.toLowerCase().contains('psic'));

  bool get isPaciente => !isSuperAdmin && !isAdminCentro && (roles.contains('Paciente') || roles.isEmpty);

  bool get esPaciente => isPaciente;

  String get primaryRole {
    if (isSuperAdmin) return 'SuperAdmin Global';
    if (isAdminCentro) return 'Administrador de Centro';
    if (isPsicologo) return 'Psicólogo Clínico';
    if (isPaciente) return 'Paciente';
    return roles.isNotEmpty ? roles.first : 'Usuario';
  }

  factory Usuario.fromJson(Map<String, dynamic> json) {
    return Usuario(
      id: json['id']?.toString() ?? '',
      email: json['email'] as String? ?? '',
      firstName: (json['first_name'] as String?) ?? '',
      lastName: (json['last_name'] as String?) ?? '',
      phone: (json['phone'] as String?) ?? '',
      roles: (json['roles'] as List<dynamic>? ?? [])
          .map((r) => r.toString())
          .toList(),
      permisos: (json['permisos'] as List<dynamic>? ?? [])
          .map((p) => p.toString())
          .toList(),
      isSuperuser: json['is_superuser'] == true,
      isStaff: json['is_staff'] == true,
      tenant: json['tenant'] is Map<String, dynamic> ? json['tenant'] as Map<String, dynamic> : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'email': email,
      'first_name': firstName,
      'last_name': lastName,
      'phone': phone,
      'roles': roles,
      'permisos': permisos,
      'is_superuser': isSuperuser,
      'is_staff': isStaff,
      'tenant': tenant,
    };
  }
}
