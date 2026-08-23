import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { Paquete1AdminSeguridadRoutingModule } from './paquete1-admin-seguridad-routing.module';
import { LoginComponent } from '../paquete1_admin_seguridad/components/login/login.component';

@NgModule({
  declarations: [
    LoginComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    Paquete1AdminSeguridadRoutingModule
  ]
})
export class Paquete1AdminSeguridadModule { }
