# -*- coding: utf-8 -*-
"""
clase sistemas distribuidos

@author: Estudiante UTP
"""
#Primeramente se realiza la conexión con el servidor
from xmlrpc.server import SimpleXMLRPCServer
import os
from collections import Counter
class funcionesrpc():
    def convertir_lista(self,lista15):
        try:
            with open('datos.txt','w') as file:
                for num in lista15:
                    file.write(str(num)+'\n')
        except:
            pass
    def invertir_lista(self,archivo1,archivo2):
        try:
            #Debemos comprobar que el archivo primero exista
            if not os.path.exists(archivo1):
                return False
            #De lo contrario se ejecutará
            else:
                with open(archivo1,'r') as file:
                    numeros = file.readlines()
                #Invertimos la lista de números                
                numeros_invertidos = numeros[::-1]
                #Ahora guardamos la nueva lista en otro archivo
                with open(archivo2,'w') as file:
                    file.writelines(numeros_invertidos)
                #Manipulamos nuevamente para mostrar su contenido
                with open(archivo2,'r') as file:
                    contenido = file.read()
            return contenido
        except Exception as e:
            pass    
    
    def mas_repetido(self,archivo):
        with open(archivo,'r') as file:
            numeros = [int(linea.strip()) for linea in file.readlines()]
        contador = Counter(numeros)
        repetido = max(contador,key=contador.get)
        return repetido
    
server = SimpleXMLRPCServer(("localhost", 8001),allow_none=True)
server.register_instance(funcionesrpc())
print("Servidor funcionando en el puerto 8001")
server.serve_forever()
