import os
import json
import modulos.validaciones as val

ruta="data/Inventario.json"

def AddAsignacion():
    
    titulo=[['|                   AGREGAR ASIGNACION               |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave='activos'
    with open(ruta,"r")as read:
        dictCampus=json.loads(read.read())
    os.system('clear')
    if len(dictCampus["zonas"])==0 and len(dictCampus["personal"])==0:
        print('No existen zonas o personas en la base de datos')
    else:
        print('Ingrese codigo del activo a Asignar:')
        CodActivo=val.ValidarKey2(dictCampus,llave)
        Fecha=str(input('Ingrese la fecha de Asignacion\n'))
        print('Tipo:\n1.Personal\n2.Zona')
        Tipo=val.ValidarTIP(dictCampus)
        if Tipo=="zonas":
            estado=1
            TipoMov="Asignado"
            print('El activo entrara en estado de Asignacion')
            print('Ingrese el codigo de la zona a la que se le ha hecho la Asignacion')
        elif Tipo=="personal":
            menu="""
                1.Dar de baja a un activo
                2.Enviar a repacion o a garantia un activo
            """
            print(menu)
            op=val.ValidarINT()
            if op==1:
                estado=2
                TipoMov="Dado de baja"
            elif op==2:
                estado=3
                TipoMov="Garantia o reparacion"
            print('Ingrese el id de a quien se le ha hecho la Asignacion\n')
            
        codigoAsig=val.ValidarKeyAsig(dictCampus,Tipo)
        codigoExiste=val.ValidarKeyExist(dictCampus,codigoAsig)
        
        if Tipo=="personal":
            if codigoExiste:
                dictCampus['asignaciones'][codigoAsig]['FechaAsignacion'].append(Fecha)
                dictCampus['asignaciones'][codigoAsig]['Activos'].append(CodActivo)
            else:
                Asignacion={
                        'FechaAsignacion':[Fecha],
                        'TipoAsignacion':Tipo,
                        'Cod':codigoAsig,
                        'Activos':[CodActivo]
                    }
                dictCampus['asignaciones'].update({codigoAsig:Asignacion})
            dictCampus['activos'][CodActivo]['HistorialActivo']['NroId'].append(codigoAsig)
            dictCampus['activos'][CodActivo]['HistorialActivo']['Fecha'].append(Fecha)
            dictCampus['activos'][CodActivo]['HistorialActivo']['tipoMov'].append(TipoMov)
            dictCampus['activos'][CodActivo]['HistorialActivo']['idRespMov'].append(codigoAsig)
            dictCampus['activos'][CodActivo]['Estado']=estado
            with open(ruta,"w+")as editar:
                editar.write(json.dumps(dictCampus,indent=(4)))
        else:
            tipoAct=dictCampus["activos"][CodActivo]["Tipo"]
            if len(dictCampus["asignaciones"][codigoAsig]["Activos"][tipoAct])== int(dictCampus["zonas"][codigoAsig]["totalCapacidad"]):
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
                    dictCampus['activos'][CodActivo]['HistorialActivo']['tipoMov'].append(TipoMov)
                    dictCampus['activos'][CodActivo]['HistorialActivo']['idRespMov'].append(codigoAsig)
                    dictCampus['activos'][CodActivo]['Estado']=estado
                    with open(ruta,"w+")as editar:
                        editar.write(json.dumps(dictCampus,indent=(4)))
    x=str(input('Digite cualquier letra para continuar'))
        
def searchAsig():
    llave='asignaciones'
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    print('Ingrese el identificador de la asignacion')
    DondeAsig=val.ValidarKey(dictCampus,llave)
    Asignacion=dictCampus[llave][str(DondeAsig)]
    print(Asignacion) 
    x=str(input('Digite cualquier letra para continuar'))

    