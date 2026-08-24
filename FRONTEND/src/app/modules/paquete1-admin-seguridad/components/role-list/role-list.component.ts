import { Component, OnInit } from '@angular/core';
import { RoleService } from '../../../../services/role.service';

@Component({
  selector: 'app-role-list',
  standalone: false,
  templateUrl: './role-list.component.html',
  styleUrls: ['./role-list.component.css']
})
export class RoleListComponent implements OnInit {
  roles: any[] = [];
  filteredRoles: any[] = [];
  searchTerm: string = '';
  isLoading = true;
  errorMessage = '';
  successMessage = '';

  constructor(private roleService: RoleService) {}

  ngOnInit(): void {
    this.loadRoles();
  }

  loadRoles(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.roleService.getRoles().subscribe({
      next: (data) => {
        this.roles = data;
        this.applyFilter();
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error cargando roles', err);
        this.errorMessage = 'No se pudieron cargar los roles del sistema.';
        this.isLoading = false;
      }
    });
  }

  applyFilter(): void {
    if (!this.searchTerm || this.searchTerm.trim() === '') {
      this.filteredRoles = [...this.roles];
    } else {
      const term = this.searchTerm.toLowerCase().trim();
      this.filteredRoles = this.roles.filter(r => 
        r.name?.toLowerCase().includes(term) || 
        r.description?.toLowerCase().includes(term)
      );
    }
  }

  deleteRole(role: any): void {
    const isSystemRole = ['superadmin', 'admincentro', 'psicologo', 'psicólogo', 'paciente', 'recepcionista']
      .includes(role.name?.toLowerCase());

    if (isSystemRole) {
      this.errorMessage = `El rol "${role.name}" es un rol base del sistema y no puede ser eliminado.`;
      setTimeout(() => this.errorMessage = '', 4000);
      return;
    }

    if (confirm(`¿Estás seguro de eliminar el rol "${role.name}"? Esta acción no se puede deshacer.`)) {
      this.roleService.deleteRole(role.id).subscribe({
        next: () => {
          this.successMessage = `Rol "${role.name}" eliminado exitosamente.`;
          this.loadRoles();
          setTimeout(() => this.successMessage = '', 3500);
        },
        error: (err) => {
          this.errorMessage = err.error?.error || 'No se pudo eliminar el rol.';
          setTimeout(() => this.errorMessage = '', 4000);
        }
      });
    }
  }

  isProtectedRole(roleName: string): boolean {
    if (!roleName) return false;
    return ['superadmin', 'admincentro', 'psicologo', 'psicólogo', 'paciente', 'recepcionista']
      .includes(roleName.toLowerCase());
  }
}
