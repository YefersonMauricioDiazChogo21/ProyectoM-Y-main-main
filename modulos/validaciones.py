import os
from tabulate import tabulate

def ValidarINT():
    try:
        x=int(input(''))
        return x
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarINT()
    

def ValidarFLOAT():
    try:
        x=float(input(''))
        return x
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarFLOAT()
    
    
def ValidarKey(dictCampus,llave):
    try:
        x=str(input(''))
        dictCampus[llave][x]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(dictCampus,llave)
    

def ValidarKey2(dictCampus,llave):
    try:
        x=str(input(''))
        dictCampus[llave][x]
        if dictCampus[llave][x]['Estado']==2:
            print('Activo dado de baja, no es posible asignarlo')
            return ValidarKey2(dictCampus,llave)
        elif dictCampus[llave][x]['Estado']==3:
            print('Activo en reparacion o garantia, no es posible asignarlo')
            return ValidarKey2(dictCampus,llave)
        elif dictCampus[llave][x]['Estado']==1:
            print('Activo ya asignado, no es posible asignarlo de nuevo')
            return ValidarKey2(dictCampus,llave)
        else:
            return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(dictCampus,llave)
    

def ValidarKeyInt(dictCampus,llave):
    try:
        x=int(input('Ingrese el identificador\n'))
        dictCampus[llave][str(x)]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKeyInt(dictCampus,llave)
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarKeyInt(dictCampus,llave)



def ValidarIngreso():
    try:
        x=int(input(''))
        return x
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarINT()   

def ValidarIngreso2():
    try:
        x=str(input(''))
        return x
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarINT()   

def ValidarIngreso3(cat):
    try:
        x=int(input('Ingrese el tipo:\n1. Cpu\n2. Mouse\n3. Teclado\n4. Monitor\n5. Electrodomestico\n6. Juego\n'))
        if cat=="Equipo de computo":
            
            if x==1:
                tipo="CPU"
            elif x==2:
                tipo="MOUSE"
            elif x==3:
                tipo="TECLADO"
            elif x==4:
                tipo="MONITOR"
            else: 
                print("opcion no valida")
                return ValidarIngreso3(cat)
        else:
            if x==5:
                tipo="ELECTRODOMESTICO"
            elif x==6:
                tipo="JUEGO"
            else:
                print('Opcion no valida')
                return ValidarIngreso3(cat) 
        return tipo      
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarIngreso3(cat)   


def ValidarCAT():
    try:
        x=int(input('Ingrese la opcion\n'))
        if x==1:
            cat="Equipo de computo"
        elif x==2:
            cat="Electrodomestico"
        elif x==3:
            cat="Juego"
        else:
            print('Opcion no valida')
            return ValidarCAT() 
        return cat       
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarCAT()
    
def ValidarTIP(dictCampus):
    try:
        x=int(input('Ingrese una opcion\n'))
        if x==1:
            tipo="personal"
        elif x==2:
            tipo="zonas"
        else:
            print('Opcion no valida')
            return ValidarTIP()
        if len(dictCampus[tipo])==0:
            print(f'No hay {tipo} registrad@s en la base de datos')
            return ValidarTIP(dictCampus)
        return tipo
    except ValueError:
        print('Opcion no valida, vuelvalo a intentar')
        return ValidarTIP(dictCampus)

def ValidarKeyExist(dictCampus,codigoExiste)->bool:
    try:
        dictCampus['asignaciones'][codigoExiste]
        return True
    except KeyError:
        return False
    
def ValidarKeyAsig(dictCampus,llave):
    try:
        x=str(input(' '))
        dictCampus[llave][x]
        return x
    except KeyError:
        print('Elemento no existente')
        return ValidarKey(dictCampus,llave)
    
def ValidarKeyReverse(dictCampus,llave):
    try:
        x=input(' ')
        dictCampus[llave][x]
        print('Ya existe, Intente nuevamente')
        return ValidarKeyReverse(dictCampus,llave)
    except KeyError:
        return x

