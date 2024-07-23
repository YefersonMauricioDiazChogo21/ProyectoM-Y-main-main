import os
import modulos.corefiles as core
import json
import modulos.validaciones as val

dictCampus={}
ruta="data/Inventario.json"

#guardar aqui= el resultado de esta funcion()

def AddPersonal():
    llave="personal"
    with open(ruta,"r") as read:
        dictCampus=json.loads(read.read())
    titulo=[['|                   AGREGAR PERSONAL                |']]
    listPersonal=[]
    if len(dictCampus["personal"])>0:
        for i in dictCampus["personal"]:
            persona=[i,dictCampus["personal"][i]["nombre"]]
            listPersonal.append(persona)
        print(val.tabulate(listPersonal,tablefmt="heavy_grid"))
    else:
        pass
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    # print('Ingrese el ID del personal')
    # id=val.ValidarKeyReverse(dictCampus,llave)
    nombre=str(input('Ingrese el nombre del personal \n').capitalize())
    email=str(input('Ingrese el email del personal\n'))
    print('Ingrese el tel movil del personal')
    movil=val.ValidarINT()
    print('Ingrese el tel de la casa del personal')
    casa=val.ValidarINT()
    print('Ingrese el tel de oficina del personal')
    oficina=val.ValidarINT()
    print('Ingrese el tel celular del personal')
    personalTel=val.ValidarINT()
    id="P"+str(len(dictCampus["personal"])+1).zfill(2)
    Personal={
        'id':id,
        'nombre':nombre,
        'email':email,
        'movil':movil,
        'casa':casa,
        'oficina':oficina,
        'personalTel':personalTel
    }
    dictCampus['personal'].update({id:Personal})
    with open(ruta,"w") as create:
        json.dump(dictCampus,create, indent=4)
    


def SearchPersonal():
    titulo=[['|                   BUSCAR PERSONAL                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="personal"
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listPersonal=[]
    if len(dictCampus["personal"])>0:
        for i in dictCampus["personal"]:
            persona=[i,dictCampus["personal"][i]["nombre"]]
            listPersonal.append(persona)
        print(val.tabulate(listPersonal,tablefmt="heavy_grid"))
    print('Ingrese el ID del personal')
    Id=val.ValidarKey(dictCampus,llave)
    persona=dictCampus['personal'][str(Id)]
    ListPersonal=[[persona["id"],persona["nombre"],persona["oficina"]]]
    print(val.tabulate(ListPersonal,headers=["ID del personal","nombre","Telefono de oficina"]))
    x=str(input('Digite cualquier letra para continuar'))


def EditPersonal():
    titulo=[['|                   EDITAR PERSONAL                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="personal"
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listPersonal=[]
    if len(dictCampus["personal"])>0:
        for i in dictCampus["personal"]:
            persona=[i,dictCampus["personal"][i]["nombre"]]
            listPersonal.append(persona)
        print(val.tabulate(listPersonal,tablefmt="heavy_grid"))
    print('Ingrese el identificador')
    Id=val.ValidarKey(dictCampus,llave)
    #a la variable personal le estoy asignando el valor que encuentre en =esta ruta
    personalAEditar=dictCampus['personal'][str(Id)]
    if(len(personalAEditar))<0:
        print('No existen elementos en este diccionario')
        x=str(input('Digite cualquier letra para continuar'))
    else:
        #voy a recorrer el personal a editar, le permito editar todo menos el id
        for key in (personalAEditar):
            if key!='Id':
                #puede que entre esas llaves este almacenado un diccionario, entre a ese diccionario por medio del 2 recorrido
                if(type(personalAEditar[key])==dict):
                    #key2 son las llaves dentro del recorrido del subdiccionario
                    for key2 in (personalAEditar[key]):
                        if bool(input(f'¿Desea editar el valor de {key2}? s(SI) enter(NO)\n')):
                            valor=input(f'Ingrese el nuevo valor de {key2}\n')
                            personalAEditar[key][key2]=valor
                else:
                    if bool(input(f'¿Desea editar el valor de {key}? s(SI) enter(NO)\n')):
                        valor=input(f'Ingrese el nuevo valor de {key}\n')
                        personalAEditar[key]=valor
    
    dictCampus['personal'][str(Id)]=personalAEditar
    with open(ruta,"w+") as Editar:
        Editar.write(json.dumps(dictCampus,indent=(4)))
        


def DeletePersonal():
    titulo=[['|                  ELIMINAR PERSONAL                |']]
    print(val.tabulate(titulo,tablefmt='rounded_grid'))
    llave="personal"
    with open(ruta, "r") as read:
        dictCampus = json.loads(read.read())
    listPersonal=[]
    if len(dictCampus["personal"])>0:
        for i in dictCampus["personal"]:
            persona=[i,dictCampus["personal"][i]["nombre"]]
            listPersonal.append(persona)
        print(val.tabulate(listPersonal,tablefmt="heavy_grid"))
    print('Ingrese el identificador')
    Id=val.ValidarKey(dictCampus,llave)
    if Id in dictCampus['asignaciones']:
        print('El personal tiene asigando activos, no es posible eliminarlo')
        x=print('Digite una tecla para continuar\n')
    else:
        dictCampus['personal'].pop(str(Id))
        with open(ruta,"w+") as delete:
            delete.write(json.dumps(dictCampus,indent=4))
        print(f'El personal identificado como "{Id}" ha sido eliminado')
        x=str(input('Digite cualquier letra para continuar'))