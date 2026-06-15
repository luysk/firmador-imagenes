Introducción
===========

`Firma Fotografía` es una herramienta Python para aplicar una firma o marca de agua
sobre imágenes JPG. El proyecto utiliza una firma por defecto y genera las
imágenes firmadas en un directorio de salida.

Características
---------------

- Firma imágenes JPG en un directorio.
- Usa un archivo de firma PNG.
- Soporta las posiciones: `top-left`, `top-right`, `bottom-left` y `bottom-right`.
- Guarda el resultado en `signed-images/`.

Instalación
-----------

Se recomienda usar un entorno virtual.

.. code-block:: bash

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pip install -r docs/requirements.txt

Estructura relevante
--------------------

- `main.py` - entrada principal del programa.
- `sign.py` - lógica de firma de imágenes.
- `utils.py` - funciones auxiliares y validaciones.
- `util-files/sign.png` - firma por defecto usada si no se provee otra.
