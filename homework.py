#======= Question 1 =======

# Task 1: Code Correction

# Buggy Code

# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

#Fixed Code

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


#======= Question 2 =======

# Task 1: get 3 numbers and identify max

num_1 = int(input("Kindly enter a number: "))
num_2 = int(input("Kindly enter another number: "))
num_3 = int(input("Kindly enter a final number: "))

if num_1 >= num_2 and num_1 >= num_3:
    big_num = num_1
elif num_2 >= num_3:
    big_num = num_2
else:
    big_num = num_3

print(f"The largest of these is {big_num}")

# Task 2: find also the min

small_num = num_1
if num_2 < small_num: small_num = num_2
if num_3 < small_num: small_num = num_3

print(f"The smallest of these is {small_num}")