import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from '../../../../services/auth.service';

@Component({
  selector: 'app-admin-layout',
  standalone: false,
  templateUrl: './admin-layout.component.html',
  styleUrls: ['./admin-layout.component.css']
})
export class AdminLayoutComponent implements OnInit, OnDestroy {
  currentUser: any = null;
  private userSub!: Subscription;

  constructor(
    public authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.currentUser = this.authService.getCurrentUser();
    this.userSub = this.authService.currentUser$.subscribe(user => {
      this.currentUser = user;
    });

    // Asegurar que el perfil esté fresco desde el backend
    if (this.authService.isLoggedIn() && !this.currentUser) {
      this.authService.fetchMe().subscribe({
        error: () => this.logout()
      });
    }
  }

  ngOnDestroy(): void {
    if (this.userSub) {
      this.userSub.unsubscribe();
    }
  }

  get userName(): string {
    if (!this.currentUser) return 'Cargando...';
    if (this.currentUser.first_name) {
      return `${this.currentUser.first_name} ${this.currentUser.last_name || ''}`.trim();
    }
    return this.currentUser.email?.split('@')[0] || 'Usuario';
  }

  get userRole(): string {
    if (!this.currentUser) return '';
    if (this.currentUser.is_superuser) return 'SuperAdmin Global';
    if (Array.isArray(this.currentUser.roles) && this.currentUser.roles.length > 0) {
      return this.currentUser.roles[0];
    }
    return 'Personal';
  }

  get tenantName(): string {
    if (this.currentUser?.tenant?.name) {
      return this.currentUser.tenant.name;
    }
    return 'SIGEPSI';
  }

  get isPaciente(): boolean {
    return this.authService.isPaciente();
  }

  logout(): void {
    this.authService.logout();
  }
}
