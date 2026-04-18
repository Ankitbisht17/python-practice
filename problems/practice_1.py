# 1) Write a Python program to Count how many vowels and consonants are present in a given string.
# a=input('enter the character: ')
# b=('AEIOUaeiou')
# vowel=0
# consoants=0
# for ch in a:
#     if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
#         if ch in b:
#             vowel+=1
#         else:
#             consoants+=1
# print('number of vowels and consoants are:',vowel,consoants)

# 2) Write a Python program to check whether a given string is a palindrome or not.
# a = input('enter the character: ')
# rev = ''
# i = len(a) - 1
# while i >= 0:
#     rev = rev + a[i]
#     i -= 1
# if a == rev:
#     print('it is a palindrome')
# else:
#     print('it is not a palindrome')

# 3) Write a Python program to Remove all duplicate characters from a string and print the result string without duplicates.
# a=input('enter the character: ')
# b=''
# for ch in a:
#     if ch not in b:
#        b=b+ch
# print(b)

# 4) Write a Python program to Find the first non-repeating character in a string.
# a = input('enter the character: ')
# for ch in a:
#     count = 0
#     for x in a:
#         if ch == x:
#             count += 1
#     if count == 1:
#         print(ch)
#         break
  
    
# 5) Write a Python program to:
# • Count the frequency of each character in a string
# • Print each character with its count
# • Do NOT repeat characters in output

a= input('enter the character: ')
printed = ''
for ch in a:
    if ch not in printed:
        count = 0
        for x in a :
            if ch == x:
               count +=1
        print(ch,'=',count)
        printed+=ch