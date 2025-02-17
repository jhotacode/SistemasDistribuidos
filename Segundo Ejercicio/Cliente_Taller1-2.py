import xmlrpc.client

#Realizamos la conexión con la base de datos
server = xmlrpc.client.ServerProxy('http://localhost:8001')

lista = []
for i in range(3):
    numero = int(input(f"Ingrese un número {i+1}: "))
    lista.append(numero)

server.convertir_lista(lista) #Esta linea nos permite convertir la lista en un archivo de texto
while True:
    eleccion = int(input("1. Lista invertida\n2. Número más repetido\n3. Salir\n>>"))
    if eleccion == 1:
        contenido = server.invertir_lista('datos.txt','datos_invertidos.txt')
        print("Lista invertida: \n" + str(contenido))
    elif eleccion == 2:
        num_repetido = server.mas_repetido('datos.txt')
        print(f"El número más repetido es: {num_repetido}")
    elif eleccion == 3:
        break
    else:
        print("Opción no válida")
    

    
    
