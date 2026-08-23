import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../../../../services/user.service';
import { RoleService } from '../../../../services/role.service';

@Component({
  selector: 'app-user-form',
  standalone: false,
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
  userForm: FormGroup;
  roles: any[] = [];
  isLoading = false;
  errorMessage = '';

  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private roleService: RoleService,
    private router: Router
  ) {
    this.userForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(8)]],
      role_id: ['', Validators.required],
      is_active: [true]
    });
  }

  ngOnInit(): void {
    this.loadRoles();
  }

  loadRoles() {
    this.roleService.getRoles().subscribe({
      next: (data) => this.roles = data,
      error: (err) => console.error('Error', err)
    });
  }

  onSubmit() {
    if (this.userForm.valid) {
      this.isLoading = true;
      const formData = { ...this.userForm.value };
      
      // La API de Django usa 'username' como campo requerido, usaremos el email sin @
      formData.username = formData.email.split('@')[0];
      
      // Transformar role_id a array de roles para la API (M2M)
      formData.roles = [parseInt(formData.role_id, 10)];
      delete formData.role_id;

      this.userService.createUser(formData).subscribe({
        next: () => {
          this.isLoading = false;
          this.router.navigate(['/users']);
        },
        error: (err) => {
          this.isLoading = false;
          this.errorMessage = err.error?.email?.[0] || 'Hubo un error al crear el usuario. Verifica los datos.';
        }
      });
    }
  }
}
