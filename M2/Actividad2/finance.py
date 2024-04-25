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


