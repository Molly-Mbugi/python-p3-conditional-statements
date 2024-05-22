#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
# control_flow.py

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # your code here
    pass
def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"


def fizzbuzz(num):
    # your code here
    pass
def fizzbuzz(num):
    if num % 3 ==0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
         return num




def calculator(operation, num1, num2):
    # your code here
    pass


def calculator(operation, num1, num2):
    # Dictionary to map operations to lambda functions
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Division by zero is undefined"
    }
    
    # Get the function based on the operation
    func = operations.get(operation)
    
    if func:
        return func(num1, num2)
    else:
        print("Invalid operation!")
        return None


