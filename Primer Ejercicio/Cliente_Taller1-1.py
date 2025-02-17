import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:9000')
while True:
    eleccion = int(input('1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia\n6. Fibonacci\n7.Salir\n>>'))
    if eleccion == 1:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))
        print('El resultado de la suma es:', s.Sumar(num1, num2))
    elif eleccion == 2:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))
        print('El resultado de la resta es:', s.Restar(num1, num2))
    elif eleccion == 3:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))
        print('El resultado de la multiplicación es:', s.Multiplicar(num1, num2))
    elif eleccion == 4:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))
        print('El resultado de la división es:', s.Dividir(num1, num2))
    elif eleccion == 5:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))
        print('El resultado de la potencia es:', s.Potencia(num1, num2))
    elif eleccion == 6:
        num1 = int(input('Ingrese el primer número: '))
        print('El resultado de la serie de Fibonacci es:', s.Fibonacci(num1))
    elif eleccion == 7:
        break
    else:
        print('Opción no válida')


