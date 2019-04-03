import json, os

from controllers.input import input_verifier as iv


print('------------------------------')
print('| Formulario de contratacion |')
print('|        para la clase       |')
print('|   De Anita la huerfanita   |')
print('|       CTR+C para salir     |')
print('------------------------------')
print()
print('Introduce tus datos')

vector_usuario = {}
Nombre = iv.check_if_string(iv,'Nombre')

print()
print('Introduce los Lenguajes que sabes')
print('Para terminar Introduce fin')
lenguajes = iv.array_string(iv,'Lenguajes')

print()
print('Introduce los Tecnologias que sabes')
print('Para terminar Introduce fin')
Tecnologias = iv.array_string(iv, 'Tecnologias')

score = 0
