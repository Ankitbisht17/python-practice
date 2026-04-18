# WAP to reverse the given number 
# n = int(input("Enter a number: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)

# WAP to print sum of the individual digit 
# n = int(input("Enter a number: "))
# num = 0
# while n > 0:
#     digit = n % 10
#     num = num + digit
#     n = n // 10
# print(num)


# WAP to print product of even number 
# n = int(input("Enter a number: "))
# num = 1
# while n > 0:
#     digit = n % 10
#     if digit%2==0:
#         num = num * digit
#     n = n // 10
# print(num)

#print sum of n natural number 
# n = int(input("Enter a number: "))
# num = 0
# while n > 0:
#     digit = n % 10
#     num = num + digit
#     n = n // 10
# print(num)

#find the factorial of a number
# n = int(input("Enter a number: "))
# num = 1
# while n > 0:
#     digit = n % 10
#     num = num * digit
#     n = n // 10
# print(num)

# 1. to print every char form the string.
# n = input("Enter a character: ")
# i = 0
# while i < len(n):
#     print(n[i])
#     i += 1

#  to extract lower case character 
# n=input('enter the character: ')
# i=0
# while i<len(n):
#     if 'a'<=n[i]<='z':
#        print(n[i])
#     i+=1

# to extract int from the given list
# n=eval(input('enter the list: '))
# i=0
# num=[]
# while i<len(n):
#     if type(n[i])==int:
#        num.append(n[i])
#     i+=1
# print(num)

#  to extract upperr case character 
# n=input('enter the character: ')
# i=0
# while i<len(n):
#     if 'A'<=n[i]<='Z':
#        print(n[i])
#     i+=1

# WAP to extract uppercase, lowercase, digit and special character in seprate output
# n = input('enter the character: ')
# i = 0
# upper = ''
# lower = ''
# digit = ''
# special = ''
# while i < len(n):
#     if 'A' <= n[i] <= 'Z':
#         upper = upper + n[i]
#     elif 'a' <= n[i] <= 'z':
#         lower = lower + n[i]
#     elif '0' <= n[i] <= '9':
#         digit = digit + n[i]
#     else:
#         special = special + n[i]
#     i += 1
# print("Uppercase:", upper)
# print("Lowercase:", lower)
# print("Digits:", digit)
# print("Special:", special)

# to sum of  int from the given list
# n=eval(input('enter the list: '))
# i=0
# num=0
# while i<len(n):
#     if type(n[i])==int:
#        num = num + n[i]
#     i+=1
# print(num)

# to convert all lowercase char str to uppercase char
# n=input('enter the character: ')
# i=0
# char=''
# while i<len(n):
#     if n[i]==n[i].upper():
#        char = char + n[i].lower()
#     else:
#         char = char+n[i]
#     i+=1
# print(char)


# wap to print the 1  to 10 using while loop
#  skip 3 and 8 
i=1
while i<=10:
    if i==3 or i==8:
        i+=1
        continue
    print(i)
    i+=1