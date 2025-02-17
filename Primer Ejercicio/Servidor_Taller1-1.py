# -*- coding: utf-8 -*-
"""
clase sistemas distribuidos

@author: Estudiante UTP
"""

from xmlrpc.server import SimpleXMLRPCServer
class funciones:
    def Sumar(self, a, b):
        return a+b
    def Restar(self, a, b):
        return a-b
    def Multiplicar(self, a, b):
        return a*b
    def Dividir(self, a, b):
        return a/b
    def Potencia(self, a, b):
        return a**b
    def Fibonacci(self, n):
        a, b = 0,1
        for i in range(n):
            a, b = b, a+b
        return a
    
server = SimpleXMLRPCServer(('localhost', 9000))
server.register_instance(funciones())
print('Servidor corriendo en el puerto 9000')
server.serve_forever()

