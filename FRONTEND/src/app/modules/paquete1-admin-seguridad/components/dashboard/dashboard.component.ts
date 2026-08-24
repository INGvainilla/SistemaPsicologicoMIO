import { Component, OnInit } from '@angular/core';
import { forkJoin, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AuthService } from '../../../../services/auth.service';
import { TenantService } from '../../../../services/tenant.service';
import { UserService } from '../../../../services/user.service';
import { RoleService } from '../../../../services/role.service';

@Component({
  selector: 'app-dashboard',
  standalone: false,
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  currentUser: any = null;
  totalCentros = 0;
  totalUsuarios = 0;
  totalRoles = 0;
  totalPermisos = 0;
  isLoading = true;

  constructor(
    public authService: AuthService,
    private tenantService: TenantService,
    private userService: UserService,
    private roleService: RoleService
  ) {}

  ngOnInit(): void {
    this.currentUser = this.authService.getCurrentUser();
    this.loadMetrics();
  }

  loadMetrics(): void {
    this.isLoading = true;

    // Construir lista de observables en paralelo
    const requests: Record<string, any> = {
      roles: this.roleService.getRoles().pipe(catchError(() => of([]))),
      permisos: this.roleService.getPermisos().pipe(catchError(() => of([]))),
    };

    if (this.authService.canManageUsers()) {
      requests['users'] = this.userService.getUsers().pipe(catchError(() => of([])));
    }

    if (this.authService.canManageTenants()) {
      requests['tenants'] = this.tenantService.getTenants().pipe(catchError(() => of([])));
    }

    // Ejecutar TODAS en paralelo y esperar a que terminen todas
    forkJoin(requests).subscribe({
      next: (results: any) => {
        this.totalRoles = results['roles']?.length || 0;
        this.totalPermisos = results['permisos']?.length || 0;
        this.totalUsuarios = results['users']?.length || 0;
        this.totalCentros = results['tenants']?.length || 0;
        this.isLoading = false;
      },
      error: () => {
        this.isLoading = false;
      }
    });
  }

  get isPaciente(): boolean {
    return this.authService.isPaciente();
  }

  get isSuperAdmin(): boolean {
    return this.authService.isSuperAdmin();
  }

  get tenantName(): string {
    return this.currentUser?.tenant?.name || 'SIGEPSI';
  }
}
