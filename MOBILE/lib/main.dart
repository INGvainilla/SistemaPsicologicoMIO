import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'paquetes/paquete1_admin_seguridad/providers/auth_provider.dart';
import 'paquetes/paquete1_admin_seguridad/screens/edit_profile_screen.dart';
import 'paquetes/paquete1_admin_seguridad/screens/forgot_password_screen.dart';
import 'paquetes/paquete1_admin_seguridad/screens/login_screen.dart';
import 'paquetes/paquete1_admin_seguridad/screens/register_screen.dart';
import 'shell/home/screens/home_screen.dart';
import 'shell/splash/screens/splash_screen.dart';

void main() {
  runApp(const SigepsiApp());
}

class SigepsiApp extends StatelessWidget {
  const SigepsiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => AuthProvider(),
      child: MaterialApp(
        title: 'SIGEPSI Móvil',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorSchemeSeed: const Color(0xFF0B4F5C),
          useMaterial3: true,
          scaffoldBackgroundColor: const Color(0xFFF1F5F9),
        ),
        initialRoute: SplashScreen.routeName,
        routes: {
          SplashScreen.routeName: (_) => const SplashScreen(),
          LoginScreen.routeName: (_) => const LoginScreen(),
          RegisterScreen.routeName: (_) => const RegisterScreen(),
          ForgotPasswordScreen.routeName: (_) => const ForgotPasswordScreen(),
          EditProfileScreen.routeName: (_) => const EditProfileScreen(),
          HomeScreen.routeName: (_) => const HomeScreen(),
        },
      ),
    );
  }
}
