import random

def generate_bigsmall(number):
    charset = list(''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) + ''.join([chr(i) for i in range(ord('a'), ord('z')+1)]))
    return ''.join(random.choice(charset) for _ in range(number))

global bigsmall
bigsmall = list(''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) + ''.join([chr(i) for i in range(ord('a'), ord('z')+1)]))

def generate_number(number):
    charset = list(''.join([str(i) for i in range(10)]))
    return ''.join(random.choice(charset) for _ in range(number))

global numbers
numbers = list(''.join([str(i) for i in range(10)]))

def generate_strongcode(number):
    charset = list(''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) + ''.join([chr(i) for i in range(ord('a'), ord('z')+1)]) + ''.join([str(i) for i in range(10)]) + ['!', '#', '$', '%', '&', "'", '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~', '@', ' '])
    return ''.join(random.choice(charset) for _ in range(number))

global strongcode
strongcode = ''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) + ''.join([chr(i) for i in range(ord('a'), ord('z')+1)]) + ''.join([str(i) for i in range(10)]) + ['!', '#', '$', '%', '&', "'", '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~', '@', ' '])

def type_of_code():
    codetype = input("What type of code you want?\n1 -> big and small letters\n2 -> only numbers\n3 -> strong code (big and small letters, numbers and special characters): ")
    if codetype == "cancel":
        cancel()
    if not codetype.isdigit() or int(codetype) < 1 or int(codetype) > 3:
        print("Write 1, 2 or 3")
        type_of_code()
    else:
        return int(codetype)

def get_digits():
    digits = input("How many digits you want?: ")
    if digits == "cancel":
        cancel()
    if not digits.isdigit() or int(digits) < 1 or int(digits) > 30:
        print("Write a number from one to thirty.")
        get_digits()
    else:
        return int(digits)

def write_password():
    password = input("Write your password ({}): ".format(digits))
    if not password.isascii():
        print("Write password in ascii characters.")
        write_password()
    if len(password) != digits:
        print("Write the password with correct number of characters ({})".format(digits))
        write_password()
    return password

def test_password(password, codetype):
    if codetype == 1:
        for char in password:
            if char not in bigsmall:
                print("Write the password in the correct type (only big and small letters)")
                write_password()
        gencode = generate_bigsmall(digits)
    elif codetype == 2:
        for char in password:
            if char not in numbers:
                print("Write the password in the correct type (only numbers)")
                write_password()
        gencode = generate_number(digits)
    elif codetype == 3:
        for char in password:
            if char not in strongcode:
                print("Write the password in the correct type (only big and small letters, numbers and ascii specials characters)")
                write_password()
        gencode = generate_strongcode(digits)
    return gencode

def cancel():
    answer = input("\nDo you want to cancel? (yes/no): ").lower()
    if answer == "yes":
        exit()
    else:
        program()

def program():
    codetype = type_of_code()
    digits = get_digits()
    password = write_password()
    i = 1
    gencode = test_password(password, codetype)
    while gencode != password:
        gencode = test_password(password, codetype)
        i += 1
        print(gencode)
    print("Your password is: {}".format(gencode))
    print("Number of attempts: {}".format(i))
    cancel()

program()
