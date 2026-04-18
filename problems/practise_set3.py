# # WAP to check user name and password is correct or not.
# username='ankit'
# password='pass123'
# user_name=input('enter the username: ')
# if username==user_name:
#     pass_word=input('enter the password: ')
#     if pass_word==password:
#         print('loggin successfull. ')
#     else:
#         print('password invaild. ')
# else:
#     print('invaild username')

# WAP to check whether the char is vowel or not.
# value=input('enter the character: ')
# vowel='aeiouAEIOU'
# if value==str(value):
#     if value[0] in vowel:
#         print(f'your {value} is a vowel.')
#     else:
#         print(f'your {value} is not a vowel.')
# else:
#     print(f'your {value} is not a character. ')
    

# # WAP to print the middle value if a list only consist of string middle value.

# value=eval(input('enter the list of your choice: '))
# if len(value)%2==1:
#     mid=value[len(value)//2]
#     if type(mid)==str:
#         print(mid)
#     else:
#         print('it has no string. ')
# else:
#     print('your list does not content any middle value')


# # WAP to check the student is passed or not if it is passed, what the grade he got?
# student=input('enter the marks obtained:')
# if student>='33':
#     print('passed')
#     if student>='90':
#         print(f"your grade is A+")
#     elif student>='80':
#         print('your grade is A')
#     elif student>='70':
#         print('your grade is B+')
#     elif student>='60':
#         print('your grade is B')
#     elif student>='50':
#         print('your grade is C')
#     elif student>='40':
#         print('your grade is D')
#     else:
#        print('your grade is P')
# else:
#     print('failed') 

# # WAP to check the data is multidata or single if multi check it len and print it is even or odd.
# data=eval(input('enter your data: '))
# if type(data) in [str,tuple,list,dict,set]:
#     if len(data)%2==0:
#         print('it is a evem multidata type. ')
#     else:
#         print('it is a odd multidata type. ')
# else:
#     print('it is a single data type. ')
    

# # WAP to print the value as it is only of the length of value is even.
# value=int(input('enter the value of list of your choice: '))
# length = len(value)
# if length % 2 == 0:
#     print("The length is even. Output:", value)
# else:
#     print("The length is odd, so nothing is printed.")

# # 1) WAP to reverse the given number using while loop 
# # num = 123
# # output=321
# num=int(input('enter the number: '))
# value=0
# while num>0:
#     i=num%10
#     value=(value*10)+i
#     num=num//10
# print(value)


# # 2) WAP to find the sum of an individual number
# # ṇum = 5641
# # output = 5+6+4+1=16

# num=int(input('enter the number: '))
# value=0
# while num>0:
#     i=num%10
#     value=value+i
#     num=num//10
# print(value)

# # 3) WAP to find the product of even individual digit in a given integer.
# # num=1825
# # output=8*2=16

# num=int(input('enter the number: '))
# value=1
# while num>0:
#     i=num%10
#     if i%2==0:
#         value=value*i
#     num=num//10
# print(value)


# # 4) WAP to find the sum of the odd index values in an individual digit.
# # num = 123456 
# # output = 2+4+6=12

# num=int(input('enter the number: '))
# l=len(str(num))-1
# value=0
# while num>0:
#     i=num%10
#     if l%2==1:
#         value=value+i
#     num=num//10
#     l=l-1
# print(value)

# # 5) WAP to find the sum of n natural number.

# num=int(input('enter the number: '))
# value=0
# i=1
# while num>=i:
#     value=value+i
#     i=i+1
# print(value)


# # 6) WAP to find the product of n natural numbers (factorial program) 


# num=int(input('enter the number: '))
# value=1
# i=1
# while num>=i:
#     value=value*i
#     i=i+1
# print(value)

# # Print numbers from 10 to 1 (reverse order)
 
# i=10
# while 0<i:
#     print(i)
#     i-=1


# # print the binary value of the integer.

# num=int(input('enter the number: '))
# binary=' '
# while 0<num:
#     rem=num%2
#     binary=str(rem)+binary
#     num=num//2
# print(binary)

