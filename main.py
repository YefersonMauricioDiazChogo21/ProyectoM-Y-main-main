
import modulos.corefiles as core
import modulos.menus as menus
import modulos.uploadActivos as um


dictCampus={
    'activos':{},
    'personal':{},
    'zonas':{},
    'asignaciones':{}
}


if __name__=="__main__":
    core.checkFile("Inventario.json",dictCampus)
    um.valUniqueUpdateActivos()
    menus.MenuPrincipal()
