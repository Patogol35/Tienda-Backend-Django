🛒 Tienda Backend

Proyecto de **tienda online** desarrollado con **Django + Django REST Framework + MySQL**, que incluye gestión de productos, carritos de compra, pedidos y autenticación con **JWT**.

---

## 🚀 Tecnologías usadas
- [Django 5.2](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT (SimpleJWT)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [MySQL](https://www.mysql.com/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [Pillow](https://pillow.readthedocs.io/)

---

⚙️ Instalación y configuración

1. Clonar repositorio

git clone https://github.com/tuusuario/tienda-backend.git
cd tienda-backend

2. Crear entorno virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instalar dependencias

pip install mysql

pip install -r requirements.txt

4. Configurar base de datos

Crea la base en MySQL:

CREATE DATABASE tienda_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

En settings.py asegúrate de configurar:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tienda_db',
        'USER': 'root',
        'PASSWORD': 'tu clave',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Migraciones

python manage.py makemigrations
python manage.py migrate

6. Crear superusuario

python manage.py createsuperuser

7. Correr el servidor

python manage.py runserver


---

🔑 Endpoints principales

Autenticación (JWT)

POST /api/register/ → Registrar usuario

POST /api/token/ → Obtener token de acceso

POST /api/token/refresh/ → Refrescar token


Productos

GET /api/productos/ → Listar productos

POST /api/productos/ → Crear producto (admin)

PUT /api/productos/{id}/ → Editar producto

DELETE /api/productos/{id}/ → Eliminar producto


Carrito

GET /api/carrito/ → Ver carrito del usuario

POST /api/carrito/agregar/ → Agregar producto al carrito


Pedidos

POST /api/pedido/crear/ → Crear pedido desde carrito

GET /api/pedidos/ → Listar pedidos del usuario



---

📸 Panel de administración

Accede a:

http://127.0.0.1:8000/admin/

Aquí puedes gestionar productos, carritos, pedidos y usuarios.


---

✅ Próximos pasos / Mejoras

[ ] Documentación de la API con Swagger o ReDoc.

[ ] Tests automatizados.

[ ] Integración con un frontend en React/Angular.

[ ] Manejo de pagos y envíos.



---

👨‍💻 Autor

Proyecto creado por Jorge Patricio ✨
