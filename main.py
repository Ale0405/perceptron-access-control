
import sys

# Simula una porta logica OR con un perceptron
def perceptron_OR(x1, x2):
    w1 = 1
    w2 = 1
    b = -0.5
    output = 1 if (x1*w1 + x2*w2 + b) >= 0 else 0
    return output

# Simula una porta logica AND con un perceptron
def perceptron_AND(x1, x2):
    w1 = 1
    w2 = 1
    b = -1.50
    output = 1 if (x1*w1 + x2*w2 + b) >= 0 else 0
    return output

# Verifica se il PIN inserito corrisponde a quello salvato per l'utente
def check_user_pin(account_data, pin, entered_pin):
    if pin in account_data:   # Assumiamo che 'pin' sia una chiave nel dizionario dell'account
        if accounts[pin].get('password') == entered_pin:
            return True # Il PIN è corretto, restituisci True
    return False    # Altrimenti False

# Restituisce True se l'account è bloccato
def account_locked(account_data, username_locked):  # Funzione per controllare se l'account è bloccato
    if username_locked in account_data:
        if accounts[username_locked].get('block') == True:
            return True
    return False

# Restituisce True se l'utente ha raggiunto il numero massimo di tentativi
def count_tentative(account_data, username):
    if username in account_data:
        if accounts[username].get('count_tentative_saved') == 3:
            return True
    return False

# Dizionario che rappresenta gli account utente con password, stato di blocco e numero di tentativi
accounts = {             # Creazione del Dict
    'Giacomo': {'password': '1425', 'block': False , 'count_tentative_saved': 0},
    'Andrea': {'password': '1564', 'block': False , 'count_tentative_saved': 1},
    'Pino': {'password': '1768', 'block': True , 'count_tentative_saved': 3}
}

# Ciclo principale: chiedi il nome utente e verifica lo stato dell'account tramite perceptron
while True:
    user_input = input('Write you name for the account: ').capitalize()
    locked =  1 if account_locked(accounts, user_input) else 0
    count_native = 1 if count_tentative(accounts, user_input) else 0
    check_AND = perceptron_AND(locked, count_native)
    if check_AND:
        print('You can\'t access because your account is blocked and you have too many login attemps!')
        break
    else:
        check_OR = perceptron_OR(locked,count_native)
        if check_OR:
            if locked == 1:
                print('Access denied because you account is blocked!')
                break
            elif count_native == 1:
                print('Access denied for must because you have too many login attempts!')
                break
        else:
            print(f'Welcome {user_input}!')
            
            count = 0
            max_attemps = 3
            authenticated = False
            
            # Fino a 3 tentativi per inserire il PIN corretto
            while count < max_attemps:
                user_pin = input('Enter the pin: ')
                check_pin = 1 if check_user_pin(accounts, user_input, user_pin) else 0
                if check_pin:
                    authenticated = True
                    break
                else:
                    count += 1
                    accounts[user_input]['count_tentative_saved'] += 1
                    if count < 3 and accounts[user_input]['count_tentative_saved'] < 3:
                        print(f'You enter a wrong pin. Now you have {accounts[user_input]["count_tentative_saved"]} attempts left!')
                    else:
                        print('You have reached the maximum number of attempts. Your account is suspended!')
                        sys.exit()
    if authenticated:
        print('Access allowed!')
        break