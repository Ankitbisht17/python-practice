# 1) Positive, Negative, or Zero
# Take a number and print:
# Positive
# Negative
# Zero

# data=input('enter the number: ')
# if '1'<=data:
#     print('it is the positive value. ')
# elif '-1'>=data:
#     print('it is the negative value. ')
# else:
#     print('it is the zero ')



#2) Largest of Three Numbers
# Take three numbers.
# Print the largest without using max().

# a=int(input('enter the number: '))
# b=int(input('enter the number: '))
# c=int(input('enter the number: '))
# if a<b<c:
#     print(f'{c} is the largest number.')
# elif a<b>c:
#     print(f'{b} is the largest number. ')
# else:
#     print(f'{a} is the largest number. ')
    
    
# 3) Check Leap Year
# Input a year.
# Print whether it is a leap year.
# (Hint: divisible by 4, 100, 400 — think carefully)

# year=int(input('enter the leap year: '))
# while year%4==1:
#     year=int(input('enter the leap year: '))
#     if year%4==0:
#         print(f'{year} is the leap year')


# 4)Input a number.
# Count how many even digits are present.
# Example:
# 48293 → 3 (4, 8, 2)

# num = int(input("Enter a number: "))
# count = 0  
# while num > 0:
#     digit = num % 10 
#     if digit % 2 == 0:  
#         count = count + 1
#     num = num // 10  
# print("Even digits count:", count)


#5) Keep Asking Until Correct Password
# Store password = "python123"
# Keep asking user to enter password.
# Stop only when correct.

password="python123"
user=input('enter the password: ')
if user!=password:
    user=input('enter the username: ')
else:
    print('login successfully. ')