import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../../../services/user.service';
import { RoleService } from '../../../../services/role.service';

export function optionalSecurePasswordValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const value = control.value;
    if (!value || value.trim() === '') return null;
    const errors: any = {};
    if (value.length < 8) errors.minLengthError = true;
    if (!/[A-Z]/.test(value)) errors.missingUppercase = true;
    if (!/[a-z]/.test(value)) errors.missingLowercase = true;
    if (!/\d/.test(value)) errors.missingNumber = true;
    if (!/[^a-zA-Z0-9]/.test(value)) errors.missingSpecialChar = true;
    return Object.keys(errors).length > 0 ? errors : null;
  };
}

@Component({
  selector: 'app-user-form',
  standalone: false,
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
  userForm: FormGroup;
  roles: any[] = [];
  isEditMode = false;
  userId: string | null = null;
  isLoading = false;
  isSaving = false;
  errorMessage = '';
  successMessage = '';

  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private roleService: RoleService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.userForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      phone: [''],
      password: ['', [optionalSecurePasswordValidator()]],
      role_id: ['', Validators.required],
      is_active: [true]
    });
  }

  ngOnInit(): void {
    this.userId = this.route.snapshot.paramMap.get('id');
    this.isEditMode = !!this.userId;

    if (!this.isEditMode) {
      this.userForm.get('password')?.setValidators([Validators.required, optionalSecurePasswordValidator()]);
      this.userForm.get('password')?.updateValueAndValidity();
    }

    this.loadRoles();
  }

  loadRoles(): void {
    this.isLoading = true;
    this.roleService.getRoles().subscribe({
      next: (data) => {
        this.roles = data;
        if (this.isEditMode && this.userId) {
          this.loadUserForEdit(this.userId);
        } else {
          this.isLoading = false;
        }
      },
      error: (err) => {
        console.error('Error cargando roles', err);
        this.errorMessage = 'No se pudieron cargar los roles para el formulario.';
        this.isLoading = false;
      }
    });
  }

  loadUserForEdit(id: string): void {
    this.userService.getUser(id).subscribe({
      next: (user) => {
        let selectedRoleId = '';
        if (Array.isArray(user.roles) && user.roles.length > 0) {
          selectedRoleId = user.roles[0];
        } else if (Array.isArray(user.roles_details) && user.roles_details.length > 0) {
          selectedRoleId = user.roles_details[0].id;
        }

        this.userForm.patchValue({
          email: user.email,
          first_name: user.first_name,
          last_name: user.last_name,
          phone: user.phone || '',
          role_id: selectedRoleId,
          is_active: user.is_active
        });

        this.isLoading = false;
      },
      error: (err) => {
        console.error('Error cargando usuario para edición', err);
        this.errorMessage = 'No se pudo cargar la información del usuario.';
        this.isLoading = false;
      }
    });
  }

  private extractErrorMessage(err: any): string {
    if (!err) return 'Error al procesar la solicitud.';
    if (typeof err.error === 'string') return err.error;
    if (err.error && typeof err.error === 'object') {
      const messages: string[] = [];
      for (const key of Object.keys(err.error)) {
        const val = err.error[key];
        if (Array.isArray(val)) {
          messages.push(val.join(' '));
        } else if (typeof val === 'string') {
          messages.push(val);
        }
      }
      if (messages.length > 0) {
        return messages.join(' | ');
      }
    }
    return err.message || 'Error al guardar el usuario. Verifica los datos.';
  }

  onSubmit(): void {
    if (this.userForm.invalid) {
      this.userForm.markAllAsTouched();
      return;
    }

    this.isSaving = true;
    this.errorMessage = '';
    this.successMessage = '';

    const formData = { ...this.userForm.value };
    
    // Normalizar email y username
    formData.email = formData.email.trim().toLowerCase();
    formData.username = formData.email;
    formData.first_name = formData.first_name.trim();
    formData.last_name = formData.last_name.trim();
    if (formData.phone) formData.phone = formData.phone.trim();
    
    // Convertir role_id a array de UUIDs (M2M en backend)
    if (formData.role_id) {
      formData.roles = [formData.role_id];
    } else {
      formData.roles = [];
    }
    delete formData.role_id;

    // Si está en modo edición y la contraseña está vacía, no enviarla
    if (this.isEditMode && (!formData.password || formData.password.trim() === '')) {
      delete formData.password;
    }

    if (this.isEditMode && this.userId) {
      this.userService.updateUser(this.userId, formData).subscribe({
        next: () => {
          this.isSaving = false;
          this.successMessage = 'Usuario actualizado exitosamente.';
          setTimeout(() => this.router.navigate(['/users']), 1200);
        },
        error: (err) => {
          this.isSaving = false;
          this.errorMessage = this.extractErrorMessage(err);
        }
      });
    } else {
      this.userService.createUser(formData).subscribe({
        next: () => {
          this.isSaving = false;
          this.successMessage = 'Usuario registrado exitosamente.';
          setTimeout(() => this.router.navigate(['/users']), 1200);
        },
        error: (err) => {
          this.isSaving = false;
          this.errorMessage = this.extractErrorMessage(err);
        }
      });
    }
  }

  get passwordControl() {
    return this.userForm.get('password');
  }

  get hasMinLength(): boolean {
    const val = this.passwordControl?.value || '';
    return val.length >= 8;
  }

  get hasUppercase(): boolean {
    const val = this.passwordControl?.value || '';
    return /[A-Z]/.test(val);
  }

  get hasLowercase(): boolean {
    const val = this.passwordControl?.value || '';
    return /[a-z]/.test(val);
  }

  get hasNumber(): boolean {
    const val = this.passwordControl?.value || '';
    return /\d/.test(val);
  }

  get hasSpecialChar(): boolean {
    const val = this.passwordControl?.value || '';
    return /[^a-zA-Z0-9]/.test(val);
  }
}
