# 🚀 Guía Definitiva de Instalación (SIGEPSI)
**De 0 a 100: Cómo levantar el entorno completo en tu máquina local.**

Esta guía está diseñada para que cualquier desarrollador pueda descargar el repositorio y poner a funcionar el sistema en menos de 10 minutos.

---

## 🛠️ 0. Requisitos Previos
Antes de empezar, asegúrate de tener instalados los siguientes programas:
1. **Python** (versión 3.10 o superior)
2. **Node.js** (versión 18 o superior)
3. **Angular CLI** (instálalo globalmente con: `npm install -g @angular/cli`)
4. **PostgreSQL / pgAdmin** (versión 14 o superior)

---

## 🐘 1. Preparar la Base de Datos (pgAdmin)
1. Abre tu pgAdmin y conéctate a tu servidor local.
2. Haz clic derecho en *Databases* -> *Create* -> *Database...*
3. En el nombre de la base de datos escribe **EXACTAMENTE**: `sigepsi_db`.
4. Guarda y cierra. No tienes que crear ninguna tabla a mano.

---

## ⚙️ 2. Levantar el BACKEND (Django)

Abre una terminal y dirígete a la carpeta `BACKEND`:
```bash
cd BACKEND
```

**A. Variables de Entorno:**
1. Haz una copia del archivo `.env.example` y renómbralo a `.env`.
2. Ábrelo y cambia el valor de `TU_CONTRASEÑA_DE_POSTGRES` por la contraseña que usas en tu pgAdmin.

**B. Entorno Virtual y Dependencias:**
Crea una "burbuja" de Python para instalar las librerías del proyecto sin afectar tu PC:
```bash
python -m venv venv
```
Activa el entorno:
*   En Windows: `venv\Scripts\activate`
*   En Mac/Linux: `source venv/bin/activate`

Instala las librerías:
```bash
pip install -r requirements.txt
```

**C. Migrar Tablas e Inicializar Datos:**
Si estás en Windows, puedes simplemente hacer **doble clic en el archivo `migrar_bd.bat`**. 
O si prefieres la consola, ejecuta:
```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
```
*(Si revisas tu pgAdmin ahora, verás que aparecieron 17 tablas automáticamente).*

Ahora, crea el usuario Administrador y la Clínica global ejecutando:
```bash
python manage.py init_system
```

**D. Iniciar el Servidor:**
```bash
python manage.py runserver
```
Déjalo corriendo. El backend ahora vive en `http://localhost:8000`.

---

## 🎨 3. Levantar el FRONTEND (Angular)

Abre **una nueva pestaña en tu terminal** (no cierres la de Django) y dirígete a la carpeta `FRONTEND`:
```bash
cd FRONTEND
```

Instala las dependencias de Node:
```bash
npm install
```

Levanta el servidor de la interfaz:
```bash
npm start
```
(O puedes usar `ng serve`). El frontend ahora vive en `http://localhost:4200`.

---

## 🧪 4. Probar el Sistema
Con el Backend y el Frontend corriendo simultáneamente:
1. Abre tu navegador web favorito.
2. Ingresa a la URL: **[http://localhost:4200/login](http://localhost:4200/login)**
3. Inicia sesión con las credenciales que se generaron en el paso de inicialización:
   *   **Correo:** `admin@sigepsi.com`
   *   **Contraseña:** `admin123`

¡Listo! Si ves el mensaje de acceso exitoso, significa que el entorno Multi-Tenant, la API, JWT, la base de datos y la vista gráfica están perfectamente conectados.
