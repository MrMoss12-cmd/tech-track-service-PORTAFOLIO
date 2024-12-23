# Tech-Track-Service

**Tech-Track-Service** es una solución basada en Django diseñada para operar como un servicio de Windows. Su propósito es gestionar y monitorear información de equipos en una empresa, almacenando datos en una base de datos SQLite y brindando una API para interactuar con estos datos.

---

## Características

- **Modelo `Equipment`**: 
  - Almacena información clave de los equipos, como nombre, dirección IP y estado (activo o inactivo).
  - Métodos personalizados para activar, desactivar y gestionar equipos.
  
- **Servicio de Windows**:
  - Diseñado para instalarse y ejecutarse como un servicio de Windows.
  - Se puede iniciar automáticamente al arrancar el sistema operativo.

- **API REST**:
  - Documentada con Swagger.
  - Permite acceder, crear, actualizar y eliminar registros de equipos.

---

## Requisitos

### Software
- **Python**: Versión 3.10 o superior.
- **Django**: Versión 4.x.
- **Dependencias adicionales**:
  - `pywin32`: Para manejar la integración con servicios de Windows.
  - `djangorestframework`: Para construir la API REST.
  - `argparse`: Para el instalador de línea de comandos.

### Sistema Operativo
- **Windows 10 o superior**: Requerido para ejecutar como servicio.

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tech-track-service.git
cd tech-track-service
