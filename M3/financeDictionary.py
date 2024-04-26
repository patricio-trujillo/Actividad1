global_account_id = 0

def create_account(accounts,name,account_type):
    global global_account_id
    account = {"account_id": global_account_id,"name":name,"account_type":account_type,"transactions":[]}
    accounts.append(account)    
    global_account_id += 1
    return account["account_id"]

def find_account_by_name(account, account_name ):
    for account in accounts:
        if account["name"] == account_name:
            return account
    return None
    


def add_transaction(accounts,account_id,description,amount ):
    account = find_account_by_name(accounts,account_id)
    if account:
        account["transactions"].append({"description":description,"amount":amount})
    else:
        print("No se encontro la cuenta")
    
 
def calculate_transaction(account):    
    return sum([transaction["amount"] for transaction in account["transactions"]])
  
     
     
    
def get_account_balance(accounts,account_id):
    balance = 0
    account = find_account_by_name(accounts,account_id)
    if account:
        for transaction in account["transactions"]:
            if account["account_type"] =="ingresos":
                balance += transaction["amount"]
            elif account["account_type"] =="egresos":
                balance -= transaction["amount"]
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


