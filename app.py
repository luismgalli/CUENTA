from Clase import Cuenta



def print_cuenta():
    cuentica.cuenta_clase()
    pass

def withdraw_cuenta():
    cuentica.retiro_clase(retiro)
    pass

def deposit_cuenta():
    cuentica.deposito_clase(deposito)
    pass


print("\nHola, este es el menu del banco.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: Para agregar un usuario.
- Type 2: Para agregar fondos a la cuenta.
- Type 3: Para retirar fondos de la cuenta.
- Type 4: Para consultar el saldo de la cuenta.
- Type 6: Para salir del menu.
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        print('Coloque su nombre')
        nombre = input()
        #cuentica.cuenta_clase(nombre)
        #add(nombre)    
        print('Desea ingresar fondos a la cuenta? s=SI , n =N0')
        respuesta = input()
        if respuesta == 's':
            print('Coloque el monto')
            fondos = int(input())
        else:
            fondos = 0
        cuentica = Cuenta(name=nombre, money=fondos)
    elif option ==2:
        print('Cuanto dinero desea depositar')
        deposito = int(input())
        deposit_cuenta()
        pass
    elif option ==3:
        print('Cuanto dinero desea retirar: ')
        retiro = int(input())
        withdraw_cuenta()
        pass
    elif option == 4:
        print_cuenta()
    elif option ==5:
        pass
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))