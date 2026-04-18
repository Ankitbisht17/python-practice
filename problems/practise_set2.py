# 1) WAP to check whether the char is upppercase, lowercase, special char or digit.
# value=input('enter the character: ')
# if '0'<=value<='9':
#     print(f'your {value} is digits. ')
# elif 'A'<=value<='Z':
#     print(f'your {value} is uppercase. ')
# elif 'a'<=value<='z':
#     print(f'your {value} is lowercase. ')
# else:
#     print(f'your {value} is a special character. ')



#function method: 

# value=input('enter the character: ')
# if value.isupper():
#     print(f'your {value} is digits. ')
# elif value.islower()
#     print(f'your {value} is uppercase. ')
# elif value.isdigit()
#     print(f'your {value} is lowercase. ')
# else:
#     print(f'your {value} is a special character. ')



# 2) WAP to check whether the given integer is single digit or two digit or three digit or more.

# value=input('enter the value: ')
# if 0<=value<= 9:
#     print(f'your {value} is single digits. ')
# elif 10<=value<= 99:
#     print(f'your {value} is double digits. ')
# elif 100<=value<=999:
#     print(f'your {value} is three digits . ')
# else:
#     print(f'your {value} is more and three digits. ')


# length function method:

# value=int(input('enter the value: '))
# if len(value)==1:
#     print(f'your {value} is single digits. ')
# elif len(value)==2:
#     print(f'your {value} is double digits. ')
# elif len(value)==3:
#     print(f'your {value} is three digits . ')
# else:
#     print(f'your {value} is more and three digits. ')





# 3) WAP to check the given points are lying in which quadrant.
# value1=int(input('enter the value of x: '))
# value2=int(input('enter the value of y: '))

# if 0<=value1 and 0<=value2:
#     print(f'your  {value1} and  {value2} lies in 1 quadrant.')
# elif -1>=value1<0 and 0<=value2:
#     print(f'your  {value1} and  {value2} lies in 2 quadrant. ')
# elif -1<=value1>0 and -1<=value2<0:
#     print(f'your  {value1} and  {value2} lies in 3 quadrant. ')
# else:
#     print(f'your  {value1} and  {value2} lies in 4 quadrant. ')
    

# 4) WAP to find the greatest among 3 numbers.
# value1=input('enter the number 1 : ')
# value2=input('enter the number 2: ')
# value3=input('enter the number 3: ')

# if value1<=value2<=value3:
#     print(f"number {value3} is greatest among all.")
# elif value1<=value2>=value3:
#     print(f"number {value2} is greatest among all.")
# else:
#     print(f"number {value1} is greatest among all.")


# 5) WAP to find the smallest of 3 numbers.
# value1=input('enter the number 1 : ')
# value2=input('enter the number 2: ')
# value3=input('enter the number 3: ')

# if value1<=value2<=value3:
#     print(f"number {value1} is smallest among all.")
# elif value1>=value2<=value3:
#     print(f"number {value2} is smallest among all.")
# else:
#     print(f"number {value3} is smallest among all.")


# 6) WAP to check the relation between two integers.
# a=input('enter the number 1 : ')
# b=input('enter the number 2: ')
# c=input('enter the number 3: ')

# if a>b and a>c: 
#     print(f"number {a} is greater then {b} and {c} .")
# elif a<b and b>c: 
#     print(f"number {b} is greater then {a} and {c} .")
# else:
#     print(f"number {c} is greater then {a} and {b} .")


# 7) consider a character input if it is uppercase convert it into lowercase ,\\
    # if it is digit print the remainder when it is deivided by 3  else if it is special char print its ascii value 
    
# value=input("enter the character of your choice: ")
# if value.islower():
#     print(value.upper())
# elif value.isupper():
#     print(value.lower())
# elif value.isdigit():
#     print(int(value)%3)
# else:
#     print(ord(value))
    
# 8) WAP to print 'fizz' if the given number is multiple of three print 'buzz' if the given number is mutliple of 5 and\\
    # print 'fizzbuzz' if the number is mutliple of 3 and 5. 

# value=int(input("enter the value: "))
# if value%3==0 and value%5==0:
#     print('fizzbuzz')
# elif value%5==0:
#     print('buzz')
# else:
#     print('fizz')
