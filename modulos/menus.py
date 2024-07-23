import modulos.validaciones as val
import modulos.personal as per
import modulos.activosMod as Act
import modulos.asignacion as asig
import modulos.reportes as rep
import modulos.zonas as zon
import modulos.movimientoAc as mov


Archivo={}
ruta="data/Inventario.json"

def menuActivos():

    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                   MENU DE ACTIVOS                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))

        menu="""
            1.Agregar
            2.Editar
            3.Eliminar
            4.Buscar
            5.Regresar menu anterior
        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            Act.AddActivos()
        elif op==2:
            Act.EditActivo()
        elif op==3:
            Act.DeleteActivo()
        elif op==4:
            Act.SearchAactivo()
        elif op==5:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')


def menuPersonal():
    
    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                   MENU DE PERSONAL                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))
        menu="""
            1.Agregar
            2.Editar
            3.Eliminar
            4.Buscar
            5.Regresar menu anterior
        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            per.AddPersonal()
        elif op==2:
            per.EditPersonal()
        elif op==3:
            per.DeletePersonal()
        elif op==4:
            per.SearchPersonal()
        elif op==5:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')


def menuZonas():

    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                   MENU DE ZONAS                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))
        menu="""
            1.Agregar
            2.Editar
            3.Eliminar
            4.Buscar
            5.Regresar menu anterior
        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            zon.AddZona()
        elif op==2:
            zon.editZona()
        elif op==3:
            zon.DeleteZona()
        elif op==4:
            zon.searchZona()
        elif op==5:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')

def menuAsigActivos():
    
    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                   MENU DE ASIGNACION DE ACTIVOS                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))
        menu="""
            1.Crear asignacion
            2.Buscar asignacion
            3.Regresar menu anterior
        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            asig.AddAsignacion()
        elif op==2:
            asig.searchAsig()
        elif op==3:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')


def menuReportes():
    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                    MENU DE REPORTES                 |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))
        menu="""
            1.Listar todos los activos
            2.Listar los activos por categoria
            3.Listar activos dados de baja por daño
            4.Listar asignacion y sus activos
            5.Listar historial de movimiento del activo
            6.Regresar al menu principal

        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            rep.ListAllActivos()
        elif op==2:
            rep.ListcatActivos()
        elif op==3:
            rep.ListaActBaja()
        elif op==4:
            rep.ListAsAc()
        elif op==5:
            rep.listarHistorial()
        elif op==6:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')


def MenuMovActivos():
    
    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                  MENU DE MOVIMIENTO DE ACTIVOS                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))
        menu="""
            1.Retorno de activos
            2.Dar de baja activo
            3.Enviar a garantia activo
            4.Cambiar asignacion de activo
            5.Regresar al menu principal

        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            mov.Retorno()
        elif op==2:
            mov.DarBaja()
        elif op==3:
            mov.Garantia()
        elif op==4:
            mov.Cambiar()
        elif op==5:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')



def MenuPrincipal():
    
    cierre=True
    while cierre:
        val.os.system('clear')
        titulo=[['|                  SISTEMA G&C DE INVENTARIO CAMPUSLANDS                |']]
        print(val.tabulate(titulo,tablefmt='rounded_grid'))

        menu="""
            1.Activos
            2.Personal
            3.Zonas
            4.Asignacion de activos
            5.Reportes
            6.Movimiento de activos
            7.Salir
        """
        print(menu)
        print('Elige la opcion')
        op=val.ValidarINT()
        if op==1:
            menuActivos()
        elif op==2:
            menuPersonal()
        elif op==3:
            menuZonas()
        elif op==4:
            menuAsigActivos()
        elif op==5:
            menuReportes()
        elif op==6:
            MenuMovActivos()
        elif op==7:
            print('Adios')
            x=(input('Digite cualquier tecla para salir: \n'))
            cierre=False
        else:
            print('Opcion no valida')
            x=(input('Digite cualquier tecla para continuar \n'))


        

        