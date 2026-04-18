#Wap to check whether a given number is even or not?

# even=int(input('enter the number: '))
# if even%2==0:
#     print(f'{even} is a even number. ')
# else:
#     print(f'{even}is not a even number.')



#WAP to check whether the given data is mutable or not?

# data=eval(input('enter the data: '))
# if type(data)==list or type(data)==set or type(data)==dict:
#     print(f"the {data} is mutable")
# else:
#     print(f'the {data} is immutable.')


#WAP to check whether the given char is digit or not ?

# char=eval(input('enter the charater:'))
# if type(char)== int or type(char)== float:
#     print(f'{char} is a digit')
# else:
#     print(f"{char} is not a digit")


#WAP to check the list is consist of middle value or not if it having middle value in it so extract it.

# data=eval(input('enter the list:'))
# if len(data)%2!=0:
#     print('the middle value of the list is',data[len(data)//2])
# else:
#     print('It has no middle value.')


#WAP to check whether the two values are pointing to same address or not ?

# a=eval(input('enter the 1 value: '))
# b=eval(input('enter the 2 value: '))
# if a is b:
#     print('it has same address')
# else:
#     print("it has not same address")




#consider the given tuple is of len 2, then check both the data are homogeneous or heterogeneous.

# a = eval(input('enter the number'))
# if type(a[o])==type(a[1]):
#     print('it is a homogeneous')
# else:
#     print('it is hetrogeneous')
    

#WAP to check whether a a given number is positive or negative .
# a = eval(input('enter the number'))
# if -1<a:
#     print('it is a positive number')
# else:
#     print('it is negative number')
    
    
    
# WAP to check the string is palindrome or not ? 
# a=input('enter the number:')
# if (a[::1])==(a[::-1]):
#     print("the number is palindrome")
# else:
#     print('it is not palindrome.')
    
        
 #prove triangle nested    
# a=4
# b=5
# c=7
# if a+b>c:
#     print('it is a traingle')
#     if a==b==c:
#         print('Equilateral')
#     elif a==b or b==c or c==a:
#         print('Isosceles')
#     elif a!=b and b!=c or c!=a:
#         print('scalene')
# else:   
#     print('not a traingle')


# l=[1,2,3,4,5,6,7,8] 
# a=int(input('enter the number: '))
# b=a+1
# c=len(l)-a
# l=l[-1:-b:-1]+l[:c:1]
# print(l)
 
 
# l=eval(input('enter the list: '))
# num=int(input('enter the number: '))
# num=num%len(l)
# l[-num::]
#[5,6,7,8] 
#l[:num]
#[1,2,3,4]
#[5,6,7,8]+[1,2,3,4]
#[5,6,7,8,1,2,3,4]
# print(l[-num::]+l[:-num])




# l=eval(input('enter the list: '))
# l=l[::3][::-1]
# print(l)



# Reverse Without Slicing

# Take a number as input and reverse it using only while loop.
# Example:
# Input: 1234
# Output: 4321

# num= int(input('enter the number: '))
# rev=0
# while num >0:
#     i=num%10
#     rev=(rev*10)+i
#     num = num // 10
# print(rev)
    
    
# Question 1: Print Numbers 1 to 10
# Using only while loop.
# Expected Output:
# 1 2 3 4 5 6 7 8 9 10

# i=0
# while i<=10:
#     print(i)
#     i=i+1


# Question 2: Sum of Numbers from 1 to N
# Take input n.
# Example:
# Input: 5
# Output: 15
# Because:
# 1 + 2 + 3 + 4 + 5 = 15

# n=int(input('enter the number: '))
# i=1
# total=0
# while i<=n:
#     total=total+i
#     i=i+1
#     print(total)

# Question 3: Count Digits of a Number
# Input: Enter number: 48293
# Output: 5
# Rules: # Do NOT convert to string  # Do NOT use len()

# n=input('enter the number: ')
