#!/usr/bin/python3


from os import pipe
#hola


def imprimirMenu():
    print()
    print("ABM de CLIENTES")
    print("________________________")
    print()
    print("Opciones disponibles:")
    print()
    print("1. Nuevo cliente")
    print("2. Modificar cliente")
    print("3. Eliminar cliente")
    print("0. Salir")
    print("________________________")
    print()

clientes = []

def agregar():
    nombre = str(input("Ingrese nombre y apellido: "))
    clientes.append(nombre)
    print()
    print("Agregado con exito! ")
    print()
    print("Asi está la lista ahora")
    print(clientes)
    print("________________________")

def eliminar():
    nombre = str(input("Ingrese el nombre y apellido a eliminar: "))
    print()
    posicion=0
    eliminado=0
  
    while posicion < len(clientes):
        if clientes[posicion] == nombre:
            clientes.pop(posicion)
            eliminado=1
            break
        else:
            posicion=posicion+1
    if eliminado == 1:
        print("Eliminado con exito! ")
    else:
        print("No se ha encontrado coincidencias.")
        print("Verifique lo ingresado e intente de nuevo. ")    

    print()
    print("Asi está la lista ahora: ") #vale para pocos elementos
    print(clientes)
    print()
    

###########################

def menu():
    imprimirMenu()
    while True:
        try:
            entrada_usuario = int(input("Seleccione una opcion: "))
            
            if entrada_usuario in range(5):

                if entrada_usuario == 0:
                    print("Salió del menú.")
                    break
                print()
               
                if entrada_usuario == 1:
                    print("< Alta de Cliente >")
                    print()
                    agregar()
                    #print("Usted eligió la opcion {} !\n".format(entrada_usuario))
                
                if entrada_usuario == 3:
                    print("< Baja de Cliente >")
                    print()
                    eliminar()                  
            else:
                print('Ingresó una opción incorrecta. Intente de nuevo.')
            
            print()
            print("1. Nuevo cliente")
            print("2. Modificar cliente")
            print("3. Eliminar cliente")
            print("0. Salir")
            print()

        except ValueError:
            print("Error, ingrese solamente numeros")


if __name__ == '__main__':
    menu()
