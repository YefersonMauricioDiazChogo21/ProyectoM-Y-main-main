import json
import modulos.corefiles as core
import modulos.validaciones as val


dictCampus={}
ruta="data/Inventario.json"


def AddActivos():
    llave="activos"
    titulo=[['|                   AGREGAR ACTIVO                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())

    print('Ingrese el codigo de transaccion')
    CodTransaccion=val.ValidarIngreso()
    print('Ingrese el numero de formulario')
    NroFormulario=val.ValidarIngreso()
    print('Ingrese el nombre')
    nombre=val.ValidarIngreso2()
    print('Ingrese el codigo de campus')
    CodCampus=val.ValidarKeyReverse(dictCampus,llave)
    #VERIFICAR SI NO EXISTE
    print('Ingrese la marca')
    Marca=val.ValidarIngreso2()
    print('Categorias:\n1.Equipo de Computo\n2.Electrodomestico\n3.Juego')
    Categoria=val.ValidarCAT()
    print('TIPO:')
    Tipo=val.ValidarIngreso3(Categoria)
    print('Ingrese el valor unitario')
    ValorUnitario=val.ValidarFLOAT()
    print('Ingrese el proveedor')
    Proveedor=val.ValidarIngreso2()
    print('Ingrese el numero de serial')
    NroSerial=val.ValidarIngreso()
    print('Ingrese la empresa responsable')
    EmpresaResponsable=val.ValidarIngreso2()

    Activo={
        'CodTransaccion':CodTransaccion,
        'NroFormulario':NroFormulario,
        'nombre':nombre, 
        'CodCampus':CodCampus, #no
        'Marca':Marca,
        'Categoria':Categoria,
        'Tipo':Tipo,
        'ValorUnitario':ValorUnitario, 
        'Proveedor':Proveedor,
        'NroSerial':NroSerial, #no
        'EmpresaResponsable':EmpresaResponsable,
        'Estado':0, # no cambiar
        'Ubicacion':"",
        'HistorialActivo':{  #no
            'NroId':[],
            'Fecha':[],
            'tipoMov':[],
            'idRespMov':[]
            }
    }
    dictCampus['activos'].update({CodCampus:Activo})
    core.updatefile(ruta,dictCampus)



def SearchAactivo():
    llave='activos'
    titulo=[['|                   BUSCAR ACTIVO                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    print('Ingrese el codigo del activo a buscar')
    CodCampus=val.ValidarKey(dictCampus,llave)
    Activo=dictCampus['activos'][str(CodCampus)]
    ListActivo=[[Activo["CodCampus"],Activo["nombre"],Activo["Estado"]]]
    print(val.tabulate(ListActivo,headers=["CODIGO","NOMBRE","ESTADO",]))
    x=str(input('Digite cualquier letra para continuar'))


def EditActivo():
    llave='activos'
    titulo=[['|                   EDITAR ACTIVO                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    print('Ingrese el codigo del activo a editar')
    CodCampus=val.ValidarKey(dictCampus,llave)
    ActivoAEditar=dictCampus['activos'][str(CodCampus)]
    if (len(ActivoAEditar))<0:
        print('No existen elementos en este diccionario')
        x=str(input('Digite cualquier letra para continuar'))
    else:
        for key in (ActivoAEditar):
            if key=='CodCampus' or key=='NroSerial' or key=='Estado' or key=='HistorialActivo':
                pass
            elif key=='Tipo':
                if bool(input(f'Desea editar el valor de {key}, s(SI), enter(NO)')):
                    Categoria=dictCampus['activos'][CodCampus]['Categoria']
                    Tipo=val.ValidarIngreso3(Categoria)
                    dictCampus['activos'][CodCampus]['Tipo']=Tipo
            elif key=="Categoria":
                if bool(input(f'Desea editar el valor de {key}, s(SI), enter(NO)')):
                    Categoria=val.ValidarCAT()
                    dictCampus['activos'][CodCampus]['TCategoria']=Categoria
            else:
                if bool(input(f'Desea editar el valor de {key}, s(SI), enter(NO)')):
                    valor=input(f'Ingrese el nuevo valor para {key}\n')
                    ActivoAEditar[key]=valor
                else: 
                    pass  
    dictCampus['activos'][str(CodCampus)]=ActivoAEditar
    with open(ruta,"w+")as editar:
        editar.write(json.dumps(dictCampus,indent=(4)))


def DeleteActivo():
    llave='activos'
    titulo=[['|                   ELIMINAR ACTIVO                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    with open(ruta,"r")as read:
        dictCampus=json.loads(read.read())
    print('Ingrese el codigo del activo a eliminar')
    CodCampus=val.ValidarKey(dictCampus,llave)
    if dictCampus['activos'][CodCampus]['Estado']==0:
        dictCampus['activos'].pop(str(CodCampus))
        print(f'El activo identificado como {CodCampus} ha sido eliminado')
        with open(ruta,"w+") as delete:
            delete.write(json.dumps(dictCampus,indent=(4)))
    else:
        print('El activo esta asignado, no es posible eliminarlo')
    x=print('Digite una tecla para salir\n')

