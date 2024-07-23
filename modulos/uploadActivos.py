from csv import reader
import modulos.corefiles as core
import json

def addActivosList():
    data=[]

    ruta="data/Inventario.json"
    with open("externaldata/productos_campus.csv","r") as file:
        lector= reader(file)
        for i in lector:
            data.append(i)

    for i in range(len(data)):
        with open(ruta, "r") as read:
            diccionario = json.loads(read.read())
        Activo={
            'CodTransaccion':data[i][1],
            'NroFormulario':data[i][3],
            'nombre':data[i][2],
            'CodCampus':data[i][4],
            'Marca':data[i][5],
            'Categoria':data[i][6],
            'Tipo':data[i][7],
            'ValorUnitario':data[i][8],
            'Proveedor':data[i][9],
            'NroSerial':data[i][10],
            'EmpresaResponsable':data[i][11],
            'Estado':int(data[i][12]),
            'Ubicacion':"",
            'HistorialActivo':{
                'NroId':[],
                'Fecha':[],
                'tipoMov':[],
                'idRespMov':[]
                }
        }
        diccionario['activos'].update({data[i][4]:Activo})
        core.updatefile(ruta,diccionario)
        
def valUniqueUpdateActivos():
    ruta="data/Inventario.json"
    with open(ruta, "r") as read:
        diccionario = json.loads(read.read())
    if len(diccionario['activos'])==0:
         addActivosList()
    else:
         pass


