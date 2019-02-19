import json
import os
import csv

data = {}
data['nombre'] = 'Jose'
data['edad'] = '15'
data['nacionalidad'] = 'Mex'

archivo = {}
for i in range (1,15):
    archivo[i] = data


dir = 'C:/Users/User/Thalía/Espol/2018-2S/Minería/noticiasVenezuela/pruebas'
file_name = "data.json"

with open(os.path.join(dir, file_name), 'w') as file:
    json.dump(archivo, file)

articulos = open("data.json","r")
articulos_csv = open("noticias.csv","w")


escritor = csv.writer(articulos_csv)

for row in json.loads(articulos.read()):
    escritor.writerow(row)