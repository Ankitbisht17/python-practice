# # Q26. Write a program to convert Binary to Decimal. 
# a=int(input('enter the binary number: '))
# num=0
# i=0
# while a>0:
#     digit=a%10
#     num=num + (digit*(2**i))
#     a//=10
#     i+=1
# print(num)
 
 
# Q27. Write a program to check whether a number is palindrome or not. 
# a=int(input('enter the number: '))
# org=a
# num=''
# while a>0:
#     digit=a%10
#     num=num+str(digit)
#     a//=10
# if org == int(num):
#     print('it is the palindrome.')
# else:
#     print('it is not a palindrome. ')

 
# Q28. Write a python program  to sum the sequence: 
# 1 + 1/1! + 1/2! + 1/3! + ........ + 1/n! 
# a=int(input('enter the number: '))
# i=1
# num=1
# num1=1
# while i<=a:
#     num1*=i
#     num+=1/num1
#     i+=1
# print(num)
 
# Q29. Write a program to accept 10 numbers from the user and display it’s average 
# num=0
# i=1
# while i<=10:
#     a=int(input('enter the number: '))
#     num=num+a
#     avg=num/10
#     i+=1
# print(avg)
 
 
# Q30. Write a program to accept 10 numbers from the user and display the largest & smallest 
# number number. 
# a=int(input('enter the number: '))
# largest= a
# smallest = a
# i=1
# while i<=9:
#     a= int(input('enter the number: '))
#     if largest < a:
#         largest=a
#     if smallest > a:
#         smallest=a
#     i+=1
# print('the smallest is ',smallest)
# print('the largest is ',largest)

 
# Q31. Write a program to display sum of odd numbers and even numbers separately that fall 
# between two numbers accepted from the user.(including both numbers) using while loop. 
# n=int(input('enter the first number : '))
# a=int(input('enter the second number: '))
# num=0
# num1=0
# while n<=a:
#     if n%2==0:
#         num=num+n
#     else:
#         num1=num1+n
#     n+=1
# print("the sum of even numbers is ",num)
# print('the sum of odd number is ',num1)



# Q32. Write a program to display all the numbers which are divisible by 13 but not by 3 
# between 100 and 500.(exclusive both numbers) 
# a=100
# b=500
# while a<=b:
#     if a%13==0 and a%3!=0:
#         print(a)
#     a+=1
 
 
 
 
# Q33. Write a program to print the following series till n terms. 
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms 
# a=int(input('enter the number: '))
# org=2
# i=1
# b=''
# while i<a:
#     digit=org%10
#     b=b+str(digit)
#     print(b,end=' , ')
#     i+=1
    

     
# Q34. Write a program to print the following series till n terms. 
# 1 4 9 16 25 _ _ _ _ _ n terms. 
# a=int(input('enter the number: '))
# i=1
# while i<=a:
#     num=i**2
#     print(num,end=' ')
#     i+=1

 
# Q35. Write a program to find the sum of the following series(accept values of x and n from 
# user) 
# 1 + x/1! + x2/2! + ..........xn/n! 
# n=int(input('enter the number of series: '))
# x=int(input('enter the number of x: '))
# i=1
# num=1
# total=1
# while i<=n:
#     num*=i
#     num1=(x**i)/num
#     total+=num1
#     i+=1
# print(total)

 
# Q36. Write a program to find the sum of following series : 
# x + x2/2 + ..........xn/n 
# a=int(input('enter the number: '))
# x=int(input('enter the value of x: '))
# i=1
# b=0
# while i<=a:
#     num=(x**i)/i
#     b+=num
#     i+=1
# print(b)

 
# Q37. Write a program to find the sum of following series 
# 1 + 8 + 27 ............n terms 
# n=int(input('enter the number: '))
# i=1
# num1=0
# while i<=n:
#     num=i**3
#     num1=num1+num
#     i+=1 
# print(num1)
 
 
 
