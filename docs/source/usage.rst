Uso
===

Modo interactivo
----------------

Ejecuta el script principal y responde las preguntas en pantalla:

.. code-block:: bash

    python main.py

El flujo solicita:

- ruta del directorio fuente con imágenes JPG.
- ruta de la firma o dejar vacía para usar la firma por defecto.
- posición de la firma.
- calidad de salida (1-100).

Modo con argumentos
-------------------

También es posible pasar los parámetros directamente:

.. code-block:: bash

    python main.py "C:\Fotos" "C:\util-files\sign.png"

Salida
------

Las imágenes firmadas se escriben en el directorio `signed-images/`
dentro del directorio fuente.
