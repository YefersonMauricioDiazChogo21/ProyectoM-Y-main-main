import modulos.validaciones as val
import modulos.corefiles as core
import json

ruta="data/Inventario.json"

def Retorno():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())

    print('Ingrese el Codigo del activo')
    cod=val.ValidarKey(dictCampus,llave)
    if dictCampus['activos'][cod]['Estado']==3:
        print('Ingrese el ID del personal que hara el retorno\n')
        codigo=val.ValidarKeyAsig(dictCampus,"personal")
        fecha=str(input('Ingrese la fecha\n'))
        dictCampus['activos'][cod]['Estado']=0
        print(f'El activo {cod} ha sido retornado, listo para ser asignado')
        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(codigo)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Retorno")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(codigo)
        dictCampus['asignaciones'][codigo]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][codigo]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(codigo))
        else:
            pass
        core.updatefile(ruta,dictCampus)
    else:
        print(f'El activo {cod} no se encuentra en garantia o reparacion, no es posible retornarlo')
    x=input('Digite una tecla para continuar')

def DarBaja():
    llave='activos'
    with open (ruta,"r") as read:
        dictCampus=json.loads(read.read())
    
    print('Ingrese el codigo del activo')
    cod=val.ValidarKey(dictCampus,llave)
    if dictCampus['activos'][cod]['Estado']==3:
        fecha=input('Ingrese la fecha\n')
        print('Ingrese el id del personal que dara de baja al activo')
        id=val.ValidarKeyAsig(dictCampus,"personal")

        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(id)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Dado de baja")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(id)
        dictCampus['activos'][cod]['Estado']=2
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        core.updatefile(ruta,dictCampus)

    else:
        print('No es posible dar de baja este Activo, unicamente a los activos que esten en garantia o reparacion')
    x=(input('Digite una tecla para continuar'))


def Garantia():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    
    print('Ingrese el codigo del activo')
    cod=val.ValidarKey(dictCampus,llave)

    if dictCampus['activos'][cod]['Estado']==1:
        fecha=input('Ingrese la fecha\n')
        print('Ingrese el id del personal que dara de baja al activo')
        id=val.ValidarKeyAsig(dictCampus,"personal")

        dictCampus['activos'][cod]['HistorialActivo']['NroId'].append(id)
        dictCampus['activos'][cod]['HistorialActivo']['Fecha'].append(fecha)
        dictCampus['activos'][cod]['HistorialActivo']['tipoMov'].append("Garantia o reparacion")
        dictCampus['activos'][cod]['HistorialActivo']['idRespMov'].append(id)
        dictCampus['activos'][cod]['Estado']=3
        dictCampus['asignaciones'][id]['Activos'].remove(str(cod))
        if len(dictCampus['asignaciones'][id]['Activos'])==0:
            dictCampus['asignaciones'].pop(str(id))
        else:
            pass
        core.updatefile(ruta,dictCampus)

    else:
        print('No es posible enviar a garantia este activo, unicamente a los activos que esten asigandos')
    x=(input('Digite una tecla para continuar'))


def Cambiar():
    llave='activos'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())

    print('Ingrese el codigo del activo')
    CodActivo=val.ValidarKey(dictCampus,llave)
    Tipo="zonas"
    if dictCampus['activos'][CodActivo]['Estado']==1:
        Fecha=(input('Ingrese la fecha\n'))
        print('Ingrese el codigo de la zona')
        codigoExiste=val.ValidarKeyExist(dictCampus,"zonas")
        codigoAsig=val.ValidarKeyAsig(dictCampus,codigoExiste)

        tipoAct=dictCampus["activos"][CodActivo]["Tipo"]
        if len(dictCampus["activos"][CodActivo]["Tipo"][tipoAct])== int(dictCampus["zonas"]["totalCapacidad"]):
            print("Capacidad maxima alcanzada para este tipo de activo")
        else:
            if codigoExiste:
                dictCampus['asignaciones'][codigoAsig]['FechaAsignacion'].append(Fecha)
                dictCampus['asignaciones'][codigoAsig]["Activos"][tipoAct].append(CodActivo)
            else:
                Asignacion={
                        'FechaAsignacion':[Fecha],
                        'TipoAsignacion':Tipo,
                        'Cod':codigoAsig,
                        'Activos':{
                            "CPU":[],
                            "MONITOR":[],
                            "MOUSE":[],
                            "TECLADO":[],
                            "ELECTRODOMESTICO":[],
                            "JUEGO":[]
                        }
                    }
                dictCampus['asignaciones'].update({codigoAsig:Asignacion})
                dictCampus['asignaciones'][codigoAsig]["Activos"][tipoAct].append(CodActivo)

                dictCampus['activos'][CodActivo]['HistorialActivo']['NroId'].append(codigoAsig)
                dictCampus['activos'][CodActivo]['HistorialActivo']['Fecha'].append(Fecha)
                dictCampus['activos'][CodActivo]['HistorialActivo']['tipoMov'].append("Re-asignacion")
                dictCampus['activos'][CodActivo]['HistorialActivo']['idRespMov'].append(codigoAsig)
                dictCampus['activos'][CodActivo]['Estado']=1
                with open(ruta,"w+")as editar:
                    editar.write(json.dumps(dictCampus,indent=(4)))
        
        core.updatefile(ruta,dictCampus)
    else:
        print('No es posible enviar a garantia este activo, unicamente a los activos que esten asigandos')
    x=(input('Digite una tecla para continuar'))