import json
import modulos.corefiles as core
import modulos.validaciones as val



dictCampus={}
ruta="data/Inventario.json"

def AddZona():
    llave="zonas"
    titulo=[['|                   AGREGAR ZONA                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listZonas=[]
    if len(dictCampus["zonas"])>0:
        for i in dictCampus["zonas"]:
            zona=[i,dictCampus["zonas"][i]["NombreZona"]]
            listZonas.append(zona)
        print(val.tabulate(listZonas,tablefmt="heavy_grid"))
    else:
        pass
    # print('ingrese el codigo de la zona')
    # NroZona=val.ValidarKeyReverse(dictCampus,llave)
    NombreZona=str(input('ingrese el nombre de la zona\n'))
    print('ingrese la capacidad de la zona')
    totalCapacidad=val.ValidarIngreso()
    NroZona="Z"+str(len(dictCampus["zonas"])+1).zfill(2)
    Zona={ #todo editar
        'NroZona':NroZona,
        'NombreZona':NombreZona,
        'totalCapacidad':totalCapacidad
        }
    
    dictCampus['zonas'].update({NroZona:Zona})
    core.updatefile(ruta,dictCampus)


def searchZona():
    titulo=[['|                   BUSCAR ZONA                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="zonas"
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    listZonas=[]
    if len(dictCampus["zonas"])>0:
        for i in dictCampus["zonas"]:
            zona=[i,dictCampus["zonas"][i]["NombreZona"]]
            listZonas.append(zona)
        print(val.tabulate(listZonas,tablefmt="heavy_grid"))
    print('Ingrese el identificador')
    NroZona=val.ValidarKey(dictCampus,llave)
    Zona=dictCampus['zonas'][str(NroZona)]
    ListZona=[[Zona["NroZona"],Zona["NombreZona"],Zona["totalCapacidad"]]]
    print(val.tabulate(ListZona,headers=["ID de Zona","Nombre","Total de Capacidad"], tablefmt='rounded_grid'))
    x=str(input('Digite cualquier letra para continuar'))


def editZona():
    titulo=[['|                   EDITAR ZONA                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="zonas"
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    listZonas=[]
    if len(dictCampus["zonas"])>0:
        for i in dictCampus["zonas"]:
            zona=[i,dictCampus["zonas"][i]["NombreZona"]]
            listZonas.append(zona)
        print(val.tabulate(listZonas,tablefmt="heavy_grid"))
    print('Ingrese el identificador')
    NroZona=val.ValidarKey(dictCampus,llave)
    ZonaAEditar=dictCampus['zonas'][str(NroZona)]
    if(len(ZonaAEditar))<0:
        print('No existen elementos en este diccionario')
    else:
        for key in (ZonaAEditar):
            if key!='NroZona':
                if bool(input(f'¿Desea editar el valor de {key}?. s(SI), enter(NO)')):
                    valor=(input(f'Ingrese el nuevo valor para {key}'))
                    ZonaAEditar[key]=valor
                else:
                    pass
            else:
                pass
    dictCampus['zonas'][str(NroZona)]=ZonaAEditar
    with open(ruta,"w+") as editar:
        editar.write(json.dumps(dictCampus, indent=4))
    

def DeleteZona():
    titulo=[['|                   ELIMINAR ZONA                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="zonas"
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    listZonas=[]
    if len(dictCampus["zonas"])>0:
        for i in dictCampus["zonas"]:
            zona=[i,dictCampus["zonas"][i]["NombreZona"]]
            listZonas.append(zona)
        print(val.tabulate(listZonas,tablefmt="heavy_grid"))
    print('Ingrese el identificador')
    NroZona=val.ValidarKey(dictCampus,llave)
    dictCampus['zonas'].pop(str(NroZona))
    print(f'La zona identificada como "{NroZona}" ha sido eliminada')
    
    with open(ruta,"w+") as delete:
        delete.write(json.dumps(dictCampus,indent=4))

    x=str(input('Digite cualquier letra para continuar'))

        
    
