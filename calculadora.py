num1 = int(input("Ingrese numero 1: ")) 
num2 = int(input("Ingrese numero 2: ")) 
num3 = int(input("numero 3: "))

valor = 0
while True:
    print("""Seleccione una opción
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir 
            5- sumar 3 valores
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("La suma es",num1+num2)
        break;
    if valor == 2:
        print("La resta es",num1-num2)
        break;
    if valor == 3:
        print("La multiplicacion es",num1*num2)
        break;
    if valor == 4:
        print("La division es",num1/num2)
        break;
    if valor == 5:
        print("la suma es",num1+num2+num3)
        break;
    else:
        print("Opcion incorrecta")
        break;