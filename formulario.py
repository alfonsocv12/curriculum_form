# -*- coding: utf-8 -*-
import json, os, urllib.request, requests
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from controllers.input import input_verifier as iv
host = 'http://localhost:8080'

try:
    from env import os
except:
    print('You havent add a env.py')

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

#Input user known leguages
print()
print('Introduce los Lenguajes que sabes')
print('Para terminar Introduce fin')
print()
lenguages = iv.array_string(iv,'Lenguajes')

#Input user known technologies
print()
print('Introduce los Tecnologias que sabes')
print('Para terminar Introduce fin')
print()
technologies = iv.array_string(iv, 'Tecnologias', True)

#Get score of technologies
score = 0

score_leguages = os.environ.get('lenguages')
for score_leguage in score_leguages:
    for lenguage in lenguages:
        if lenguage == score_leguage:
            score += score_leguages[score_leguage]

score_tegnologies = os.environ.get('technologies')
for score_tegnologie in score_tegnologies:
    for technologie in technologies:
        if score_tegnologie == technologie:
            score += score_tegnologies[score_tegnologie]

print()
if score >= os.environ.get('requerimientos'):
    data = {'status':'true'}
    contents = requests.request(method='GET',url='{}/vacante/{}/status'.format(host, os.environ.get('vacante')), data=data)
else:
    data = {'status':'false'}
    contents = requests.request(method='GET',url='{}/vacante/{}/status'.format(host, os.environ.get('vacante')), data=data)
