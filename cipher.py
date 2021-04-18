# Caesar Cipher Miniproject
# [DESCRIPTION] -> Given a string and key shift value, the cipher will encrypt / decrypt the string using the caesar
# cipher algorithm.


# Fetch method, user message, and key for the shift
method = input('Do you wish to encrypt or decrypt your message? Enter E for Encrypt or D for decrypt (E/D) ')

if (method.upper().strip() != 'E' and method.upper().strip() != 'D'):
    print("Not a valid option, please enter either 'E' or 'D'")
    exit()

key = input('What is the secret key value you wish to use? (1-25)' ) 
key = int(key) 

if (int(key) < 1 or int(key) > 25):
    print("You must select a value between 1 and 25")
    exit()


# Encrypt message
def encrypt():

    msg = input('What is the message you want to encrypt? ')

    if (msg.replace(' ', '').isalpha() == False):
        print(msg.strip())
        print('You may only enter strings that contain letters')
        exit()
   
    str = ""
    #ignore spaces 
    for i in range (0, len(msg)):
        if msg[i] == ' ':
            str += ' '
            continue
        
        # loopback to a if ascii total ascii value exceeds 123 (which is z)
        if msg[i].islower():
            if ord(msg[i]) + key >= 123:
                str += chr((97 + (ord(msg[i]) + key) % 123))
            else:
                str += chr(ord(msg[i]) + key)

        if msg[i].isupper():
            if ord(msg[i]) + key >= 91:
                str += chr((65 + (ord(msg[i]) + key) % 91))
            else:
                str += chr(ord(msg[i]) + key)
    return str 

# Decrypt message
def decrypt():

    msg = input('What is the message you want to decrypt? ')
    if (msg.replace(' ', '').isalpha() == False):
        print(msg.strip())
        print('You may only enter strings that contain letters')
        exit()

    str = ""
    #ignore spaces 
    for i in range (0, len(msg)):
        if msg[i] == ' ':
            str += ' '
            continue

        if msg[i].islower():
            if ord(msg[i]) - key <= 97:
                loopbackValue = 97 % (ord(msg[i]) - key)
                str += chr(123 - loopbackValue)
            else:
                str += chr(ord(msg[i]) - key)

        if msg[i].isupper():
            if ord(msg[i]) - key <= 65:
                loopbackValue = 65 % (ord(msg[i]) - key)
                str += chr(91 - loopbackValue)
            else:
                str += chr(ord(msg[i]) - key)
    return str    

if (method.upper().strip() == 'E'):
    print(encrypt())

if (method.upper().strip() == 'D'):
    print(decrypt())



