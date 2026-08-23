import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../../../services/auth.service';

@Component({
  selector: 'app-password-reset',
  standalone: false,
  templateUrl: './password-reset.component.html',
  styleUrls: ['./password-reset.component.css']
})
export class PasswordResetComponent implements OnInit {
  resetForm: FormGroup;
  isConfirmMode: boolean = false;
  token: string | null = null;
  isLoading: boolean = false;
  successMessage: string = '';
  errorMessage: string = '';

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.resetForm = this.fb.group({
      email: [''],
      newPassword: [''],
      confirmPassword: ['']
    });
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      if (params['token']) {
        this.token = params['token'];
        this.isConfirmMode = true;
        
        this.resetForm = this.fb.group({
          newPassword: ['', [Validators.required, Validators.minLength(8)]],
          confirmPassword: ['', Validators.required]
        });
      } else {
        this.resetForm = this.fb.group({
          email: ['', [Validators.required, Validators.email]]
        });
      }
    });
  }

  onSubmit() {
    if (this.resetForm.invalid) return;

    this.isLoading = true;
    this.errorMessage = '';
    this.successMessage = '';

    if (this.isConfirmMode && this.token) {
      const { newPassword, confirmPassword } = this.resetForm.value;
      
      if (newPassword !== confirmPassword) {
        this.errorMessage = 'Las contraseñas no coinciden';
        this.isLoading = false;
        return;
      }

      this.authService.confirmPasswordReset(this.token, newPassword).subscribe({
        next: (res: any) => {
          this.isLoading = false;
          this.successMessage = res.message;
          setTimeout(() => this.router.navigate(['/login']), 3000);
        },
        error: (err: any) => {
          this.isLoading = false;
          this.errorMessage = err.error?.error || 'Error al restablecer contraseña';
        }
      });

    } else {
      const { email } = this.resetForm.value;
      this.authService.requestPasswordReset(email).subscribe({
        next: (res: any) => {
          this.isLoading = false;
          this.successMessage = res.message;
        },
        error: (err: any) => {
          this.isLoading = false;
          this.errorMessage = 'Ocurrió un error al procesar la solicitud';
        }
      });
    }
  }
}
