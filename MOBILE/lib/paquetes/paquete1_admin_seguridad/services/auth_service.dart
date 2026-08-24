import '../../../core/config/api_config.dart';
import '../../../core/network/api_client.dart';
import '../../../core/storage/token_storage.dart';
import '../models/auth_tokens.dart';
import '../models/usuario.dart';

/// CU02 — Gestionar inicio de sesión y autenticación (HU-01, HU-02, HU-09).
class AuthService {
  AuthService({ApiClient? apiClient, TokenStorage? tokenStorage})
    : _apiClient = apiClient ?? ApiClient(),
      _tokenStorage = tokenStorage ?? TokenStorage();

  final ApiClient _apiClient;
  final TokenStorage _tokenStorage;

  /// Registra un nuevo paciente y deja la sesión iniciada.
  Future<Usuario> register({
    required String email,
    required String password,
    required String firstName,
    required String lastName,
    String phone = '',
  }) async {
    final response = await _apiClient.post(ApiConfig.registerEndpoint, {
      'email': email.trim().toLowerCase(),
      'password': password,
      'first_name': firstName.trim(),
      'last_name': lastName.trim(),
      'phone': phone.trim(),
    });

    final tokens = AuthTokens.fromJson(response as Map<String, dynamic>);
    await _tokenStorage.saveTokens(
      access: tokens.access,
      refresh: tokens.refresh,
    );
    return Usuario.fromJson(response['user'] as Map<String, dynamic>);
  }

  /// Inicia sesión con credenciales existentes.
  Future<Usuario> login({
    required String email,
    required String password,
  }) async {
    final response = await _apiClient.post(ApiConfig.loginEndpoint, {
      'email': email.trim().toLowerCase(),
      'password': password,
    });

    final tokens = AuthTokens.fromJson(response as Map<String, dynamic>);
    await _tokenStorage.saveTokens(
      access: tokens.access,
      refresh: tokens.refresh,
    );
    return fetchMe();
  }

  Future<Usuario> fetchMe() async {
    final response = await _apiClient.get(
      ApiConfig.meEndpoint,
      authenticated: true,
    );
    return Usuario.fromJson(response as Map<String, dynamic>);
  }

  /// Actualiza los datos del perfil del usuario y opcionalmente su contraseña.
  Future<Usuario> updateProfile({
    required String id,
    required String firstName,
    required String lastName,
    String? phone,
    String? email,
    String? password,
  }) async {
    final Map<String, dynamic> body = {
      'first_name': firstName.trim(),
      'last_name': lastName.trim(),
      'phone': (phone ?? '').trim(),
    };
    if (email != null && email.isNotEmpty) {
      body['email'] = email.trim().toLowerCase();
    }
    if (password != null && password.isNotEmpty) {
      body['password'] = password;
    }

    await _apiClient.put(
      '/users/usuarios/$id/',
      body,
      authenticated: true,
    );
    return fetchMe();
  }

  // --- GESTIÓN DE USUARIOS ---

  Future<List<dynamic>> fetchUsers({String? search, String? role}) async {
    String path = '/users/usuarios/';
    final List<String> params = [];
    if (search != null && search.trim().isNotEmpty) {
      params.add('search=${Uri.encodeComponent(search.trim())}');
    }
    if (role != null && role.trim().isNotEmpty && role != 'Todos') {
      params.add('role=${Uri.encodeComponent(role.trim())}');
    }
    if (params.isNotEmpty) {
      path += '?${params.join('&')}';
    }

    final response = await _apiClient.get(path, authenticated: true);
    if (response is List) return response;
    return [];
  }

  Future<dynamic> createUser(Map<String, dynamic> userData) async {
    return _apiClient.post('/users/usuarios/', userData, authenticated: true);
  }

  Future<dynamic> updateUser(String id, Map<String, dynamic> userData) async {
    return _apiClient.put('/users/usuarios/$id/', userData, authenticated: true);
  }

  Future<dynamic> deleteUser(String id) async {
    return _apiClient.delete('/users/usuarios/$id/', authenticated: true);
  }

  // --- GESTIÓN DE CENTROS (TENANTS) ---

  Future<List<dynamic>> fetchTenants() async {
    final response = await _apiClient.get('/tenants/', authenticated: true);
    if (response is List) return response;
    return [];
  }

  Future<dynamic> createTenant(Map<String, dynamic> tenantData) async {
    return _apiClient.post('/tenants/', tenantData, authenticated: true);
  }

  // --- GESTIÓN DE ROLES Y PERMISOS ---

  Future<List<dynamic>> fetchRoles() async {
    final response = await _apiClient.get('/users/roles/', authenticated: true);
    if (response is List) return response;
    return [];
  }

  Future<List<dynamic>> fetchPermissions() async {
    final response = await _apiClient.get('/users/permisos/', authenticated: true);
    if (response is List) return response;
    return [];
  }

  Future<dynamic> createRole(Map<String, dynamic> roleData) async {
    return _apiClient.post('/users/roles/', roleData, authenticated: true);
  }

  Future<dynamic> updateRole(String id, Map<String, dynamic> roleData) async {
    return _apiClient.put('/users/roles/$id/', roleData, authenticated: true);
  }

  Future<dynamic> deleteRole(String id) async {
    return _apiClient.delete('/users/roles/$id/', authenticated: true);
  }

  // --- SESIÓN ---

  Future<void> refreshToken() async {
    final refresh = await _tokenStorage.readRefreshToken();
    if (refresh == null) return;
    final response = await _apiClient.post(ApiConfig.refreshEndpoint, {
      'refresh': refresh,
    });
    await _tokenStorage.saveAccessToken((response as Map<String, dynamic>)['access'] as String);
  }

  Future<void> logout() async {
    await _tokenStorage.clear();
  }

  Future<bool> hasSession() async {
    final token = await _tokenStorage.readAccessToken();
    return token != null;
  }
}
