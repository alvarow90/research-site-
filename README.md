# Theoretical Computer Science @ Lancaster

Sitio web institucional para un grupo de investigacion en ciencias de la computacion teorica. La aplicacion presenta informacion sobre el grupo, incluyendo personas, lineas de investigacion, seminarios, noticias y oportunidades academicas.

## Descripcion general

Este proyecto es una aplicacion web ligera desarrollada en **Python** usando **Flask**. El contenido se renderiza en el servidor mediante plantillas HTML, mientras que parte de la informacion del sitio se gestiona desde un archivo `JSON`.

El objetivo del proyecto es ofrecer un sitio sencillo de mantener, facil de desplegar y adecuado para contenido academico e institucional.

## Tecnologias utilizadas

- **Python** como lenguaje principal.
- **Flask** como framework web.
- **Jinja2** para el renderizado de plantillas HTML dinamicas.
- **HTML5** para la estructura de las paginas.
- **CSS3** para estilos personalizados.
- **Bootstrap 5** para maquetacion responsive y componentes visuales.
- **JSON** para almacenar parte del contenido del sitio.
- **Vercel** como plataforma de despliegue configurada.

## Estructura del proyecto

```text
research-site-/
├── app.py
├── data.json
├── requirements.txt
├── vercel.json
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── people.html
│   ├── research.html
│   ├── seminars.html
│   └── opportunities.html
```

## Funcionamiento

El archivo `app.py` define la aplicacion Flask, carga los datos desde `data.json`, registra las rutas y renderiza las vistas correspondientes.

Las plantillas del sitio se encuentran en `templates/` y comparten una estructura base comun. Los recursos estaticos, como hojas de estilo e imagenes, se almacenan en `static/`.

## Secciones del sitio

El sitio incluye las siguientes secciones principales:

- **Home**
- **People**
- **Research**
- **Seminars**
- **Opportunities**

## Gestion del contenido

Parte del contenido se mantiene en `data.json`, lo que permite actualizar informacion del sitio sin modificar directamente la logica principal de la aplicacion.

Entre los datos gestionados se incluyen:

- informacion general del grupo
- noticias recientes
- personas
- temas de investigacion
- seminarios

## Despliegue

El proyecto incluye un archivo `vercel.json`, por lo que esta preparado para desplegarse en **Vercel** con soporte para aplicaciones Python.

## Ejecucion local

Instalacion de dependencias:

```bash
pip install -r requirements.txt
```

Ejecucion del servidor:

```bash
python app.py
```

Acceso local:

```text
http://127.0.0.1:5000
```

## Notas

Este README evita incluir informacion personal, credenciales o datos sensibles. Si el proyecto va a publicarse de forma abierta, conviene revisar periodicamente el contenido de `data.json`, las imagenes y cualquier configuracion de despliegue para asegurar que no se exponga informacion que no deba ser publica.
