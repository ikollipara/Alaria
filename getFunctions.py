"""
Get Functions
Ian Kollipara
Started: 10/2/17
"""

from slowType import text
import checkers

def get_yes_no(prompt):
    text(prompt, .005)
    yesNo = input()
    yesNo = yesNo.lower()
    if yesNo in ['y','yes','sure','okay','yep','of course','yea','yeah']:
        yesNo = 'yes'
    elif yesNo in ['n','no','nope','nah','nah fam','no way']:
        yesNo = 'no'
    while yesNo not in ['n','y','yes','no','okay','nah fam','nah','no way','sure','yep','of course','nope']:
        text("Please Clarify", .005)
        print()
        text(prompt, .005)
        yesNo = input()
        yesNo = yesNo.lower()
    return yesNo
    
def get_number(prompt):
    number = input(prompt)
    isNumber = checkers.number_checker(number)
    while isNumber == False:
        number = input("Please input an actual number: ")
        isNumber = checkers.number_checker(number)
    return number

def is_negative(number):
    if number < 0:
        number = input("Please enter a postive number: ")
        number = float(number)
    return number

def get_binary(prompt):
    binaryList = ['1','0']
    isBinary = False
    while isBinary == False:
        text(prompt, .005)
        binary = input()
        isBinary = checkers.binary_checker(binary)
    return binary

def get_list_number(prompt, number):
    legalValues = range(1, number+1)
    legalValues = str(list(legalValues))
    choice = input(prompt)
    while choice not in legalValues:
        print("Please select someting on the list")
        choice = input(prompt)
    return choice

def get_integer(prompt):
    isInteger = False
    while isInteger == False:
        integer = input(prompt)
        isInteger = checkers.integer_checker(integer)
    return integer

def find_binary(number):
    number = str(number)
    if number[-1] == '5':
        binary = '1'
    else:
        binary = '0'
    return binary

def find_length(item):
    length = len(item)
    return length

def is_true(tester, thing):
    if tester in thing:
        isTrue = True
    else:
        isTrue = False
    return isTrue

def find_file(question):
    file = input(question)
    isTrue = is_true('.',file)
    if isTrue == True:
        if file[-3] or file[-4] or file[-5] == '.':
            file = file
        else:
            file = None
    else:
        file = None
    return file
