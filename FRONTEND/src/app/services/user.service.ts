import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(private http: HttpClient, private authService: AuthService) { }

  private get apiUrl(): string {
    return `${this.authService.getApiBaseUrl()}/users/usuarios/`;
  }

  getUsers(role?: string, search?: string): Observable<any[]> {
    let params = new HttpParams();
    if (role && role !== 'todos') {
      params = params.set('role', role);
    }
    if (search && search.trim() !== '') {
      params = params.set('search', search.trim());
    }
    return this.http.get<any[]>(this.apiUrl, { params });
  }

  getUser(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}${id}/`);
  }

  createUser(user: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, user);
  }

  updateUser(id: string, user: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}${id}/`, user);
  }

  deleteUser(id: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}${id}/`);
  }
}
