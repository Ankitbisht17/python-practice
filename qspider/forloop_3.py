# wap to fin len of a given colln without len funtion 
# n = input("Enter the character: ")
# num = 0
# for i in n:
#     num = num + 1
# print("Length is:", num) 

#extract vowel from string 
# s = input("Enter string: ")
# vowel = ""
# for i in s:
#     if i in "aeiouAEIOU":
#         vowel = vowel + i
# print("Vowel are:", vowel)
 
#wap to replace space '_'{underscore} I/p= py ti hi o/p=py_ti_hi 
# s = input("Enter string: ")
# result = ""
# for i in s:
#     if i == " ":
#         result = result + "_"
#     else:
#         result = result + i
# print(result)

#to check a given string palindrome or not without slicing 
# s = input("Enter string: ")
# rev = ""
# i = 0
# while i < len(s):
#     rev = s[i] + rev
#     i += 1
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#wap to remove duplicates from list
# n = eval(input("Enter list: "))
# unique = []
# for i in n:
#     if i not in unique:
#         unique.append(i)
# print("Without duplicates:", unique)

# extract all int which are multiple of 5 and three digit in it from the given list.
# num = eval(input('enter the list: '))
# out=[]
# for i in num:
#     if type(i)==int:
#         if i%5==0 and 99<=i<=999:
#             out.append(i)
# print(out)

# to remove duplicates values from a list 
# a = eval(input('enter the list: '))
# out=[]
# for i in a:
#     if i not in out:
#          out.append(i)
# print(out)

# WAP to print a number is strong number or not ?
# a=int(input('enter the number: '))
# num=0
# for i in str(a):
#     fact=1
#     digit=int(i)
#     for j in range (digit,0,-1):
#         fact=fact*j
#     num=fact+num
# if num==a:
#     print('it is the strong number: ')
# else:
#     print('it not the strong number. ')

# l=[12,'program',6+5j,5.3,'break',9]
# output = {'program':'oa','break':'ea'}
# l = [12, 'program', 6+5j, 5.3, 'break', 9]
# d = {}
# for i in l:
#     if type(i) == str:
#         vowel = ''
#         for ch in i:
#             if ch in 'aeiou':
#                 vowel = vowel + ch
#         d[i] = vowel

# print(d)

# l=[12,'program',6+5j,5.3,'break',9]
# output1 = {'program':'PROGRAM','break':'BREAK'}
# output2 = {'program':'prgrm','break':'brk'}
# l = [12,'program',6+5j,5.3,'break',9]
# d1 = {}
# d2 = {}
# for i in l:
#     if type(i) == str:
#         d1[i] = i.upper()
#         consonant = ''
#         for ch in i:
#             if ch not in 'aeiou':
#                 consonant += ch
#         d2[i] = consonant
# print(d1)
# print(d2)

# l=[10,13,4,6]
# out=[23,20,29,27]
# l = [10, 13, 4, 6]
# total = sum(l)
# out = []
# for i in l:
#     out.append(total - i)
# print(out)


# a = int(input('enter the number:'))
# for i in range(a):
#     for j in range(i):
#         print("*", end=" ")
#     print("@")

# n = int(input('enter the number: '))
# for i in range(n):
#     for j in range(n - i):
#         print("#", end=" ")
#     print("$", end=" ")
#     for j in range(i):
#         print("&", end=" ")
#     print()

# n = int(input("Enter n: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == n//2 + 1 or j == n//2 + 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if (i == 1 or i == n or j == 1 or j == n) or (i == j) or (i + j == n + 1):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
    

# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     for s in range(n - i):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if i == n or j == 1 or j == 2*i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input('enter the number: '))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j <= n:
#             print(j, end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# n = int(input('enter the number: '))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i <= n:
#             print(i, end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# n = int(input('enter the number: '))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j <= i:
#             print(j, end=' ')
#         else:
#             print(' ', end=' ')
#     print() 
