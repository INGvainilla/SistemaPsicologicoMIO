import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { PasswordResetComponent } from './components/password-reset/password-reset.component';
import { PasswordResetConfirmComponent } from './components/password-reset-confirm/password-reset-confirm.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TenantListComponent } from './components/tenant-list/tenant-list.component';
import { TenantFormComponent } from './components/tenant-form/tenant-form.component';
import { UserListComponent } from './components/user-list/user-list.component';
import { UserFormComponent } from './components/user-form/user-form.component';
import { RoleListComponent } from './components/role-list/role-list.component';
import { RoleFormComponent } from './components/role-form/role-form.component';
import { AdminLayoutComponent } from './components/admin-layout/admin-layout.component';

import { authGuard } from '../../guards/auth.guard';
import { superAdminGuard, canManageUsersGuard, canManageRolesGuard } from '../../guards/role.guard';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'password-reset', component: PasswordResetComponent },
  { path: 'password-reset/confirm', component: PasswordResetConfirmComponent },
  { 
    path: '', 
    component: AdminLayoutComponent,
    canActivate: [authGuard],
    children: [
      { path: 'dashboard', component: DashboardComponent },
      
      // Gestión de Centros (Tenants): Exclusivo SuperAdmin
      { path: 'tenants', component: TenantListComponent, canActivate: [superAdminGuard] },
      { path: 'tenants/new', component: TenantFormComponent, canActivate: [superAdminGuard] },
      
      // Gestión de Usuarios: SuperAdmin / AdminCentro / Gestionar Usuarios
      { path: 'users', component: UserListComponent, canActivate: [canManageUsersGuard] },
      { path: 'users/new', component: UserFormComponent, canActivate: [canManageUsersGuard] },
      { path: 'users/edit/:id', component: UserFormComponent, canActivate: [canManageUsersGuard] },
      
      // Gestión de Roles y Permisos: SuperAdmin / AdminCentro / Gestionar Roles
      { path: 'roles', component: RoleListComponent, canActivate: [canManageRolesGuard] },
      { path: 'roles/new', component: RoleFormComponent, canActivate: [canManageRolesGuard] },
      { path: 'roles/edit/:id', component: RoleFormComponent, canActivate: [canManageRolesGuard] },
      
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class Paquete1AdminSeguridadRoutingModule { }
