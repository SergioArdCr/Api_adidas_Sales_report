# 🛒 Adidas Sales Report API

**ES**

---

## 📌 Descripción

API REST que expone el dataset real de ventas de Adidas US con autenticación JWT, construida con FastAPI y SQLAlchemy ORM. Permite consultar ventas por región, producto y estado, además de un CRUD completo de registros. Dockerizada y desplegada en Railway.

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo backend.

**URL en producción:** https://apiadidassalesreport-production.up.railway.app/docs

## 🛠️ Tecnologías

- `FastAPI` — framework web para construir la API
- `SQLAlchemy` — ORM para manejo de base de datos
- `SQLite` — base de datos relacional
- `JWT` + `bcrypt` — autenticación y hashing de contraseñas
- `pytest` — tests automatizados
- `Docker` — contenedorización
- `Railway` — deploy en producción

## 📁 Estructura

```
app/
├── main.py
├── db/
│   └── database.py
├── models/
│   ├── ventas.py
│   └── usuarios.py
├── routers/
│   ├── auth.py
│   └── endpoints.py
└── services/
    └── auth_services.py
config/
└── settings.py
data/
└── Ventas.db
tests/
├── test_auth.py
└── test_ventas.py
Dockerfile
requirements.txt
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/Api_adidas_Sales_report.git
cd Api_adidas_Sales_report

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
echo "SECRET_KEY=tu_clave_secreta" > .env

# Correr el servidor
uvicorn app.main:app --reload
```

## 🐳 Correr con Docker

```bash
docker build -t adidas-api .
docker run -p 8000:8000 adidas-api
```

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```
SECRET_KEY=tu_clave_secreta
```

## 🚀 Endpoints

### Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/register` | Registrar nuevo usuario |
| POST | `/auth/login` | Login y obtener token JWT |

### Ventas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/regiones` | Obtener todas las regiones |
| GET | `/ventas/{region}` | Ventas por región |
| GET | `/ventas/producto/{region}` | Ventas agrupadas por producto |
| GET | `/ventas/estado/{region}` | Ventas agrupadas por estado |
| POST | `/ventas` | Crear registro de venta |
| PUT | `/ventas/{id}` | Actualizar registro de venta |
| DELETE | `/ventas/{id}` | Eliminar registro de venta |

## 🧪 Correr tests

```bash
pytest tests/ -v
```

## 💡 Ejemplo de uso

```python
import httpx

# Login
response = httpx.post("https://apiadidassalesreport-production.up.railway.app/auth/login", data={
    "username": "tu_usuario",
    "password": "tu_contraseña"
})
token = response.json()["access_token"]

# Obtener regiones
headers = {"Authorization": f"Bearer {token}"}
regiones = httpx.get("https://apiadidassalesreport-production.up.railway.app/regiones", headers=headers)
print(regiones.json())
```

## 💡 Aprendizajes clave

- Construcción de API REST con FastAPI y SQLAlchemy ORM
- Autenticación con JWT y hashing de contraseñas con bcrypt
- Protección de rutas con `Depends`
- Testing de endpoints con `TestClient` de FastAPI
- Contenedorización con Docker y deploy en Railway

---

---

# 🛒 Adidas Sales Report API

**EN**

---

## 📌 Description

REST API that exposes the real Adidas US sales dataset with JWT authentication, built with FastAPI and SQLAlchemy ORM. Allows querying sales by region, product and state, plus full CRUD for sales records. Dockerized and deployed on Railway.

Built as part of a Python learning plan focused on backend development.

**Live URL:** https://apiadidassalesreport-production.up.railway.app/docs

## 🛠️ Tech Stack

- `FastAPI` — web framework for building the API
- `SQLAlchemy` — ORM for database management
- `SQLite` — relational database
- `JWT` + `bcrypt` — authentication and password hashing
- `pytest` — automated tests
- `Docker` — containerization
- `Railway` — production deploy

## 📁 Structure

```
app/
├── db/
│   └── database.py
├── models/
│   ├── ventas.py
│   └── usuarios.py
├── routers/
│   ├── auth.py
│   └── endpoints.py
└── services/
    └── auth_services.py
config/
└── settings.py
data/
└── Ventas.db
tests/
├── test_auth.py
└── test_ventas.py
Dockerfile
requirements.txt
```

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/Api_adidas_Sales_report.git
cd Api_adidas_Sales_report

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "SECRET_KEY=your_secret_key" > .env

# Run the server
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t adidas-api .
docker run -p 8000:8000 adidas-api
```

## 🔐 Environment Variables

Create a `.env` file at the project root:

```
SECRET_KEY=your_secret_key
```

## 🚀 Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get JWT token |

### Sales
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/regiones` | Get all regions |
| GET | `/ventas/{region}` | Sales by region |
| GET | `/ventas/producto/{region}` | Sales grouped by product |
| GET | `/ventas/estado/{region}` | Sales grouped by state |
| POST | `/ventas` | Create sale record |
| PUT | `/ventas/{id}` | Update sale record |
| DELETE | `/ventas/{id}` | Delete sale record |

## 🧪 Run Tests

```bash
pytest tests/ -v
```

## 💡 Usage Example

```python
import httpx

# Login
response = httpx.post("https://apiadidassalesreport-production.up.railway.app/auth/login", data={
    "username": "your_user",
    "password": "your_password"
})
token = response.json()["access_token"]

# Get regions
headers = {"Authorization": f"Bearer {token}"}
regions = httpx.get("https://apiadidassalesreport-production.up.railway.app/regiones", headers=headers)
print(regions.json())
```

## 💡 Key Learnings

- Building REST APIs with FastAPI and SQLAlchemy ORM
- JWT authentication and password hashing with bcrypt
- Route protection with `Depends`
- Endpoint testing with FastAPI's `TestClient`
- Docker containerization and Railway deployment
