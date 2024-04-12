def create_account(accounts,name,account_type):
    account_id= len(accounts)
    account = [account_id,name,account_type,[]]
    accounts.append(account)    
    return account_id


def add_transaction(accounts,account_id,description,amount ):
    for account in accounts:
        if account[0] == account_id:
            account[3].append([description,amount])
            break    

def get_account_balance(accounts,account_id):
    balance = 0
    for account in accounts:
        if account[0] == account_id:
            for transaction in account[3]:
                if account[2] == 'ingreso':
                    balance += transaction[1]
                elif account[2] == 'egreso':
                    balance -= transaction[1]
            break
    return balance


def get_total_balance(accounts):
    total_balance = 0
    for account in accounts:
        balance = get_account_balance(accounts,account[0])
        total_balance += balance
    return total_balance




accounts = []  # Lista para almacenar las cuentas

# Crear una cuenta de ahorros para Juan
#create_account(accounts, 'Juan', 'ingresos')
#create_account(accounts, 'María', 'egresos')
'''
account_id=create_account(accounts, 'Juan', 'ingreso')
print(account_id)

#Agregar transacciones
add_transaction(accounts, account_id, 'Compra de comestibles',100.0)
add_transaction(accounts, account_id, 'Arriendo de departamento', 500.0)
# Obtener el saldo de la cuenta
account_id=create_account(accounts, 'Pepito', 'egreso')
print("agregando egresos",account_id)
#Agregar transacciones
add_transaction(accounts, account_id, 'Compra de comestibles',50.0)
add_transaction(accounts, account_id, 'Arriendo de departamento', 300.0)
print(accounts)

balance = get_account_balance(accounts, account_id)
print("Saldo de la cuenta:", balance)

total_balance = get_total_balance(accounts)
print("Saldo total de todas las cuentas:", total_balance)
'''


def main():
    accounts = []
    while True:
        print("\nMenu:")
        print("1. Crear cuenta")
        print("2. Agregar transacción")
        print("3. Obtener saldo de una cuenta")
        print("4. Obtener saldo total")
        print("5. Ver cantidad de cuentas existentes")
        print("6. Listar todas las cuentas")
        print("7. Salir")

        choice = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if choice == '1':
            name = input("Ingrese el nombre del titular de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta (ingreso/egreso): ")
            create_account(accounts, name, account_type)
            print("Cuenta creada exitosamente.")

        elif choice == '2':
            account_id = int(input("Ingrese el ID de la cuenta: "))
            description = input("Ingrese la descripción de la transacción: ")
            amount = float(input("Ingrese el monto de la transacción: "))
            add_transaction(accounts, account_id, description, amount)
            print("Transacción agregada exitosamente.")

        elif choice == '3':
            account_id = int(input("Ingrese el ID de la cuenta: "))
            balance = get_account_balance(accounts, account_id)
            print(f"El saldo de la cuenta {account_id} es: {balance}")

        elif choice == '4':
            total_balance = get_total_balance(accounts)
            print(f"El saldo total de todas las cuentas es: {total_balance}")

        elif choice == '5':
            print(f"La cantidad de cuentas existentes es: {len(accounts)}")

        elif choice == '6':
            print("\nListado de todas las cuentas:")
            for account in accounts:
                print(f"ID: {account[0]}, Titular: {account[1]}, Tipo: {account[2]}")
                print("Transacciones:")
                for transaction in account[3]:
                    print(f"  Descripción: {transaction[0]}, Monto: {transaction[1]}")

        elif choice == '7':
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
