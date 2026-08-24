import { Component, OnInit } from '@angular/core';
import { TenantService } from '../../../../services/tenant.service';

@Component({
  selector: 'app-tenant-list',
  standalone: false,
  templateUrl: './tenant-list.component.html',
  styleUrls: ['./tenant-list.component.css']
})
export class TenantListComponent implements OnInit {
  tenants: any[] = [];
  isLoading = true;
  errorMessage = '';
  successMessage = '';

  constructor(private tenantService: TenantService) {}

  ngOnInit(): void {
    this.loadTenants();
  }

  loadTenants(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.tenantService.getTenants().subscribe({
      next: (data) => {
        this.tenants = data;
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error cargando centros', err);
        this.errorMessage = 'No se pudieron cargar los centros psicológicos.';
        this.isLoading = false;
      }
    });
  }

  toggleActive(tenant: any): void {
    if (tenant.schema_name === 'public') {
      return;
    }
    this.tenantService.toggleActive(tenant.id).subscribe({
      next: (res: any) => {
        tenant.is_active = res.is_active;
        this.successMessage = res.message || 'Estado actualizado.';
        setTimeout(() => this.successMessage = '', 3500);
      },
      error: (err) => {
        this.errorMessage = err.error?.error || 'Error al cambiar estado del centro.';
        setTimeout(() => this.errorMessage = '', 3500);
      }
    });
  }

  getPrimaryDomain(tenant: any): string {
    if (tenant.domains && tenant.domains.length > 0) {
      const primary = tenant.domains.find((d: any) => d.is_primary);
      return primary ? primary.domain : tenant.domains[0].domain;
    }
    return `${tenant.schema_name}.localhost:8000`;
  }

  get totalActivos(): number {
    return this.tenants.filter(t => t.is_active).length;
  }

  get totalInactivos(): number {
    return this.tenants.filter(t => !t.is_active).length;
  }
}
