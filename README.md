# TPV Bar (Django)

Sistema de punto de venta (TPV) desarrollado en Python con Django, orientado a bares y pequeños negocios.

Este proyecto forma parte de mi portfolio personal y está enfocado al aprendizaje práctico del desarrollo web con Django y la gestión de ventas.

---

## 🧾 Funcionalidades

- Gestión de productos
- Registro de ventas
- Selección de método de pago
- Interfaz web sencilla para el TPV
- Generación de informes básicos

---

## 🛠 Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML / CSS

---

## 📁 Estructura del proyecto

```text
tpv-bar-django/
│
├── core/                 # Lógica principal del TPV
├── tpv_cervezas/         # Configuración del proyecto Django
├── manage.py
├── requirements.txt
└── README.md
```

---

## ▶️ Ejecución

A continuación se muestra cómo ejecutar el proyecto en entorno local:

```bash
git clone https://github.com/YankoArm/tpv-bar-django.git
cd tpv-bar-django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

Una vez iniciado, accede desde el navegador a:

- http://127.0.0.1:8000/
- La ruta raíz redirige automáticamente a la interfaz del TPV.

---

## 🧠 ¿Cómo funciona el TPV?

- El sistema carga los productos disponibles.
- Se registran las ventas a través de la interfaz web.
- Cada venta puede asociarse a un método de pago.
- Los datos se almacenan en una base de datos local SQLite.

---

## 🎯 Objetivo del proyecto

Este proyecto ha sido desarrollado con fines formativos, con el objetivo de:

- Aprender el funcionamiento interno de Django.
- Practicar el desarrollo de aplicaciones web completas.
- Gestionar modelos, vistas y plantillas.
- Simular un caso real de uso de un TPV para hostelería.

---

📌 Notas

- El proyecto se ejecuta de forma local.
- La base de datos no se incluye en el repositorio.
- Pensado como proyecto de aprendizaje y demostración.
