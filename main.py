
import sys

# Simulate an OR logic gate with a perceptron

def perceptron_OR(x1, x2):
    w1 = 1
    w2 = 1
    b = -0.5
    output = 1 if (x1*w1 + x2*w2 + b) >= 0 else 0
    return output

# Simulate an AND logic gate with a perceptron

def perceptron_AND(x1, x2):
    w1 = 1
    w2 = 1
    b = -1.50
    output = 1 if (x1*w1 + x2*w2 + b) >= 0 else 0
    return output

# Check if the PIN entered matches the one saved for the user
def check_user_pin(account_data, pin, entered_pin):
    if pin in account_data:   # Let's assume that 'pin' is a key in the account dictionary
        if accounts[pin].get('password') == entered_pin:
            return True # The PIN is correct, return True
    return False    # Altrimenti False

# Returns True if the account is blocked
def account_locked(account_data, username_locked):  # Function to check if the account is locked
    if username_locked in account_data:
        if accounts[username_locked].get('block') == True:
            return True
    return False

# Returns True if the user has reached the maximum number of attempts
def count_tentative(account_data, username):
    if username in account_data:
        if accounts[username].get('count_tentative_saved') == 3:
            return True
    return False

# Dictionary representing user accounts with password, lockout status and number of attempts
accounts = {             # Creation of the dict
    'Giacomo': {'password': '1425', 'block': False , 'count_tentative_saved': 0},
    'Andrea': {'password': '1564', 'block': False , 'count_tentative_saved': 1},
    'Pino': {'password': '1768', 'block': True , 'count_tentative_saved': 3}
}

# Main loop: ask for username and check account status via perceptron
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
            
            # Up to 3 attempts to enter the correct PIN
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
