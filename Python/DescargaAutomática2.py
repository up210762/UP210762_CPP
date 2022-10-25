import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

def url_response(url):
    path, url = url
    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:
    
        for ch in r:
            f.write(ch)

urls = []
cantidad = int(input("¿Cuántos archivos son? "))
Decision = str(input("¿Es un solo tipo de archivo? "))
if Decision == "Si" or "si" or "si" or "sI":
    TipoArchivo = str(input("Escribe el tipo de archivo: "))
    for i in range(cantidad):
        link = str(input("Escribe el link del archivo: "))
        url = (f"Evento{i}.{TipoArchivo}", link)
        urls.append(url)

elif Decision == "No" or "No" or "no" or "nO":
    for i in range(cantidad):
        TipoArchivo = str(input("Escribe el tipo de archivo: "))
        link = str(input("Escribe el link del archivo: "))
        url = (f"Evento{i}.{TipoArchivo}", link)
        urls.append(url)

#https://drive.google.com/file/d/1AkC4kFoF3zUGJoqP7qtXEwogTnfwvhzd/view?usp=sharing

start = time()
for x in urls:
    url_response (x)
print(f"Time to download: {time() - start}")

ThreadPool(9).imap_unordered(url_response, urls)