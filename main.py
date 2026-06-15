"""
Entry point del proyecto de firma de fotografías.

Este módulo expone la función `main` que ejecuta el flujo de interacción con el usuario,
valida el directorio origen y aplica la firma a las imágenes JPG.
"""
import sys

from utils import check_source_dir
from sign import get_signature_path, sign_photo_files


def main(args):
    """
    Ejecuta el flujo principal de la aplicación.

    Parámetros:
    - args: lista de argumentos de la línea de comandos.
    """
    source_dir = args[0] if len(args) >= 1 else input("Input the source-dir path: ")
    signature_file = args[1] if len(args) >= 2 else input("Input the signature path or empty to use the default one: ")

    print("""
Select the position of the signature (Default bottom-right): 
    a) top-left
    b) top-right
    c) bottom-left
    d) bottom-right  
    """)
    position_letter = input("Type the letter to select the position: ")
    position = "bottom-right"

    if position_letter == "a":
        position = "top-left"
    if position_letter == "b":
        position = "top-right"
    if position_letter == "c":
        position = "bottom-left"

    check_result = check_source_dir(source_dir)
    if check_result != True:
        sys.exit(check_result)
    
    signature_path = get_signature_path(signature_file)
    if not signature_path:
        sys.exit("The signature path doesn't have a valid image file")
    
    quality = input("Insert the photo quality relative to original pthoto (1-100): ")
    quality = int(quality)

    result = sign_photo_files(source_dir, signature_path, position, quality=quality)
    
    sys.exit(result)

if __name__ == "__main__":
   main(sys.argv[1:])