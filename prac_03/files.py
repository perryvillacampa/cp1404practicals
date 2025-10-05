#1
user_name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(user_name)
name_file.close()
print(f"Name '{user_name}' has been written to name.txt.")

#2
name_file = open("name.txt", "r")
name_from_file = name_file.read()
name_file.close()
name_from_file = name_from_file.strip()
print(f"Hi {name_from_file}!")

#3
with open("numbers.txt", "r") as numbers_file:
    number1_string = numbers_file.readline()
    number2_string = numbers_file.readline()
total_of_two = int(number1_string.strip()) + int(number2_string.strip())
print(f"The total of the first two numbers is: {total_of_two}") # Should print 59

#4
total_of_all = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        number = int(line.strip())
        total_of_all += number
print(f"The total of all numbers is: {total_of_all}") # Should print 459