import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../../paquetes/paquete1_admin_seguridad/providers/auth_provider.dart';
import '../../../paquetes/paquete1_admin_seguridad/services/auth_service.dart';
import '../views/dashboard_tab.dart';
import '../views/profile_tab.dart';
import '../views/roles_tab.dart';
import '../views/tenants_tab.dart';
import '../views/users_tab.dart';

/// Pantalla Principal (Shell) con navegación por Pestañas inferiores (BottomNavigationBar)
class HomeScreen extends StatefulWidget {
  static const routeName = '/home';

  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;
  final AuthService _authService = AuthService();

  List<dynamic> _tenants = [];
  List<dynamic> _users = [];
  List<dynamic> _roles = [];
  bool _isLoadingData = false;

  @override
  void initState() {
    super.initState();
    _loadDashboardData();
  }

  Future<void> _loadDashboardData() async {
    final user = context.read<AuthProvider>().currentUser;
    if (user == null) return;

    setState(() => _isLoadingData = true);
    try {
      if (user.isSuperAdmin) {
        // Lanzar las 3 peticiones en paralelo en vez de secuencial
        final results = await Future.wait([
          _authService.fetchTenants(),
          _authService.fetchUsers(),
          _authService.fetchRoles(),
        ]);
        if (mounted) {
          setState(() {
            _tenants = results[0];
            _users = results[1];
            _roles = results[2];
          });
        }
      } else if (user.isAdminCentro) {
        final results = await Future.wait([
          _authService.fetchUsers(),
          _authService.fetchRoles(),
        ]);
        if (mounted) {
          setState(() {
            _users = results[0];
            _roles = results[1];
          });
        }
      }
    } catch (e) {
      debugPrint('Error cargando datos: $e');
    } finally {
      if (mounted) setState(() => _isLoadingData = false);
    }
  }

  void _onTabSelected(int index) {
    setState(() => _currentIndex = index);
  }

  @override
  Widget build(BuildContext context) {
    final authProvider = context.watch<AuthProvider>();
    final user = authProvider.currentUser;

    final isSuperAdmin = user?.isSuperAdmin == true;
    final isAdminCentro = user?.isAdminCentro == true;
    final isStaffOrAdmin = isSuperAdmin || isAdminCentro;

    // Construcción dinámica de pestañas según el rol
    final List<Widget> tabViews = [];
    final List<NavigationDestination> destinations = [];
    final List<String> titles = [];

    // Tab 1: Dashboard
    titles.add('Panel Principal');
    destinations.add(
      const NavigationDestination(
        icon: Icon(Icons.dashboard_outlined),
        selectedIcon: Icon(Icons.dashboard, color: Color(0xFF0B4F5C)),
        label: 'Inicio',
      ),
    );
    tabViews.add(
      DashboardTab(
        user: user,
        tenants: _tenants,
        users: _users,
        roles: _roles,
        isLoading: _isLoadingData,
        onRefresh: _loadDashboardData,
        onNavigateToTab: _onTabSelected,
      ),
    );

    // Tab 2: Usuarios (para SuperAdmin y AdminCentro)
    if (isStaffOrAdmin) {
      titles.add('Gestión de Usuarios');
      destinations.add(
        const NavigationDestination(
          icon: Icon(Icons.people_outline),
          selectedIcon: Icon(Icons.people, color: Color(0xFF0B4F5C)),
          label: 'Usuarios',
        ),
      );
      tabViews.add(UsersTab(authService: _authService));
    }

    // Tab 3: Centros (solo SuperAdmin)
    if (isSuperAdmin) {
      titles.add('Centros Psicológicos');
      destinations.add(
        const NavigationDestination(
          icon: Icon(Icons.apartment_outlined),
          selectedIcon: Icon(Icons.apartment, color: Color(0xFF0B4F5C)),
          label: 'Centros',
        ),
      );
      tabViews.add(TenantsTab(authService: _authService, user: user));
    }

    // Tab 4: Roles y Permisos (para SuperAdmin y AdminCentro)
    if (isStaffOrAdmin) {
      titles.add('Roles y Permisos');
      destinations.add(
        const NavigationDestination(
          icon: Icon(Icons.security_outlined),
          selectedIcon: Icon(Icons.security, color: Color(0xFF0B4F5C)),
          label: 'Roles',
        ),
      );
      tabViews.add(RolesTab(authService: _authService));
    }

    // Tab Final: Mi Perfil (todos)
    titles.add('Mi Perfil');
    destinations.add(
      const NavigationDestination(
        icon: Icon(Icons.person_outline),
        selectedIcon: Icon(Icons.person, color: Color(0xFF0B4F5C)),
        label: 'Perfil',
      ),
    );
    tabViews.add(const ProfileTab());

    // Asegurar que el índice seleccionado no quede fuera de rango
    final safeIndex = _currentIndex >= tabViews.length ? 0 : _currentIndex;

    return Scaffold(
      backgroundColor: const Color(0xFFF1F5F9),
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                color: const Color(0xFF1E8A7E),
                borderRadius: BorderRadius.circular(8),
              ),
              child: const Icon(Icons.psychology, color: Colors.white, size: 20),
            ),
            const SizedBox(width: 10),
            Text(
              titles[safeIndex],
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
            ),
          ],
        ),
        backgroundColor: const Color(0xFF0B4F5C),
        foregroundColor: Colors.white,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            tooltip: 'Cerrar sesión',
            onPressed: () async {
              await authProvider.logout();
              if (context.mounted) {
                Navigator.of(context).pushNamedAndRemoveUntil('/login', (_) => false);
              }
            },
          ),
        ],
      ),
      body: IndexedStack(
        index: safeIndex,
        children: tabViews,
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: safeIndex,
        onDestinationSelected: (idx) => setState(() => _currentIndex = idx),
        backgroundColor: Colors.white,
        indicatorColor: const Color(0xFFE0F2FE),
        elevation: 8,
        destinations: destinations,
      ),
    );
  }
}
