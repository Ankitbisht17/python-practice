# condition statements 
# 1) if 
# 2) if else
# 3) elif
# 4) nested if 


# 1) If statement
#age 

# age = int(input('enter your age: '))
# if age >= 18:
#     print('your are eligible: ')
# else:
#     print("you are not eligible. ")

# even number 

# num = int(input('enter the number: '))
# if num%2==0:
#     print(f"{num} is a even number: ")

# WAP to check a given number is odd or not?

# num = int(input('enter the number: '))
# if num%2==1:
#     print(f"{num} is a odd  number: ")


#WAP to check wheater a given string is palindrome or not?

# a= input('enter the String: ')
# if a == a[::-1]:
#     print(f'the {a} is a palindrome.')

#WAP to check whether a given string is starting with vowel or not?

# a= input('enter the String: ')
# vowels = 'aeiouAEIOU'
# if a[0] in vowels:
#     print(f'the {a} is a vowel.')

#WAP to check whether the given data is float or not?
# a= eval(input('enter the value: '))
# if type(a) == float:
#     print(f'the {a} is a float. ')

#WAP a square of the number only if it is even.

# a= int(input('enter the value: '))
# if a%2==0:
#     print(f'the {a} is a square. ',(a**2))



#WAP a cube of a number only if it is divisble by 9 or 6.

# num = int(input('enter the number: '))
# if num % 9 and 6 == 0:
#     print(f'this {num} is divisble by 9 or 6: ',(num**3))


# 2) if else statement 

# age = int(input('enter your age: '))
# if age >= 18:
#     print('your are eligible: ')
# else:
#     print('your are not eligible: ')





# 3) elif statement 

# age = int(input('enter your age: '))
# if age >= 18:
#     print('your are eligible: ')
# elif age<=0:
#         print('your are not born:')
# else:
#     print('your are not eligible: ')


# 4) nested if

# db_un='ankit'
# db_pw='test' 
# un=input('enter the username: ')
# if un==db_un:
#     pw=input('enter the password: ')
#     if pw==db_pw:
#         print('loggin successfull. ')
#     else:
#         print('password invaild. ')
# else:
#     print('invaild username')
