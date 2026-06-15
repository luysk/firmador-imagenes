"""
Funciones para aplicar una firma sobre imágenes JPG.

Este módulo busca la firma por defecto, verifica su existencia y aplica
la firma en una posición definida por el usuario.
"""
import os
import glob
from utils import get_base_dir

from PIL import Image, ImageOps


def get_signature_path(path):
    """
    Devuelve la ruta válida al archivo de firma.

    Si `path` está vacío, utiliza la firma por defecto en `util-files/sign.png`.
    Si la ruta no existe, retorna `False`.
    """
    if not path:
        path = os.path.join(
            get_base_dir(),
            "util-files",
            "sign.png"
        )

    if not os.path.exists(path):
        return False

    return path

def sign_photo_files(dir, signature_path, position, quality):
    """
    Firma todas las imágenes JPG en un directorio.

    Parámetros:
    - dir: directorio que contiene las imágenes JPG a firmar.
    - signature_path: ruta del archivo de firma PNG.
    - position: posición de la firma en la imagen.
    - quality: calidad de salida de la imagen firmada (1-100).
    """

    search_documents_path = os.path.join(
        dir,
        "*.JPG"
    )

    destination_folder = os.path.join(
        dir,
        'signed-images'
    )

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    signature_image = Image.open(signature_path)

    images_paths = glob.glob(search_documents_path)

    for image_to_sign_path in images_paths:

        image = Image.open(image_to_sign_path)
        image = ImageOps.exif_transpose(image)

        img_name = image_to_sign_path.replace(dir, "")[1:]

        img_destination = os.path.join(
            destination_folder,
            img_name
        )

        coordiantes = get_coordinates_by_position(image, position)

        image.paste(signature_image, coordiantes, signature_image)
        image.save(
            img_destination, 
            optimize = True,                 
            quality=quality
        )

        image.close()

def get_coordinates_by_position(image, position):
    """
    Calcula las coordenadas de la firma según la posición seleccionada.

    Devuelve una tupla `(x, y)` con la coordenada superior izquierda donde se
    pegará la imagen de la firma.
    """
    coordinates = ( image.size[0] - 498, image.size[1] - 150)  # bottom-right
    if position == "top-left":
        coordinates = ( 25, 25)
    if position == "top-right":
        coordinates = ( image.size[0] - 498, 25)
    if position == "bottom-left":
        coordinates = ( 25, image.size[1] - 150)

    return coordinates
    
