"""
Utilidades auxiliares del proyecto de firma de fotografías.

Incluye validación del directorio fuente y cálculo del directorio base.
"""
import os
from pathlib import Path

def create_essential_dir_n_files():
    """
    Crea el directorio de firmas si no existe.

    Esta función asegura que la carpeta `signatures` exista dentro del
    directorio base del proyecto.
    """
    signatures_path = os.path.join(
        get_base_dir(),
        'signatures'
    )

    if not os.path.exists(signatures_path):
        os.makedirs(signatures_path)


def check_source_dir(dir):
    """
    Comprueba que un directorio fuente existe y es un directorio.

    Retorna `True` si el directorio es válido, de lo contrario un mensaje de error.
    """
    if not os.path.exists(dir):
        return "The source dir doesn't exists"

    if not os.path.isdir(dir):
        return "The source dir is not a dir"

    return True

def get_base_dir():
    """
    Devuelve el directorio base del proyecto.
    """
    BASE_DIR = Path(__file__).resolve().parent
    return BASE_DIR
