import random

letterbank_lower = 'abcdefghijklmnopqrstuvwxyz'
letterbank_upper = letterbank_lower.upper()
numberbank = '1234567890'
symbolbank = '!@#$%^&*()-=_+`~{}|[];:<>,./?'
thebank = [letterbank_lower,letterbank_upper,numberbank,symbolbank]
password = []

def charcheck(check):
    try:
        if check.upper() == 'Y':
            check = 1
        elif check.upper() == 'N':
            check = 0
        else:
            print('You have entered an invalid input')
    except ValueError:
        print('You have entered an invalid input')
    return check


while True:
    is_lower = input('Password contains lower case characters? Y/N\n')
    is_lower = charcheck(is_lower)
    if is_lower == 1 or is_lower == 0:
        break

while True:
    is_upper = input('Password contains upper case characters? Y/N\n')
    is_upper = charcheck(is_upper)
    if is_upper == 1 or is_upper == 0:
        break


while True:
    is_numbers = input('Password contains numbers? Y/N\n')
    is_numbers = charcheck(is_numbers)
    if is_numbers == 1 or is_numbers== 0:
        break


while True:
    is_symbols = input('Password contains symbols? Y/N\n')
    is_symbols = charcheck(is_symbols)
    if is_symbols== 1 or is_symbols == 0:
        break

if is_lower == False:
    thebank.remove(letterbank_lower)
if is_upper == False:
    thebank.remove(letterbank_upper)
if is_numbers == False:
    thebank.remove(numberbank)
if is_symbols == False:
    thebank.remove(symbolbank)
if len(thebank) == 0:
    print('You have no characters to choose from. The program will now close.')
    exit()

try:
    passlength = int(input('Finally, please enter the desired length of the password. Invalid inputs will automatically be 12.\n'))
except ValueError:
    print('Your value is invalid. Your password length is assigned as 12 characters.')
    passlength = 12

for p in range(0,passlength):
    password.append(random.choice(random.choice(thebank)))

print(f'Your password is {"".join(password)}')
