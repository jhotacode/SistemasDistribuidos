# SistemasDistribuidos
Taller RPC básicas
En grupos de 2 estudiantes resolver los siguientes problemas:
1. Se debe construir un programa cliente que liste el siguiente menú:
*************Menú Matemático******************************
a. Sumar.
b. Restar
c. Multiplicar.
d. Dividir
e. Potencia
f. Fibonacci
Escoja su opción:
Dichas funciones deben estar implementadas en el servidor, deben ser invocadas mediante
una RPC según la escogencia en el menú al lado del cliente.
2. Se requiere un programa cliente que lea una lista de 15 posiciones por teclado con
números enteros, dicha lista debe ser guardada en un archivo de texto.
Se debe implementar un programa servidor con las siguientes funciones:
 Invertir_lista: debe recibir como argumento un archivo de texto con una lista
numérica, debe retornar un archivo con la lista invertida
 Repetido_lista: debe recibir como argumento un archivo de texto con una
lista numérica, debe retornar el número que más se repite en dicha lista.
El cliente debe invocar las funciones del servidor en un menú mediante RPC.
3. Se requiere que cuando un cliente sea ejecutado, se le presente la siguiente petición:
Usuario:xxxxxxx
clave: ********
En el programa servidor debe existir un mecanismo de verificación:
Datos_Usuario=(‘falcao’, ‘rayo2024’)
Se debe construir una función de verificación con los datos enviados desde el
cliente
El cliente debe enviar los datos leídos al servidor por medio de una RPC, si dichos
datos coinciden se le permite ejecutar el punto 2, si no coinciden se le debe informar
al cliente con un mensaje que los datos son erróneos.
Nota: para las funciones del servidor, evitar en lo posible usar funciones existentes
en Python.