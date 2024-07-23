import os
import json
BASE_DATA="data/"

Archivo={}
ruta="data/Inventario.json"

def checkFile(Archivo, dictCampus):
    if(not(os.path.isfile(BASE_DATA+ Archivo))):
        with open(BASE_DATA + Archivo ,"w+") as bw:
            json.dump(dictCampus,bw,indent=4)


def updatefile(archivo,diccionario):
     with open(archivo,"w+") as createdata:
        json.dump(diccionario,createdata,indent=4)