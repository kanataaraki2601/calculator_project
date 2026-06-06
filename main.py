
from calculator import Calculator

from utils import get_numbers, save_result, handle_command

calc = Calculator()

def show_results(a, b):
    add_result = calc.add(a, b)
    multiply_result = calc.multiply(a, b)
    
    print("Addition:", add_result)
    print("Multiply:", multiply_result)
    
    save_result(f"{a} + {b} = {add_result}")
    save_result(f"{a} * {b} = {multiply_result}")
    
    try:
        division_result = calc.division(a, b)
        
        print("Division:", division_result)
        
        save_result(f"{a} / {b} = {division_result}")
        
    except ZeroDivisionError:
        print("cannnot divide by zero.")
        

while True:
    command = input("Press Enter to calculate, or type help: ")
    
    
    action = handle_command(command)
    
    if action == "quit":
        break
    if action == "continue":
        continue
    
    try:
        a, b = get_numbers()
        
    except ValueError:
        print("Please enter valid number.")
        continue

    show_results(a, b)
    
    