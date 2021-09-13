#!/usr/bin/python3
from io import open
from os import pipe
import os


def imprimirMenu():
    print()
    print("1. Nuevo cliente")
    print("2. Modificar cliente")
    print("3. Eliminar cliente")
    print("4. Mostrar archivo")
    print("0. Salir")
    print("________________________")
    print()


def agregar ():                                           #"r+"> leer y escribir(actualizar)
    datos = open("clientes.txt", "a", encoding="utf-8")  #"a">salto de linea / "w"> sin salto de linea
    nombre = str(input("Ingrese nombre completo: "))
    codigo = int(input("Ingrese numero de codigo: ")) #mejorar a funcion aleatoria
    datos.write(nombre + "\n")
   # datos.write(codigo)
    datos.close()
    print("Añadido con exito")
    

def mostrarArchivo():
    datos = open("clientes.txt", "r", encoding="utf-8")
    print(datos.read())
    datos.close()


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
                    print("---ALTA CLIENTE---")
                    print()
                    agregar()
                    #print("Usted eligió la opcion {} !\n".format(entrada_usuario))
                
                if entrada_usuario == 2:
                    print("---MODIFICAR CLIENTE---")
                    print()
                    modificar()

                if entrada_usuario == 3:
                    print("---BAJA CLIENTE---")
                    eliminar()             

                if entrada_usuario == 4:
                    print("---ARCHIVO---")         
                    print()
                    mostrarArchivo()
            else:
                print('Ingresó una opción incorrecta. Intente de nuevo.')
            
            print()
            print("1. Nuevo cliente")
            print("2. Modificar cliente")
            print("3. Eliminar cliente")
            print("4. Mostrar archivo")
            print("0. Salir")
            print()

        except ValueError:
            print("Error, ingrese solamente numeros")
    

if __name__ == '__main__':
    file = "/home/camila/Git/Repositorio/BDI/Trabajo_Practico_1/clientes.txt"
    if not os.path.isfile(file) :
        datos = open("clientes.txt","w") 
        datos.write( "Nombre                    "+" Nro Cliente.\n") 
        datos.close() 

    menu()
    