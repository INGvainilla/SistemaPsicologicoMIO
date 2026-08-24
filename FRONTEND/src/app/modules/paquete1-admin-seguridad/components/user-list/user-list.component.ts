import { Component, OnInit } from '@angular/core';
import { UserService } from '../../../../services/user.service';
import { RoleService } from '../../../../services/role.service';
import { AuthService } from '../../../../services/auth.service';

@Component({
  selector: 'app-user-list',
  standalone: false,
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
  users: any[] = [];
  roles: any[] = [];
  selectedRoleFilter: string = 'todos';
  searchTerm: string = '';
  isLoading = true;
  errorMessage = '';
  successMessage = '';

  constructor(
    private userService: UserService,
    private roleService: RoleService,
    public authService: AuthService
  ) {}

  ngOnInit(): void {
    this.loadRoles();
    this.loadUsers();
  }

  loadRoles(): void {
    this.roleService.getRoles().subscribe({
      next: (data) => this.roles = data,
      error: (err) => console.error('Error cargando roles', err)
    });
  }

  loadUsers(): void {
    this.isLoading = true;
    this.errorMessage = '';
    this.userService.getUsers(this.selectedRoleFilter, this.searchTerm).subscribe({
      next: (data) => {
        this.users = data;
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error cargando usuarios', err);
        this.errorMessage = 'No se pudieron cargar los usuarios.';
        this.isLoading = false;
      }
    });
  }

  onFilterChange(): void {
    this.loadUsers();
  }

  onSearchChange(): void {
    this.loadUsers();
  }

  deleteUser(user: any): void {
    const current = this.authService.getCurrentUser();
    if (current && current.id === user.id) {
      this.errorMessage = 'No puedes eliminar tu propia cuenta de usuario activa.';
      setTimeout(() => this.errorMessage = '', 3500);
      return;
    }

    if (confirm(`¿Estás seguro de eliminar o dar de baja al usuario "${user.first_name} ${user.last_name} (${user.email})"?`)) {
      this.userService.deleteUser(user.id).subscribe({
        next: () => {
          this.successMessage = `Usuario "${user.email}" eliminado correctamente.`;
          this.loadUsers();
          setTimeout(() => this.successMessage = '', 3500);
        },
        error: (err) => {
          this.errorMessage = err.error?.error || 'Error al eliminar el usuario.';
          setTimeout(() => this.errorMessage = '', 3500);
        }
      });
    }
  }

  getUserRoleNames(user: any): string[] {
    if (user.roles_details && user.roles_details.length > 0) {
      return user.roles_details.map((r: any) => r.name);
    }
    if (user.roles && user.roles.length > 0) {
      return user.roles.map((roleId: string) => {
        const found = this.roles.find(r => r.id === roleId);
        return found ? found.name : 'Rol Asignado';
      });
    }
    if (user.is_superuser) {
      return ['SuperAdmin'];
    }
    return ['Sin Rol'];
  }

  getRoleBadgeColor(roleName: string): { bg: string, color: string } {
    const name = roleName.toLowerCase();
    if (name.includes('superadmin')) return { bg: '#e0e7ff', color: '#3730a3' }; // Indigo
    if (name.includes('admincentro')) return { bg: '#fef3c7', color: '#92400e' }; // Amber
    if (name.includes('psic')) return { bg: '#ccfbf1', color: '#115e59' }; // Teal
    if (name.includes('recep')) return { bg: '#e0f2fe', color: '#0369a1' }; // Sky
    if (name.includes('paciente')) return { bg: '#f3e8ff', color: '#6b21a8' }; // Purple
    return { bg: 'var(--color-bg)', color: 'var(--color-text)' };
  }
}
