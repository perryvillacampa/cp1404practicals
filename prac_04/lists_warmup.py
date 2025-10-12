numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] is the first element, index 0 (3)
# numbers[-1] is the last element
# numbers[3] is the element at index 3 (1)
# numbers[:-1] is [3, 1, 4, 1, 5, 9] All elements up to, but not including, the last one
# numbers[3:4] A slice starting at index 3 and stopping before index 4; always returns a list [1]
# 5 in numbers - The number 5 is present in the list (True)
# 7 in numbers - The number 7 is not present in the list (False)
# "3" in numbers - "3" is a string, and only the number 3 is in the list (False)
# numbers + [6, 5, 3] is the combination of the 2 lists [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#1
numbers[0] = "ten"
print(f"After changing first element: {numbers}")

#2
numbers[-1] = 1
print(f"After changing last element: {numbers}")

#3
print(f"Elements except the first two: {numbers[2:]}")

#4
print(f"Is 9 an element of numbers? {9 in numbers}")