# # 1) WAP to print every char from the given string 
# i='python'
# while i:
#     print(i[0])
#     i=i[1:]    


# # 2) WAP to extract lowercase chars from the given str
# a=input('enter the string: ')
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i])
#     i=i+1


# # 3) WAP to extract int from the given list 
# l= [4.2,8,6,3+9j,'hello',89]
# i=0
# while i<len(l):
#     if type(l[i])==int:
#         print(l[i])
#     i=i+1


# # 4) WAP to extract uppercase char from the str
# a=input('enter the string: ')
# i=0
# while i<len(a):
#     if a[i].isupper():
#         print(a[i])
#     i=i+1


# # 5) WAP to extract uppercase, lowercase, digits and special char separately into 4 differents output string 
# a=input('enter the string: ')
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(f'{a[i]} is a lowercase' )
#     elif a[i].isupper():
#         print(f'{a[i]} is a uppercase')
#     elif a[i].isdigit():
#         print(f'{a[i]} is a digit')
#     else:
#         print(f'{a[i]} is a special char')
#     i=i+1


# # 6) find the sum of integers in the given list.
# l= eval(input('enter the list: '))
# i=0
# total=0
# while i<len(l):
#     if type(l[i])==int:
#        total=total+l[i]
#     i=i+1
# print(total)


# # 7) find the product of all the float numbers present at odd position in a given tuple.
# l= eval(input('enter the tuple: '))
# i=0
# while i<len(l):
#     if type(l[i])==float:
#         print(l[i])
#     i=i+1


# # 8) to convert all the lowercase char to uppercase char.
# a=input('enter the string: ')
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i].upper())
#     i=i+1

# # 9) convert all uppercase to lower and lower to uppercase.
 
# a=input('enter the string: ')
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i].upper())
#     elif a[i].isupper():
#         print(a[i].lower())
#     i=i+1


# # WAP to check whether given number is armstrong or not using while loop.
# # armstrong_num =153
# # concept to check - len(153) => 3
# #                     1**3+5**3+3**3=> 153
                    
# num=int(input('enter the number: '))
# number=num
# l=len(str(num))
# total=0
# while num>0:
#     sqr=num%10
#     total=total+(sqr**l)
#     num=num//10 
# if number==total:
#     print('it is a armstrng.')
# else:
#     print('it is not a armstrong. ')
    
    
# # WAP to remove the duplicate from the given list without typecasting.
# a=[10,20,40,10,20,52,58]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)  


# # WAP to print 'A' to 'z' in the list format.

# i='A'
# b=[]
# while i<='Z':
#     if i not in b:
#         b.append(i)
#     i=chr(ord(i)+1)
# print(b)  

# # WAP to check the given number is strong number or not.
# # n=145 => 1!+4!+5!

# num= int(input('enter the number: '))
# temp=num
# total=0
# while temp>0:
#     digit=temp%10
#     fact =1
#     i=1
#     while i<=digit:
#         fact=fact*i
#         i=i+1
#     total=total+fact
#     temp=temp//10
# if total == num:
#     print(f"{num} is a Strong Number")
# else:
#     print(f"{num} is NOT a Strong Number")


# # WAP to print 'z' to 'a'.

# i='z'
# while i>='a':
#     print(i,end=' ')
#     i=chr(ord(i)-1)

# # WAP to print fabonacci series till a number.
# # 0 1 1 2 3 5 8 13 21 ...................n

# l= int(input('enter the num '))
# a,b=0,1
# i=0
# while i<=l:
#     print(a,end=' ')
#     a,b=b,a+b
#     i=i+1

# # WAP to print the below pattern 
# # 1
# # 2 2
# # 3 3 3 
# # 4 4 4 4 
# # 5 5 5 5 5
# # 6 6 6 6 6 6

# l=int(input('enter the number: '))
# i=1
# while i<=l:
#     a = (str(i)+' ')*i
#     print(a)
#     i=i+1
 