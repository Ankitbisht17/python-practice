# 1) waf to covert the string to uppercase.
# def upper():
#     a=input('enter the string: ')
#     out=''
#     for i in a:
#         if 'a'<=a<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=1
#     print(out)
# upper()
# 2) to count the number of occurance of given char in a given string 
# def count():
#     a=input('enter the string: ')
#     ch=input('enter the count the char: ')
#     count=0
#     for i in a:
#         if i==ch:
#             count+=1
#     print(count)
# count()

#3) WAP to create a function which will extact pallindrome.
#l=['ji',5,6.2,'aba',8+5j,'pop']
#out=['aba','pop']
# def pallin(l):
#     out=[]
#     for i in l:
#         if type(i)==str:
#             if i == i[::-1]:
#                 out.append(i)
#     print(out)
# pallin(eval(input('enter the list:')))

# 4) WAP to find greater among three number.
# def greater():
#     a=int(input('enter the 1st number: '))
#     b=int(input('enter the 2nd number: '))
#     c=int(input('enter the 3rd number: '))
#     if a>=b:
#         if a>=c:
#             print(f'{a} is greater.')
#         else:
#             print(f'{c} is greater.')
#     else:
#         if b>=c:
#             print(f'{b} is greater.')
#         else:
#             print(f'{c} is greater.')
# greater()