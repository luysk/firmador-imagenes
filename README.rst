Firma Fotografía
================

Herramienta Python para aplicar una firma (marca de agua) sobre imágenes JPG.

Descripción
-----------

Este proyecto permite firmar imágenes JPG ubicadas en un directorio determinado
utilizando una imagen PNG como firma. Si no se suministra un archivo de firma,
se usa la firma por defecto localizada en `util-files/sign.png`.

Características
---------------

- Firma imágenes JPG en lote.
- Posiciones soportadas: `top-left`, `top-right`, `bottom-left`, `bottom-right`.
- Genera resultados en un directorio `signed-images/` dentro del directorio fuente.
- Soporta especificar calidad de salida (1-100).
- Documentación generada con Sphinx.

Requisitos
----------

- Python 3.8+
- Pillow

Instalación
-----------

.. code-block:: bash

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pip install -r docs/requirements.txt

Uso
---

Ejecuta el script principal y responde las preguntas en pantalla:

.. code-block:: bash

    python main.py

También puedes pasar la ruta del directorio y la firma como argumentos:

.. code-block:: bash

    python main.py "C:\Fotos" "C:\util-files\sign.png"

Generar documentación
---------------------

Desde el directorio raíz del proyecto:

.. code-block:: bash

    cd docs
    make html

La documentación generada quedará en `docs/build/html/`.

Estructura de archivos
----------------------

- `main.py` — entrada principal del programa.
- `sign.py` — lógica de aplicación de firma a imágenes.
- `utils.py` — utilidades de validación y rutas.
- `util-files/` — activos del proyecto, incluyendo la firma por defecto.
- `docs/` — configuración y archivos de documentación Sphinx.

Licencia
--------

Proyecto sin licencia especificada.
