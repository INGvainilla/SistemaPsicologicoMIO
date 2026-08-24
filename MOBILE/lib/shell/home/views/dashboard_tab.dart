import 'package:flutter/material.dart';

class DashboardTab extends StatelessWidget {
  const DashboardTab({
    super.key,
    required this.user,
    required this.tenants,
    required this.users,
    required this.roles,
    required this.isLoading,
    required this.onRefresh,
    required this.onNavigateToTab,
  });

  final dynamic user;
  final List<dynamic> tenants;
  final List<dynamic> users;
  final List<dynamic> roles;
  final bool isLoading;
  final Future<void> Function() onRefresh;
  final void Function(int) onNavigateToTab;

  @override
  Widget build(BuildContext context) {
    return RefreshIndicator(
      onRefresh: onRefresh,
      child: SingleChildScrollView(
        physics: const AlwaysScrollableScrollPhysics(),
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _buildUserHeaderCard(),
            const SizedBox(height: 16),

            if (user?.isSuperAdmin == true) ...[
              _buildSuperAdminDashboard(),
            ] else if (user?.isAdminCentro == true) ...[
              _buildAdminCentroDashboard(),
            ] else if (user?.isPsicologo == true) ...[
              _buildPsicologoDashboard(),
            ] else ...[
              _buildPacienteDashboard(),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildUserHeaderCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: const [
          BoxShadow(
            color: Color(0x0A000000),
            blurRadius: 10,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          CircleAvatar(
            radius: 28,
            backgroundColor: const Color(0xFF0B4F5C),
            child: Text(
              ((user?.firstName as String?)?.isNotEmpty == true
                      ? user!.firstName[0]
                      : 'U')
                  .toUpperCase(),
              style: const TextStyle(
                color: Colors.white,
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  user?.fullName ?? 'Usuario',
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF1E293B),
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  user?.email ?? '',
                  style: const TextStyle(fontSize: 13, color: Color(0xFF64748B)),
                ),
                const SizedBox(height: 6),
                Wrap(
                  spacing: 6,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE0F2FE),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        user?.primaryRole ?? 'Usuario',
                        style: const TextStyle(
                          color: Color(0xFF0369A1),
                          fontSize: 11,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                      decoration: BoxDecoration(
                        color: const Color(0xFFF1F5F9),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        user?.tenantName ?? 'SIGEPSI',
                        style: const TextStyle(
                          color: Color(0xFF475569),
                          fontSize: 11,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSuperAdminDashboard() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          'Panel Global de SuperAdministrador',
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: GestureDetector(
                onTap: () => onNavigateToTab(2), // Centros tab
                child: _buildMetricCard(
                  'Centros',
                  tenants.isNotEmpty ? tenants.length.toString() : '0',
                  Icons.apartment,
                  const Color(0xFF3B82F6),
                ),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: GestureDetector(
                onTap: () => onNavigateToTab(1), // Usuarios tab
                child: _buildMetricCard(
                  'Usuarios',
                  users.isNotEmpty ? users.length.toString() : '0',
                  Icons.people,
                  const Color(0xFF10B981),
                ),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: GestureDetector(
                onTap: () => onNavigateToTab(3), // Roles tab
                child: _buildMetricCard(
                  'Roles',
                  roles.isNotEmpty ? roles.length.toString() : '0',
                  Icons.security,
                  const Color(0xFFF59E0B),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 20),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            const Text(
              'Centros Psicológicos',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
            ),
            TextButton(
              onPressed: () => onNavigateToTab(2),
              child: const Text('Ver todos →', style: TextStyle(color: Color(0xFF0B4F5C))),
            ),
          ],
        ),
        const SizedBox(height: 8),
        if (isLoading)
          const Center(child: Padding(padding: EdgeInsets.all(20), child: CircularProgressIndicator()))
        else if (tenants.isEmpty)
          _buildEmptyCard('No hay centros registrados')
        else
          ListView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: tenants.length > 3 ? 3 : tenants.length,
            itemBuilder: (context, index) {
              final t = tenants[index];
              return Card(
                elevation: 0,
                margin: const EdgeInsets.only(bottom: 8),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                  side: const BorderSide(color: Color(0xFFE2E8F0)),
                ),
                child: ListTile(
                  leading: const CircleAvatar(
                    backgroundColor: Color(0xFFE0F2FE),
                    child: Icon(Icons.local_hospital, color: Color(0xFF0284C7)),
                  ),
                  title: Text(t['name'] ?? '', style: const TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text('Esquema: ${t['schema_name']}'),
                  trailing: Chip(
                    label: Text(t['is_active'] == true ? 'Activo' : 'Inactivo'),
                    backgroundColor: t['is_active'] == true ? const Color(0xFFDCFCE7) : const Color(0xFFFEE2E2),
                    labelStyle: TextStyle(
                      fontSize: 11,
                      color: t['is_active'] == true ? const Color(0xFF166534) : const Color(0xFF991B1B),
                    ),
                  ),
                ),
              );
            },
          ),
      ],
    );
  }

  Widget _buildAdminCentroDashboard() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          'Gestión de Clínica Psicológica',
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: GestureDetector(
                onTap: () => onNavigateToTab(1), // Usuarios
                child: _buildMetricCard(
                  'Personal',
                  users.isNotEmpty ? users.length.toString() : '0',
                  Icons.badge_outlined,
                  const Color(0xFF0284C7),
                ),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: GestureDetector(
                onTap: () => onNavigateToTab(2), // Roles
                child: _buildMetricCard(
                  'Roles',
                  roles.isNotEmpty ? roles.length.toString() : '0',
                  Icons.shield_outlined,
                  const Color(0xFF8B5CF6),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 20),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            const Text(
              'Personal de la Clínica',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
            ),
            TextButton(
              onPressed: () => onNavigateToTab(1),
              child: const Text('Gestionar →', style: TextStyle(color: Color(0xFF0B4F5C))),
            ),
          ],
        ),
        const SizedBox(height: 8),
        if (isLoading)
          const Center(child: Padding(padding: EdgeInsets.all(20), child: CircularProgressIndicator()))
        else if (users.isEmpty)
          _buildEmptyCard('No hay personal registrado en este centro')
        else
          ListView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: users.length > 3 ? 3 : users.length,
            itemBuilder: (context, index) {
              final u = users[index];
              return Card(
                elevation: 0,
                margin: const EdgeInsets.only(bottom: 8),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                  side: const BorderSide(color: Color(0xFFE2E8F0)),
                ),
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: const Color(0xFFF1F5F9),
                    child: Text(
                      ((u['first_name'] as String?)?.isNotEmpty == true ? u['first_name'][0] : 'U').toUpperCase(),
                      style: const TextStyle(color: Color(0xFF334155), fontWeight: FontWeight.bold),
                    ),
                  ),
                  title: Text('${u['first_name'] ?? ''} ${u['last_name'] ?? ''}'.trim(), style: const TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text(u['email'] ?? ''),
                ),
              );
            },
          ),
      ],
    );
  }

  Widget _buildPsicologoDashboard() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          'Atención Clínica y Pacientes',
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Color(0xFF334155)),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(child: _buildMetricCard('Citas Hoy', '0', Icons.calendar_today, const Color(0xFF10B981))),
            const SizedBox(width: 10),
            Expanded(child: _buildMetricCard('Pacientes', '0', Icons.people_outline, const Color(0xFF3B82F6))),
          ],
        ),
        const SizedBox(height: 16),
        _buildActionCard(
          'Agenda Terapéutica',
          'Consulta los horarios programados y sesiones clínicas.',
          Icons.event_note,
        ),
      ],
    );
  }

  Widget _buildPacienteDashboard() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              colors: [Color(0xFF0B4F5C), Color(0xFF1E8A7E)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Icon(Icons.favorite, color: Colors.white, size: 28),
              const SizedBox(height: 12),
              Text(
                '¡Hola, ${user?.firstName ?? 'Paciente'}!',
                style: const TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 4),
              const Text(
                'Bienvenido a tu espacio de salud y bienestar psicológico.',
                style: TextStyle(color: Colors.white70, fontSize: 13),
              ),
            ],
          ),
        ),
        const SizedBox(height: 16),
        _buildActionCard(
          'Mis Citas y Consultas',
          'Revisa el estado de tus citas programadas y tu terapeuta asignado.',
          Icons.calendar_month,
        ),
        const SizedBox(height: 10),
        _buildActionCard(
          'Historial Terapéutico',
          'Accede al seguimiento y notas de tus sesiones.',
          Icons.folder_shared_outlined,
        ),
      ],
    );
  }

  Widget _buildMetricCard(String title, String value, IconData icon, Color color) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFE2E8F0)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(icon, color: color, size: 22),
          const SizedBox(height: 8),
          Text(
            value,
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: color),
          ),
          const SizedBox(height: 2),
          Text(
            title,
            style: const TextStyle(fontSize: 12, color: Color(0xFF64748B), fontWeight: FontWeight.w500),
          ),
        ],
      ),
    );
  }

  Widget _buildActionCard(String title, String desc, IconData icon) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFE2E8F0)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: const Color(0xFFF1F5F9),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, color: const Color(0xFF0B4F5C), size: 24),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Color(0xFF1E293B))),
                const SizedBox(height: 2),
                Text(desc, style: const TextStyle(color: Color(0xFF64748B), fontSize: 12)),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildEmptyCard(String message) {
    return Container(
      padding: const EdgeInsets.all(20),
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFFE2E8F0)),
      ),
      child: Text(message, style: const TextStyle(color: Color(0xFF94A3B8))),
    );
  }
}
