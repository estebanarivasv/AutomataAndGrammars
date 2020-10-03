## ***Automata and grammars***

In this repository, my classmate Yoel and me made some exercises regarding automata and grammars subject for UM.

### Trabajo Práctico Nº1
#### Statement:
Utilizando el lenguaje de programación Python, construir para cada una de las siguientes
expresiones, un analizador léxico. El analizador léxico debe recibir como entrada una cadena y
en la salida definir si reconoce como correcta la cadena de entrada.
1. Email (nombre@dominio)
2. URL (http-https://www…..)
3. Dirección IPv4 (000.000.000.000-255.255.255.255)
4. Contraseña segura*
#### *Se considera contraseña segura a una contraseña que cumpla con las siguientes condiciones:
- Que contengan al menos una letra mayúscula.
- Que contengan al menos una letra minúscula.
- Que Contengan al menos un número.
- Longitud mínima de 8 caracteres.

***Ejemplo: analizador léxico en Python que reconoce extensiones para imágenes.***
```
import re
print("Validar extensión de imagen")
ext = input("Ingrese una extensión de una imagen: ")
if re.match('jpg|png|gif|bmp', ext):
 print('La extensión ', ext, 'se corresponde con una imagen')
else:
 print('La extensión ', ext, 'no se corresponde con una imagen')
```
