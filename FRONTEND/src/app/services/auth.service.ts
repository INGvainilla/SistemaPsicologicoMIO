import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap, switchMap, of } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private tokenKey = 'sigepsi_token';
  private userKey = 'sigepsi_user';
  
  private currentUserSubject = new BehaviorSubject<any>(this.getStoredUser());
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) {}

  // URL del backend en Railway — ACTUALIZAR DESPUÉS DEL DEPLOY
  private readonly PRODUCTION_API_URL = 'https://PENDIENTE.up.railway.app/api';

  public getApiBaseUrl(): string {
    const hostname = window.location.hostname || 'localhost';
    // En producción (Vercel u otro dominio), usar la URL de Railway
    if (hostname !== 'localhost' && hostname !== '127.0.0.1' && !hostname.includes('192.168.')) {
      return this.PRODUCTION_API_URL;
    }
    // En desarrollo local
    const port = '8000';
    const protocol = window.location.protocol || 'http:';
    return `${protocol}//${hostname}:${port}/api`;
  }

  private getStoredUser(): any {
    const userStr = localStorage.getItem(this.userKey);
    try {
      return userStr ? JSON.parse(userStr) : null;
    } catch {
      return null;
    }
  }

  login(email: string, password: string): Observable<any> {
    const loginUrl = `${this.getApiBaseUrl()}/users/auth/login/`;
    return this.http.post<any>(loginUrl, { email, password }).pipe(
      tap((res: any) => {
        if (res.access) {
          localStorage.setItem(this.tokenKey, res.access);
        }
      }),
      switchMap(() => this.fetchMe())
    );
  }

  fetchMe(): Observable<any> {
    const meUrl = `${this.getApiBaseUrl()}/users/me/`;
    return this.http.get<any>(meUrl).pipe(
      tap((userData: any) => {
        this.setUser(userData);
      })
    );
  }

  setUser(user: any): void {
    localStorage.setItem(this.userKey, JSON.stringify(user));
    this.currentUserSubject.next(user);
  }

  getCurrentUser(): any {
    return this.currentUserSubject.value;
  }

  logout(): void {
    localStorage.removeItem(this.tokenKey);
    localStorage.removeItem(this.userKey);
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }

  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }

  // --- Role & Permission Helpers ---

  isSuperAdmin(): boolean {
    const user = this.getCurrentUser();
    if (!user) return false;
    if (user.is_superuser) return true;
    return Array.isArray(user.roles) && user.roles.some((r: string) => r.toLowerCase() === 'superadmin');
  }

  isAdminCentro(): boolean {
    const user = this.getCurrentUser();
    if (!user) return false;
    if (this.isSuperAdmin()) return true;
    return Array.isArray(user.roles) && user.roles.some((r: string) => r.toLowerCase() === 'admincentro');
  }

  isPsicologo(): boolean {
    const user = this.getCurrentUser();
    if (!user) return false;
    return Array.isArray(user.roles) && user.roles.some((r: string) => r.toLowerCase().includes('psic'));
  }

  isPaciente(): boolean {
    const user = this.getCurrentUser();
    if (!user) return false;
    if (this.isSuperAdmin() || this.isAdminCentro()) return false;
    return Array.isArray(user.roles) && user.roles.some((r: string) => r.toLowerCase() === 'paciente');
  }

  hasRole(roleName: string): boolean {
    const user = this.getCurrentUser();
    if (!user || !user.roles) return false;
    return user.roles.some((r: string) => r.toLowerCase() === roleName.toLowerCase());
  }

  hasPermission(codename: string): boolean {
    const user = this.getCurrentUser();
    if (!user) return false;
    if (this.isSuperAdmin()) return true;
    return Array.isArray(user.permisos) && user.permisos.includes(codename);
  }

  canManageUsers(): boolean {
    return this.isSuperAdmin() || this.isAdminCentro() || this.hasPermission('gestionar_usuarios');
  }

  canManageRoles(): boolean {
    return this.isSuperAdmin() || this.isAdminCentro() || this.hasPermission('gestionar_roles');
  }

  canManageTenants(): boolean {
    return this.isSuperAdmin() || this.hasPermission('gestionar_centros');
  }

  // --- Password reset ---

  requestPasswordReset(email: string): Observable<any> {
    return this.http.post(`${this.getApiBaseUrl()}/users/auth/password-reset/`, { email });
  }

  confirmPasswordReset(token: string, newPassword: string): Observable<any> {
    return this.http.post(`${this.getApiBaseUrl()}/users/auth/password-reset/confirm/`, {
      token,
      new_password: newPassword
    });
  }

  verifyPasswordResetCode(code: string): Observable<any> {
    return this.http.post(`${this.getApiBaseUrl()}/users/auth/password-reset-verify/`, { code });
  }
}
