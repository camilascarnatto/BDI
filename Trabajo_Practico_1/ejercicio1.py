#!/usr/bin/python3
from io import open
import os


global posicion
posicion = 0

def imprimirMenu():
    print()
    print("1. Nuevo cliente")
    print("2. Modificar cliente")
    print("3. Eliminar cliente")
    print("4. Mostrar archivo")
    print("0. Salir")
    print("________________________")
    print()

def incrementarPosicion():
    global posicion
    posicion = posicion+1
    
def agregar (): 
    global posicion                                          #"r+"> leer y escribir(actualizar)
    datos = open("clientes.txt", "a", encoding="utf-8")  #"a">salto de linea / "w"> sin salto de linea
    nombre = str(input("Ingrese nombre completo: "))
    codigo = int(input("Ingrese numero de codigo: "))
    datos.write( str(posicion) + "     " + nombre + "          " + str(codigo)+"\n")
    datos.close()
    incrementarPosicion()
    print("Añadido con exito")
    

def mostrarArchivo():
    datos = open("clientes.txt", "r", encoding="utf-8")
    print(datos.read())
    datos.close()

def modificar() :
    mostrarArchivo()

    pos = int(input("Ingrese la posicion que desea modificar: "))
    nombre = str(input("Ingrese nombre: "))
    codigo = int(input("Ingrese codigo: "))
  
    datos = open("clientes.txt", "r+", encoding="utf-8")
  
    nuevaLinea = (str(pos) + "    " + nombre + "        " + str(codigo))
    
   # datos.seek(0,0)
    datos.seek(1,pos)
    datos.writelines(" ")
    datos.writelines(nuevaLinea)
    datos.close()

    print("Registro modificado!")
    print()
    mostrarArchivo()
 


    
    

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
    