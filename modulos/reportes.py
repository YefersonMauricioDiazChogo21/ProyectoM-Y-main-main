import json
import modulos.validaciones as val

dictCampus={}
ruta="data/Inventario.json"

def ListAllActivos():
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listaActivos=[]
    cont=0
    for i in dictCampus['activos']:
        cont+=1
        activo=[i,dictCampus['activos'][i]["nombre"],dictCampus['activos'][i]["Marca"],dictCampus['activos'][i]["Tipo"],dictCampus['activos'][i]["Estado"]]
        listaActivos.append(activo)
        if cont==30:
            cont=0
            print(val.tabulate(listaActivos,tablefmt="rounded_grid"))
            listaActivos=[]
            cierre=bool(input('Desea listar mas activos? s(Si) Enter(No)'))
            if not(cierre):
                break
            else:
                pass
        else:
            pass
    if cont<30 and cont>0:
        pass
        print(val.tabulate(listaActivos,tablefmt="rounded_grid"))
    x=(input('Digite cualquier tecla para salir: \n'))

def ListcatActivos():
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    opciones="""
            1. Equipo de computo
            2. Electrodomestico
            3. Juego
    """
    print(opciones)
    print('Elige la opcion')
    op=val.ValidarINT()
    if op==1:
        categoria="Equipo de computo"
    elif op==2:
        categoria="Electrodomestico"
    elif op==3:
        categoria="Juego"
    else:
        print('opcion no valida')
    listaActivos=[]
    for i in dictCampus['activos']:
        if dictCampus['activos'][i]["Categoria"]==categoria:
            activo=[i,dictCampus['activos'][i]["nombre"],dictCampus['activos'][i]["Marca"],dictCampus['activos'][i]["Tipo"],dictCampus['activos'][i]["Estado"]]
            listaActivos.append(activo)
    
    print(val.tabulate(listaActivos,headers=["CODIGO","NOMBRE","MARCA","TIPO","ESTADO"],tablefmt="rounded_grid"))
    x=(input('Digite cualquier tecla para salir: \n'))
        
def ListaActBaja():
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listaActivos=[]
    for i in dictCampus['activos']:
        if dictCampus['activos'][i]["Estado"]==2:
            activo=[i,dictCampus['activos'][i]["nombre"],dictCampus['activos'][i]["Marca"],dictCampus['activos'][i]["Tipo"],dictCampus['activos'][i]["Estado"]]
            listaActivos.append(activo)
    if (len(listaActivos))==0:
        print('No hay activos dados de baja')
    else: 
        pass
        print(val.tabulate(listaActivos,headers=["CODIGO","NOMBRE","MARCA","TIPO","ESTADO"],tablefmt="rounded_grid"))
    x=(input('Digite cualquier tecla para salir: \n'))
    
    
def listarHistorial():
    val.os.system('clear')
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    print('Ingrese el codigo del activo, para mostrar su historial solicitado')
    codigo=val.ValidarKey(dictCampus,"activos")
    listaHistorial=[]
    historialActivo=dictCampus['activos'][codigo]["HistorialActivo"]
    for i in range(len(historialActivo['NroId'])):
        historial=[0,1,2,3]
        historial[0]=historialActivo['NroId'][i]
        historial[1]=historialActivo['Fecha'][i]
        historial[2]=historialActivo['tipoMov'][i]
        historial[3]=historialActivo['idRespMov'][i]
        listaHistorial.append(historial)
    
    print(val.tabulate(listaHistorial,headers=["ID-MOVIMIENTO","FECHA","TIPO DE MOVIMIENTO","ID-DE-ENCARGADO"],tablefmt="rounded_grid"))
    x=(input('Digite cualquier tecla para salir: \n'))
    
def ListAsAc():
    val.os.system('clear')
    llave='asignaciones'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    for i in dictCampus['asignaciones']:
        print(f'codigo {i}')
    print('Ingrese el codigo')
    cod=val.ValidarKey(dictCampus,llave)
    print(cod)
    listaAsignacionActivos=[]
    print('1.Personal\n2.Zona')
    op=val.ValidarINT()
    if op==1:
        for i in range(len(dictCampus['asignaciones'][cod]['Activos'])):
            lista=[i+1, dictCampus['asignaciones'][cod]['Activos'][i]]
            listaAsignacionActivos.append(lista)
        print(val.tabulate(listaAsignacionActivos, headers=["N°","CODIGO ACTIVO"]))
    elif op==2:
        for i in (dictCampus['asignaciones'][cod]['Activos']):
            listaAsignacionActivos=[]
            for j in range(len(dictCampus['asignaciones'][cod]['Activos'][i])):
                lista=[j+1, dictCampus['asignaciones'][cod]['Activos'][i][j]]
                listaAsignacionActivos.append(lista)
        print(val.tabulate(listaAsignacionActivos, headers=["N°","CODIGO ACTIVO"]))
    else:
        print('Opcion no valida')
    x=(input('Digite una tecla para continuar'))

    