# Q38. Write a program to find the sum of following series: 
# 1 + 2 + 6 + 24 + 120 . . . . . n terms 
# n=int(input('enter the number: '))
# i=1
# num=1
# num1=0
# while i<=n:
#     num=num*i    
#     num1=num1+num
#     i+=1
# print(num1)

 
# Q39. Write a program to find the sum of following series: 
# S = 1 + 4 – 9 + 16 – 25 + 36 – ... ... n terms 
# n=int(input('enter the number: '))
# i=1
# total=0
# while i<=n:
#     num=i**2
#     if num%2==1:
#         total-=num
#     else:
#         total+=num
#     i+=1
# print(total)

 
# Q40. Write a Program to print all the characters in the string ‘PYTHON’ using while loop. 
# s='PYTHON'
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1
 

# Q41. Write a program to print only odd numbers from the given list using while loop. 
# L = [23, 45, 32, 25, 46, 33, 71, 90]
 
# l= [23, 45, 32, 25, 46, 33, 71, 90] 
# i=0
# while i<len(l):
#     if l[i]%2!=0:
#         print(l[i])
#     i+=1

 
# Q42. Write a program to print all the factors of a number using while loop. 
# n=int(input('enter the number: '))
# i=1
# while i<=n:
#     if n%i==0:
#         print ('Remainder 0 ',i)
#     i+=1
 
 
 
 
# Q43. Write a python program to get the following output 
# 1—–49 
 
# 2—–48 
 
# 3—–47 
# ... 
# ... 
# 48—–2 
 
# 49—–1 
 
# n=int(input('enter the number: '))
# i=1
# j=49
# while i<=n:
#     print(i,'--',j)
#     i+=1
#     j-=1
 
 
# Q44.Write a program to extract all the upper case character from the given string 
# s=input("enter the string: ")
# i=0
# while i<len(s):
#     if s[i].isupper():
#         print(s[i])
#     i+=1
 
 
# Q45.Write a Program to separate positive and negative number from a list. 
# s = eval(input('enter the list: ')) 
# i=0
# a=[]
# b=[]
# while i<len(s):
#     if s[i]<=0:
#         b.append(s[i])
#     else:
#         a.append(s[i])
#     i+=1
# print('the positive number are: ',a)
# print('the negative number are: ',b)
 
 
# Q46.Write a program that appends the type of elements from a list. 
# n = [23, 'Python',23.98] 
# i=0
# a=[]
# while i<len(n):
#     item=type(n[i])
#     a.append(item)
#     i+=1
# print(a)
 
 
# Q47. Write a program to fetch only even values from a dictionary. 
# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 } 

# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 } 

# # 1. Grab all the keys and turn them into a list we can count through
# keys_list = list(dic.keys()) 

# # 2. Prepare the empty basket
# even_values = []
# i = 0

# # 3. The Assembly Line
# while i < len(keys_list):
    
#     # Grab the current key (the locker name tag)
#     current_key = keys_list[i] 
    
#     # Open the locker to look at the number inside
#     current_value = dic[current_key] 
    
#     # 4. The Split Test (Is it even?)
#     if current_value % 2 == 0:
        
#         # 5. The Collection
#         even_values.append(current_value)
        
#     i += 1

# print("The even values are:", even_values)
 
 
 
# Q48.Write a program to extract all the string data items from the given list only 
# if string is palindrome 
# n=eval(input('enter the list: '))
# i=0
# a=[]
# while i<len(n):
#     if type(n[i])==str:
#         a.append(n[i])
#     i+=1
# j=0
# b=[]
# while j<len(a):
#     if a[j][::-1]==a[j]:
#         b.append(a[j])
#     j+=1
# print(b)
 
 
 
 
# Q49.Write a program to extract all the special characters from the given string 
# s=input('enter the string: ')
# i=0
# a=''
# while i<len(s):
#     if not 'a'<=s[i]<='z' and not 'A'<=s[i]<='Z' and not '0'<=s[i]<='9':
#         print(s[i],end=' ')
#     i+=1
 
 
# Q50.Write a program to extract all the upper case character ,lower case 
# character ,numbers and special characters into four different output variables 
# from the given string 
# s=input('enter the string: ')
# i=0
# a=' '
# b=' '
# c=' '
# d=' '
# while i<len(s):
#     if s[i].isupper():
#         a+=(s[i])
#     elif s[i].islower():
#         b+=(s[i])
#     elif s[i].isdigit():
#         c+=(s[i])
#     else:
#         d+=(s[i])
#     i+=1
# print('the upper characters are: ',a)    
# print('the lower characters are: ',b)    
# print('the digit characters are: ',c)    
# print('the speical characters are: ',d)    
    