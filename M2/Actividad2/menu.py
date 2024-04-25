from finance import create_account, add_transaction, get_account_balance, get_total_balance

# Función principal

def main():
    #inicializamo la lista de cuentas
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

        opcion = int(input("Ingrese el número correspondiente a la acción que desea realizar: "))

        if opcion == 1:
            name = input("Ingrese el nombre del titular de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta (ingreso/egreso): ")
            
            account_id = create_account(accounts, name, account_type)
            
            print(f"Cuenta creada exitosamente. ID de la cuenta : {account_id}\n")

        elif opcion == 2:
            account_id = int(input("Ingrese el ID de la cuenta: "))
            description = input("Ingrese la descripción de la transacción: ")
            amount = float(input("Ingrese el monto de la transacción: "))
            
            add_transaction(accounts, account_id, description, amount)
            
            print("Transacción agregada exitosamente.")

        elif opcion == 3:
            account_id = int(input("Ingrese el ID de la cuenta: "))
            balance = get_account_balance(accounts, account_id)
            print(f"El saldo de la cuenta {account_id} es: {balance}")

        elif opcion == 4:
            total_balance = get_total_balance(accounts)
            print(f"El saldo total de todas las cuentas es: {total_balance}")

        elif opcion == 5:
            print(f"La cantidad de cuentas existentes es: {len(accounts)}")

        elif opcion == 6:
            print("\nListado de todas las cuentas:")
            for account in accounts:
                print(f"ID: {account[0]}, Titular: {account[1]}, Tipo: {account[2]}")
                print("Transacciones:")
                for transaction in account[3]:
                    print(f"  Descripción: {transaction[0]}, Monto: {transaction[1]}")

        elif opcion == 7:
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
