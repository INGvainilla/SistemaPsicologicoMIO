import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';
import { Router } from '@angular/router';
import { TenantService } from '../../../../services/tenant.service';
import { AuthService } from '../../../../services/auth.service';

export function securePasswordValidator(): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const value = control.value;
    if (!value) return null;
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
  selector: 'app-tenant-form',
  standalone: false,
  templateUrl: './tenant-form.component.html',
  styleUrls: ['./tenant-form.component.css']
})
export class TenantFormComponent implements OnInit {
  tenantForm: FormGroup;
  isLoading = false;
  errorMessage = '';
  successMessage = '';

  constructor(
    private fb: FormBuilder,
    private tenantService: TenantService,
    private authService: AuthService,
    private router: Router
  ) {
    this.tenantForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      schema_name: ['', [Validators.required, Validators.pattern(/^[a-z0-9_]+$/)]],
      domain_url: ['', Validators.required],
      admin_name: ['', [Validators.required, Validators.minLength(2)]],
      admin_email: ['', [Validators.required, Validators.email]],
      admin_password: ['Sigepsi2026!', [Validators.required, securePasswordValidator()]]
    });
  }

  ngOnInit(): void {
    // Auto-completar schema, dominio y sugerencia de correo administrador
    this.tenantForm.get('name')?.valueChanges.subscribe(name => {
      if (name && !this.tenantForm.get('schema_name')?.dirty) {
        const slug = name
          .toLowerCase()
          .normalize('NFD')
          .replace(/[\u0300-\u036f]/g, '')
          .replace(/[^a-z0-9]/g, '_')
          .replace(/_+/g, '_')
          .replace(/^_|_$/g, '');
        
        this.tenantForm.patchValue({
          schema_name: slug,
          domain_url: `${slug.replace(/_/g, '-')}.localhost`,
          admin_email: !this.tenantForm.get('admin_email')?.dirty ? `admin.${slug.replace(/_/g, '')}@sigepsi.com` : undefined
        }, { emitEvent: false });
      }
    });

    this.tenantForm.get('schema_name')?.valueChanges.subscribe(schema => {
      if (schema && !this.tenantForm.get('domain_url')?.dirty) {
        this.tenantForm.patchValue({
          domain_url: `${schema.replace(/_/g, '-')}.localhost`
        }, { emitEvent: false });
      }
    });
  }

  private extractErrorMessage(err: any): string {
    if (!err) return 'Error al registrar el centro.';
    if (typeof err.error === 'string') return err.error;
    if (err.error && typeof err.error === 'object') {
      const messages: string[] = [];
      for (const key of Object.keys(err.error)) {
        const val = err.error[key];
        if (Array.isArray(val)) {
          messages.push(`${key}: ${val.join(' ')}`);
        } else if (typeof val === 'string') {
          messages.push(`${key}: ${val}`);
        }
      }
      if (messages.length > 0) {
        return messages.join(' | ');
      }
    }
    return err.message || 'Error al procesar la solicitud.';
  }

  onSubmit(): void {
    if (this.tenantForm.invalid) {
      this.tenantForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';
    this.successMessage = '';

    const payload = { ...this.tenantForm.value };
    payload.name = payload.name.trim();
    payload.schema_name = payload.schema_name.trim().toLowerCase();
    payload.domain_url = payload.domain_url.trim().toLowerCase();
    payload.admin_name = payload.admin_name.trim();
    payload.admin_email = payload.admin_email.trim().toLowerCase();

    this.tenantService.createTenant(payload).subscribe({
      next: (res: any) => {
        this.isLoading = false;
        this.successMessage = `¡Centro "${payload.name}" registrado con éxito! Su Administrador (${payload.admin_email}) ya puede acceder.`;
        setTimeout(() => {
          this.router.navigate(['/tenants']);
        }, 1800);
      },
      error: (err: any) => {
        this.isLoading = false;
        this.errorMessage = this.extractErrorMessage(err);
      }
    });
  }

  get passwordControl() {
    return this.tenantForm.get('admin_password');
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
