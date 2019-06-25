# Author: Clifford Zhan
# Date: 25.6.2019
# Project Name: Calculator

# Version 1: a calculator that take the input from user and print result of calculation. Integers only.
# Note: use regular expression to check validality.
# The calculation includes + - * /. 
import re

# Convert string to number, and identify sign.
def StrToNum(string):
    inputsign = 0
    signcount = 0
    for idx,char in enumerate(string):
        if char in ['+','-','*','/']:
            inputsign = char
            signcount = signcount+1
            #Check if numbers are available.
            #use slice to find 2 numbers before and after sign.
            number1 = int(string[0:idx])
            number2 = int(string[(idx+1):])
            if signcount>1:
                print('You input too many signs at a time')
                break
    if inputsign == 0:
        print('you should input a sign to perform calculation')
    return number1,number2,inputsign

#use regular expression to check if input is correct
def stringcheck(string):
    stringformat = r'^\d+[\+\-\*\/]\d+$'
    if re.match(stringformat,string):
        #print('Input is valid')
        return 1
    else:
        print('Input is invalid, please input a number followed by a sign and a number')
        return 0

print('Please input numbers with sign+-*/, finish with enter. Integers only')
print('Type \'q\' to quit program')
while(1):
    inputformula = input()
    if inputformula =='q':
        break
    if stringcheck(inputformula):
        num1,num2,inputsign = StrToNum(inputformula)
        if inputsign == '+':
            result = num1+num2
        elif inputsign == '-':
            result = num1-num2
        elif inputsign == '*':
            result = num1*num2
        else:
            result = num1/num2
        print('result is:',result)



