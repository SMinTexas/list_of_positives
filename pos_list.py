# Given a list of numbers, create a new list which contains every number
# in the given list which is positive.

numbers = [-2, 0, 9, 17, 21, -21, -17, -9, 0, 2]
pos_list = []

for number in numbers:
    if number > 0:
        pos_list.append(number)

print(f"The original list is: {numbers}")
print(f"The new list of positive numbers is: {pos_list}")