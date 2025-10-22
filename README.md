# Super Duper Octo Garbanzo: Aplicación Flask Distribuida con Monitoreo Integral

Este proyecto demuestra una configuración de una aplicación web Flask simple con gestión de usuarios, diseñada para ser desplegada en un entorno distribuido con balanceo de carga, y un sistema de monitoreo robusto utilizando Prometheus y Grafana.

## Descripción del Proyecto

El objetivo principal de este repositorio es mostrar cómo integrar una aplicación web con un stack de monitoreo completo. La aplicación Flask es un ejemplo básico de gestión de usuarios, mientras que el sistema de monitoreo proporciona visibilidad profunda sobre el rendimiento del sistema, la base de datos, el servidor web y la propia aplicación.

## Características

### Aplicación Web (Flask)
-   **Gestión de Usuarios**: Una aplicación Flask sencilla que permite listar y añadir usuarios a una base de datos (implícitamente MySQL).
-   **Interfaz de Usuario**: Utiliza Bootstrap 5 para una interfaz limpia y responsiva.
-   **Diseño Distribuible**: La mención de "instancia balanceada" sugiere que está preparada para funcionar detrás de un balanceador de carga, permitiendo escalar horizontalmente.

### Monitoreo (Prometheus & Grafana)
-   **Dashboard Completo**: Un dashboard de Grafana preconfigurado (`system_monitoring.json`) para una visión integral del sistema.
-   **Uso de Recursos del Sistema**: Monitoreo de CPU, memoria y espacio en disco utilizando `node_exporter`.
-   **Monitoreo de Base de Datos**: Seguimiento de conexiones activas de MySQL utilizando `mysql_exporter`.
-   **Monitoreo de Servidor Web**: Métricas de tráfico de Nginx (implícito, usando `nginx_exporter`).
-   **Monitoreo de Aplicación**:
    -   **Latencia de Requests**: Percentil 95 de la duración de las solicitudes HTTP.
    -   **Requests por Segundo**: Tasa de solicitudes HTTP.
    -   **Tasa de Error HTTP**: Porcentaje de errores 5xx en las solicitudes.
-   **Estado de Servicios**: Visibilidad del estado de salud de los servicios (`up` metric).
-   **Monitoreo de Contenedores**: Uso de recursos por contenedor (implícito, usando `cAdvisor` o similar).
-   **Umbrales Visuales**: Configuración de umbrales de color (verde, amarillo, rojo) en los paneles de Grafana para una rápida identificación de problemas.

## Tecnologías Utilizadas

-   **Backend**: Python, Flask
-   **Frontend**: HTML, Bootstrap 5
-   **Base de Datos**: MySQL (implícito)
-   **Servidor Web/Proxy**: Nginx (implícito)
-   **Monitoreo**:
    -   **Prometheus**: Sistema de monitoreo y alerta de código abierto.
    -   **Grafana**: Plataforma de código abierto para analítica y monitoreo interactivo.
    -   **Node Exporter**: Exportador de métricas del sistema para Prometheus.
    -   **MySQL Exporter**: Exportador de métricas de MySQL para Prometheus.
    -   **Nginx Exporter**: Exportador de métricas de Nginx para Prometheus.
    -   **cAdvisor**: (Implícito) Para métricas de contenedores.
-   **Orquestación/Contenerización**: Docker / Docker Compose o Kubernetes (implícito por la naturaleza distribuida y las métricas de contenedores).

## Estructura del Proyecto

-   `app1/`: Contiene la aplicación Flask, incluyendo sus plantillas HTML (`index.html`, `usuarios.html`).
-   `grafana/`: Contiene la configuración de Grafana, específicamente el dashboard de monitoreo (`system_monitoring.json`) que se provisiona automáticamente.
-   `README.md`: Este archivo.

## Cómo Empezar

Para poner en marcha este proyecto, necesitarás tener Docker y Docker Compose (o un clúster de Kubernetes) instalados.

1.  **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/your-username/super-duper-octo-garbanzo.git
    cd super-duper-octo-garbanzo
    ```

2.  **Configuración de la Aplicación Flask**:
    -   Asegúrate de tener un `requirements.txt` en `app1/` con las dependencias de Flask (e.g., `Flask`, `pymysql` o `psycopg2` si usas otra DB, etc.).
    -   Configura la conexión a tu base de datos MySQL dentro de la aplicación Flask.

3.  **Despliegue con Docker Compose (Ejemplo)**:
    Deberías crear un archivo `docker-compose.yml` en la raíz del proyecto que orqueste los siguientes servicios:
    -   La aplicación Flask (`app1`).
    -   Una instancia de MySQL.
    -   Prometheus con una configuración que recoja métricas de los exporters.
    -   Grafana, con el volumen de provisionamiento apuntando a `grafana/provisioning/dashboards/`.
    -   `node_exporter`.
    -   `mysql_exporter`.
    -   `nginx_exporter` (si Nginx está en uso).
    -   Nginx como proxy inverso para la aplicación Flask.

    Una vez configurado el `docker-compose.yml`, puedes iniciar todos los servicios con:
    ```bash
    docker-compose up -d
    ```

4.  **Acceder a la Aplicación y Monitoreo**:
    -   **Aplicación Flask**: Generalmente accesible a través de Nginx en `http://localhost:80` o `http://localhost:5000` (dependiendo de tu configuración).
    -   **Grafana**: Accesible en `http://localhost:3000`. Las credenciales por defecto suelen ser `admin`/`admin`. El dashboard "Sistema de Monitoreo Completo" debería estar disponible automáticamente.

## Uso

-   Navega a la aplicación Flask para interactuar con la gestión de usuarios.
-   Explora el dashboard de Grafana para visualizar el estado y rendimiento de todos los componentes del sistema.

## PRESENTADO POR:

-Carlos Manrique

-Laura Malagón

-María Medina
