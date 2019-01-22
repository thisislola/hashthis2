# The lamest hashing program in Python 3
# by Lorena Carthy

import hashlib

plain_str = input('**************************** \n'
                  '*   H A S H   T H I S   2  *\n'
                  '****************************\n'
                  'Encrypt string: ')

options = ['MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512', 'All above', 'Quit']

print('** Encoding options **')
for i in range(len(options)):
    print('  ', str(i+1) + ":", options[i])

inp = int(input("Select:  "))
try:
    if inp in range(1, 10):
        # if inp == options[inp-1]:
        if inp == 1:
            print('Result of string encoded to MD5:', hashlisb.md5(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 2:
            print('Result of string encoded to SHA1:', hashlib.sha1(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 3:
            print('Result of string encoded to SHA224:', hashlib.sha224(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 4:
            print('Result of string encoded to SHA256:', hashlib.sha256(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 5:
            print('Result of string encoded to SHA384:', hashlib.sha384(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 6:
            print('Result of string encoded to SHA512:', hashlib.sha512(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 7:
            print('Encoded to MD5:', hashlib.md5(plain_str.encode('UTF-8')).hexdigest())
            print('Encoded to SHA1:', hashlib.sha1(plain_str.encode('UTF-8')).hexdigest())
            print('Encoded to SHA224:', hashlib.sha224(plain_str.encode('UTF-8')).hexdigest())
            print('Encoded to SHA256:', hashlib.sha256(plain_str.encode('UTF-8')).hexdigest())
            print('Encoded to SHA384:', hashlib.sha384(plain_str.encode('UTF-8')).hexdigest())
            print('Encoded to SHA512:', hashlib.sha512(plain_str.encode('UTF-8')).hexdigest())
        elif inp == 8:
            print('Goodbye!')
    else:
        print('Invalid input.')
except IndexError:
    print('That is not an option.')
