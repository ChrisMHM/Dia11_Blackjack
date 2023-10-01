import art
import clear
import time

operations = """+
-
*
/"""

again = True
usingResultAgain = False


#Operation functions
def sum(firstNumber, secondNumber):
    """Returns the sum of two integer numbers 
    passed as parameters"""
    return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
    return round(firstNumber/secondNumber, 2)

def choiseOperation(firstNumber, secondNumber, operation):
    result = 0
    if operation == "+":
        result = sum(firstNumber, secondNumber)
    elif operation == "-":
        result = subtract(firstNumber, secondNumber)
    elif operation == "*":
        result = multiply(firstNumber, secondNumber)
    elif operation == "/":
        if secondNumber == 0:
            return None
        else:
            result = divide(firstNumber, secondNumber)
    else:
        result = None

    return result

def getFirstNumber():
    print(art.logo)
    firstNumber = int(input("What's the first number?: "))
    print(operations)

    return firstNumber

def getResult(firstNumber):
    operation = input("Pick an operation: ")
    secondNumber = int(input("What's the next number?: "))
    result = choiseOperation(firstNumber, secondNumber, operation)

    if result is None:
        print("Not valid operation")
    else:
        print(f"{firstNumber} {operation} {secondNumber} = {result}")

    return result

while again:
    if usingResultAgain:
        result = getResult(result)
    else:
        firstNumber = getFirstNumber()
        result = getResult(firstNumber)
    
    if result == None:
        usingResultAgain = False
        time.sleep(3)
        clear.clear()
    else:
        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if repeat == "n":
            clear.clear()
            usingResultAgain = False
        else:
            usingResultAgain = True
