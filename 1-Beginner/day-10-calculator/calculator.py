# Calculator
from art import logo
import os

clear = lambda: os.system('clear')
# Add
def add(num1, num2):
  return num1 + num2


# Subtract
def subtract(num1, num2):
  return num1 - num2


# Multiply
def multiply(num1, num2):
  return num1 * num2


# Divide
def divide(num1, num2):
  return num1 / num2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
  print(logo)
  number1 = float(input("What's the first number? "))
  for symb in operations:
    print(symb)

  last = False

  while not last:
    operation_symbol = input("Pick an operation from the line above: ")
    number2 = float(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")

    continue_calc = input(
        f"Type 'y' to continue calculating with {answer}, or type 'r' to restart, or neither to exit: "
    )
    if continue_calc.lower() == 'y':
      number1 = answer
    elif continue_calc.lower() == 'r':
      last = True
      clear()
      calculator()
    else:
      last = True
      print("Goodbye, thanks for using the calculator!")


calculator()
