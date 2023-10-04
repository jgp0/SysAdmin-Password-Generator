import random
import string
import pyperclip  # Para copiar al portapapeles

def generar_contrasena(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_caracteres_especiales=True):
    caracteres = string.ascii_letters  # Caracteres por defecto: letras minúsculas
    if usar_mayusculas:
        caracteres += string.ascii_uppercase  # Agregar letras mayúsculas
    if usar_numeros:
        caracteres += string.digits  # Agregar números
    if usar_caracteres_especiales:
        caracteres += string.punctuation  # Agregar caracteres especiales

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == '__main__':
    print("Generador de Contraseñas Seguras")
    longitud = int(input("Longitud de la contraseña: "))
    usar_mayusculas = input("¿Usar letras mayúsculas? (Sí/No): ").strip().lower() == 'si'
    usar_numeros = input("¿Usar números? (Sí/No): ").strip().lower() == 'si'
    usar_caracteres_especiales = input("¿Usar caracteres especiales? (Sí/No): ").strip().lower() == 'si'

    contrasena_generada = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_caracteres_especiales)
    print("Contraseña generada:", contrasena_generada)

    # Opcionalmente, copiar al portapapeles
    copiar = input("¿Copiar al portapapeles? (Sí/No): ").strip().lower() == 'si'
    if copiar:
        pyperclip.copy(contrasena_generada)
        print("Contraseña copiada al portapapeles.")