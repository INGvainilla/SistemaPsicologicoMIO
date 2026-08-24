import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class TenantService {
  constructor(private http: HttpClient, private authService: AuthService) { }

  private get apiUrl(): string {
    return `${this.authService.getApiBaseUrl()}/tenants/`;
  }

  getTenants(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getTenant(id: number | string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}${id}/`);
  }

  createTenant(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

  updateTenant(id: number | string, data: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}${id}/`, data);
  }

  toggleActive(id: number | string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}${id}/toggle-active/`, {});
  }
}
