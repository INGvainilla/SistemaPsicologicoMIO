import 'dart:convert';
import 'package:http/http.dart' as http;

import '../config/api_config.dart';
import '../storage/token_storage.dart';
import 'api_exception.dart';

/// Envoltorio sobre `package:http` para interactuar con la API de SIGEPSI.
/// Inyecta automáticamente el token Bearer JWT y maneja errores HTTP.
class ApiClient {
  ApiClient({http.Client? httpClient, TokenStorage? tokenStorage})
    : _httpClient = httpClient ?? http.Client(),
      _tokenStorage = tokenStorage ?? TokenStorage();

  final http.Client _httpClient;
  final TokenStorage _tokenStorage;

  Future<dynamic> post(
    String path,
    dynamic body, {
    bool authenticated = false,
  }) async {
    final headers = await _buildHeaders(authenticated: authenticated);
    final response = await _httpClient.post(
      Uri.parse('${ApiConfig.baseUrl}$path'),
      headers: headers,
      body: jsonEncode(body),
    );
    return _decode(response);
  }

  Future<dynamic> get(
    String path, {
    bool authenticated = true,
  }) async {
    final headers = await _buildHeaders(authenticated: authenticated);
    final response = await _httpClient.get(
      Uri.parse('${ApiConfig.baseUrl}$path'),
      headers: headers,
    );
    return _decode(response);
  }

  Future<dynamic> put(
    String path,
    dynamic body, {
    bool authenticated = true,
  }) async {
    final headers = await _buildHeaders(authenticated: authenticated);
    final response = await _httpClient.put(
      Uri.parse('${ApiConfig.baseUrl}$path'),
      headers: headers,
      body: jsonEncode(body),
    );
    return _decode(response);
  }

  Future<dynamic> delete(
    String path, {
    bool authenticated = true,
  }) async {
    final headers = await _buildHeaders(authenticated: authenticated);
    final response = await _httpClient.delete(
      Uri.parse('${ApiConfig.baseUrl}$path'),
      headers: headers,
    );
    return _decode(response);
  }

  Future<Map<String, String>> _buildHeaders({
    required bool authenticated,
  }) async {
    final headers = {'Content-Type': 'application/json'};
    if (authenticated) {
      final token = await _tokenStorage.readAccessToken();
      if (token != null) {
        headers['Authorization'] = 'Bearer $token';
      }
    }
    return headers;
  }

  dynamic _decode(http.Response response) {
    if (response.body.isEmpty) {
      return <String, dynamic>{};
    }
    final decodedBody = jsonDecode(response.body);

    if (response.statusCode >= 200 && response.statusCode < 300) {
      return decodedBody;
    }

    if (decodedBody is Map<String, dynamic>) {
      throw ApiException(
        statusCode: response.statusCode,
        message: _extractMessage(decodedBody),
        errors: decodedBody,
      );
    } else {
      throw ApiException(
        statusCode: response.statusCode,
        message: 'Error en el servidor (${response.statusCode})',
      );
    }
  }

  String _extractMessage(Map<String, dynamic> body) {
    if (body.containsKey('detail')) {
      return body['detail'].toString();
    }
    if (body.containsKey('error')) {
      return body['error'].toString();
    }
    if (body.containsKey('message')) {
      return body['message'].toString();
    }
    // DRF suele devolver {"campo": ["mensaje1", "mensaje2"]}
    for (final value in body.values) {
      if (value is List && value.isNotEmpty) {
        return value.first.toString();
      }
      if (value is String && value.isNotEmpty) {
        return value;
      }
    }
    return 'Ocurrió un error inesperado. Intenta de nuevo.';
  }
}
