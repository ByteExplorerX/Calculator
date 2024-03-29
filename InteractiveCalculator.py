import os
import time

# Arithmetic Operations:
def main():
    welcome_message()
    history = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()        
        user_choice = input("Please enter your choice or 'exit' to quit: ")
        if user_choice.lower() == 'exit':
            print("Exiting. Goodbye!")
            break       
        os.system('cls' if os.name == 'nt' else 'clear')
        # Handle user's choice:
        if user_choice == "1":
            # Addition
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print(f"The result of addition is: {result}")
            history.append(f"Result: {num1} + {num2} = {result}")
            time.sleep(2)
        elif user_choice == "2":
            # Subtraction
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract_numbers(num1, num2)
            print(f"The result of substraction is: {result}")  
            history.append(f"Result: {num1} - {num2} = {result}")
         
            time.sleep(2)
        elif user_choice == "3":
            # Multiplication
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply_numbers(num1, num2)
            print(f"The result of multiplication is: {result}")
            history.append(f"Result: {num1} * {num2} = {result}")            
            time.sleep(2)
        elif user_choice == "4":
            # Division
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = divide_numbers(num1, num2)
            print(f"The result of division is: {result}") 
            history.append(f"Result: {num1} / {num2} = {result}")           
            time.sleep(2)
        elif user_choice == "5":
            # Comparisons
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = compare_numbers(num1, num2)
            print(result)
            history.append(result)           
            time.sleep(2)
        elif user_choice == "6":
            # Logical OR Operation
            val1 = int(input("Enter the first value (True [1] or False [0]): "), base=2)
            val2 = int(input("Enter the second value (True [1] or False [0]): "), base=2)
            result = logical_or_operation(val1, val2)
            print(f"The result of logical OR operation is: {result}")
            history.append(f"Result: {val1} OR {val2} = {result}")            
            time.sleep(2)
        elif user_choice == "7":
            # Logical AND Operation
            val1 = int(input("Enter the first value (True [1] or False [0]): "), base=2)
            val2 = int(input("Enter the second value (True [1] or False [0]): "), base=2)
            result = logical_and_operation(val1, val2)
            print(f"The result of logical AND operation is: {result}")     
            history.append(f"Result: {val1} AND {val2} = {result}")       
            time.sleep(2)
        elif user_choice == "8":
            # Logical XOR Operation
            val1 = int(input("Enter the first value (True [1] or False [0]): "), base=2)
            val2 = int(input("Enter the second value (True [1] or False [0]): "), base=2)
            result = logical_xor_operation(int(val1), int(val2))
            print(f"The result of logical XOR operation is: {result}")
            history.append(f"Result: {val1} XOR {val2} = {result}")            
            time.sleep(2)
        elif user_choice == "9":
            # Modulus Calculation
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter the second number: "))
            result = calculate_modulus(num1, num2)
            print(f"The result of modulus is: {result}")
            history.append(result)                   
            time.sleep(2)    
        elif user_choice == "10":
            # Factorial Calculation
            num = int(input("Enter a non-negative integer: "))
            result = calculate_factorial(num)
            print(f"The result of factorial calculation is: {result}")  
            history.append(result)          
            time.sleep(2)
        elif user_choice == "11":
            print("Here is your history:")
            print()
            for _ in history:
                print(_)
            print()
            input("Press enter to continue...")
            
        elif user_choice == "12":
            # Exit
            break            
        else:
            print("Please enter a valid number. Returning to the menu...")
            time.sleep(2.5)  
            
def welcome_message():
    print("""
Welcome to "Interactive Calculator" by Juri... proceeding to menu .....

                             ┌───────────┐
                             │  ^     ^  │
                             │  O     O  │
                             │     *     │
                             │           │
                             │  (─────)  │
                             │           │
                             └───────────┘
""")
    time.sleep(2.5)
                
def display_menu():
    print("Chose an operation: ")
    print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Comparisons
6. Logical OR Operation
7. Logical AND Operation
8. Logical XOR Operation
9. Modulus Calculation
10. Factorial Calculation
11. Results History
12. Exit
        """)
    
    
# Addition:
def add_numbers(num1, num2):
    result = num1 + num2
    return int(result)

# Subtraction:
def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

# Multiplication:
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

# Division:
def divide_numbers(num1, num2):
    result = num1 / num2
    return result

# Logical Operations:

# Comparisons:
def compare_numbers(num1, num2):
    if num1 < num2:
        return f"{num1} is smaller than {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    else:
        return f"{num1} is equal to {num2}"

# Logical OR Operation:
def logical_or_operation(val1, val2):
    result = val1 or val2
    return result

# Logical AND Operation:
def logical_and_operation(val1, val2):
    result = val1 and val2
    return result

# Logical XOR Operation:
def logical_xor_operation(val1, val2):
    result = val1 ^ val2
    return result

# Additional Functionalities:

# Modulus Calculation:
def calculate_modulus(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    
    result = num1 % num2
    return result

# Factorial Calculation:
def calculate_factorial(num):
    if num < 0:
        return "If a number is negative, the factorial is not defined."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * calculate_factorial(num - 1)

# Entry point of the program:
if __name__ == "__main__":
    main()
