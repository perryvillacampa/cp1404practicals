for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a. Count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print a number of stars.
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# d. print lines of increasing stars.
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)

