import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { RoleService } from '../../../../services/role.service';

@Component({
  selector: 'app-role-form',
  standalone: false,
  templateUrl: './role-form.component.html',
  styleUrls: ['./role-form.component.css']
})
export class RoleFormComponent implements OnInit {
  roleForm: FormGroup;
  permisosDisponibles: any[] = [];
  selectedPermisos: Set<string> = new Set();
  isEditMode = false;
  roleId: string | null = null;
  isLoading = false;
  isSaving = false;
  errorMessage = '';
  successMessage = '';

  constructor(
    private fb: FormBuilder,
    private roleService: RoleService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.roleForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      description: ['']
    });
  }

  ngOnInit(): void {
    this.roleId = this.route.snapshot.paramMap.get('id');
    this.isEditMode = !!this.roleId;

    this.loadInitialData();
  }

  loadInitialData(): void {
    this.isLoading = true;
    this.roleService.getPermisos().subscribe({
      next: (permisos) => {
        this.permisosDisponibles = permisos;
        
        if (this.isEditMode && this.roleId) {
          this.loadRoleForEdit(this.roleId);
        } else {
          this.isLoading = false;
        }
      },
      error: (err) => {
        console.error('Error cargando permisos', err);
        this.errorMessage = 'No se pudieron cargar los permisos del sistema.';
        this.isLoading = false;
      }
    });
  }

  loadRoleForEdit(id: string): void {
    this.roleService.getRole(id).subscribe({
      next: (role) => {
        this.roleForm.patchValue({
          name: role.name,
          description: role.description || ''
        });

        // Marcar los permisos asignados
        this.selectedPermisos.clear();
        if (Array.isArray(role.permisos)) {
          role.permisos.forEach((pId: any) => this.selectedPermisos.add(pId));
        } else if (Array.isArray(role.permisos_details)) {
          role.permisos_details.forEach((p: any) => this.selectedPermisos.add(p.id));
        }

        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error cargando rol para edición', err);
        this.errorMessage = 'No se pudo cargar la información del rol seleccionado.';
        this.isLoading = false;
      }
    });
  }

  togglePermission(permisoId: string): void {
    if (this.selectedPermisos.has(permisoId)) {
      this.selectedPermisos.delete(permisoId);
    } else {
      this.selectedPermisos.add(permisoId);
    }
  }

  isPermissionSelected(permisoId: string): boolean {
    return this.selectedPermisos.has(permisoId);
  }

  selectAllPermissions(): void {
    this.permisosDisponibles.forEach(p => this.selectedPermisos.add(p.id));
  }

  deselectAllPermissions(): void {
    this.selectedPermisos.clear();
  }

  onSubmit(): void {
    if (this.roleForm.invalid) {
      this.roleForm.markAllAsTouched();
      return;
    }

    this.isSaving = true;
    this.errorMessage = '';

    const payload = {
      name: this.roleForm.value.name.trim(),
      description: this.roleForm.value.description?.trim() || '',
      permisos: Array.from(this.selectedPermisos)
    };

    if (this.isEditMode && this.roleId) {
      this.roleService.updateRole(this.roleId, payload).subscribe({
        next: () => {
          this.isSaving = false;
          this.successMessage = 'Rol actualizado exitosamente.';
          setTimeout(() => this.router.navigate(['/roles']), 1200);
        },
        error: (err) => {
          this.isSaving = false;
          this.errorMessage = err.error?.name?.[0] || err.error?.error || 'Error al actualizar el rol.';
        }
      });
    } else {
      this.roleService.createRole(payload).subscribe({
        next: () => {
          this.isSaving = false;
          this.successMessage = 'Rol creado exitosamente.';
          setTimeout(() => this.router.navigate(['/roles']), 1200);
        },
        error: (err) => {
          this.isSaving = false;
          this.errorMessage = err.error?.name?.[0] || err.error?.error || 'Error al crear el rol.';
        }
      });
    }
  }
}
