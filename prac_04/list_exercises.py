"""
Program to read 5 numbers, store them in a list, and display stats.
"""
numbers = []
for i in range(5):
    try:
        number = int(input("Number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        i -= 1
        continue

total_sum = sum(numbers)
count = len(numbers)
average = total_sum / count
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average:.1f}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")


