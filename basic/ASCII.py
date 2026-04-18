# ASCII is used for the finding the value of the data stored.
# ord = ordenal function

# WAP to print ASCII value of a char only if it is uppercase
# value=input('enter the name in uppercase: ')
# if 'A'<=value<='Z':
#     print(f"{value} is in uppercase: ",ord(value))


# WAP to check whether a given char is lowercase or not.

# value=input('enter the name in lowercase: ')
# if 'a'<=value<='z':
#     print(f"{value} is in lowercase: ")


# WAP to check whether a given char is special char or no.

# value=input('enter the char: ')
# if not 'a'<=value<='z' and not 'A'<=value<='Z' and not '0'<=value<='9':
#     print(f"{value} is a special char: ")


# WAP to check whether a given digit is 3 digit or not.

# value=int(input('enter the digit: '))
# if 100<=value<1000:
#     print(f"{value} is a 3 digit number: ") 


# WAP to check whether a last digit of a number char or not.

# value=input('enter the char: ')
# if value[-1].isalpha():
#     print(f"the last digit of {value} is a char. ")
# else:
#     print(f"the last digit of {value} is not a char. ")
     


# WAP to check whether a last digit of a number is 5 or not.
# value=int(input('enter the digit: '))
# if value%10 == 5:
#     print(f"the last digit of {value} is 5: ")



# WAP to check if the data is single value data type or not.
# value=input('enter the single value data: ')
# if type(value) == int or type(value) == float or type(value) == bool:
#     print(f"{value} is a single value data type: ")

# find the greatest among two number
# a=int(input('enter the first number: '))
# b=int(input('enter the second number: '))
# if a >b:
#     print(f'{a} is the greatest among the two.')
# elif b>a:
#     print(f'{b} is the greatest among the two')
# else:
#     print(f'{a} and {b} are equal.')

# find the greatest among three number
# a=int(input('enter the first number: '))
# b=int(input('enter the second number: '))
# c=int(input('enter the third number: '))
# if a >b and a>c:
#     print(f'{a} is the greatest among the three.')
# elif b>c:
#     print(f'{b} is the greatest among the three')
# else:
#     print(f'{c} is the greatest among the three')

# WAP to print if number is divisible by 5 print fizz and if by 3 print buzz and if with both fizzbuzz
# a=int(input('enter the first number: '))
# if a%3==0 and a%5==0:
#     print('FIZZBUZZ')
# elif a%5==0:
#     print('FIZZ')
# else:
#     print('BUZZ')

# print the quadirant of the x and y 
# x=int(input('enter the value of x quadirent: '))
# y=int(input('enter the value of y quadirent:  '))
# if x>=0 and y>=0:
#     print(f'{x} and {y} belongs to 1st quadirent.')
# elif x<=0 and y>=0:
#     print(f'{x} and {y} belongs to 2nd quadirent.')
# elif x<=0 and y<=0:
#     print(f'{x} and {y} belongs to 3rd quadirent.')
# else:
#     print(f'{x} and {y} belongs to 4th quadirent.')

# check number is single digit, two digit, three digit or more than three digit.
# value=int(input('enter the digit: '))
# if 0<=value<9:
#     print(f"{value} is a single digit number: ") 
# elif 10<=value<99:
#     print(f"{value} is a two digit number: ") 
# elif 100<=value<999:
#     print(f"{value} is a three digit number: ") 
# else:
#     print(f'{value} is more than three digit number:')


# to check given character is uppercase , lowercase, or digit or a special character
# value=input('enter the character: ')
# if 'A'<=value<'Z':
#     print(f"{value} is a uppercase. ") 
# elif 'a'<=value<'z':
#     print(f"{value} is a lowercase. ") 
# elif "0"<=value<"9":
#     print(f"{value} is a digit. ") 
# else:
#     print(f'{value} is a special character.')

# greatest among 4 number
# a=int(input('enter the first number: '))
# b=int(input('enter the second number: '))
# c=int(input('enter the third number: '))
# d=int(input('enter the fourth number: '))
# if a >b and a>c and a>d:
#     print(f'{a} is the greatest among the four.')
# elif b>c and b>d:
#     print(f'{b} is the greatest among the four.')
# elif c>d:
#     print(f'{c} is the greatest among the four.')
# else:
#     print(f'{d} is the greatest among the four.')
