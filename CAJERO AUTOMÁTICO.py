saldo = 1000

def consultar_saldo(saldo):
    print(f"su saldo actual es: ", saldo)
    
def depositar(saldo):
    monto = float(input("ingrese el monto que quiere depositar: "))
    
    if monto > 0:
        saldo = saldo + monto
        print("deposito realizado. su saldo se a actualizado a: ", saldo)
    
    else:
        print("error, el monto a depositar debe ser mayor que 0")
    
    return saldo

def retirar(saldo):
    monto = float(print("ingrese el monto que quiere retirar: "))
    
    if monto <= 0:
        print("error, el monto el monto a retirar debe ser mayor a 0")
    
    elif monto > saldo:
        print("error, no tienes suficiente saldo. tu saldo acttual es: ", saldo)
    
    else:
        saldo = saldo - monto
        print("retiro realizado, su nuevo saldo actual es de: ", saldo)
    
    return saldo

opcion = -1

while opcion != 0:
    print("\n=====>CAJERO AUTOMATICO<=====")
    print("para realizar cada funcion pon su numero asignado:")
    print("1. consultar saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("0. salir")
    
    
    opcion = int(input("seleccione una opcion: "))
    if opcion == 1:
        consultar_saldo(saldo)
    
    elif opcion == 2:
        saldo = depositar(saldo)
    
    elif opcion == 3:
        saldo = retirar(saldo)
        
    elif opcion == 0:
        print("gracias por usar nuestro cajero, hasta pronto")
        
    else:
        print("la opcion elegida no es valida")