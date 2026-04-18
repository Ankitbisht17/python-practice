# Q1.Write a program to print the following using while loop 
#  First 10 Even numbers 
# a=20
# i=0
# while i<a:
#     print(i)
#     i+=2

# Q2.First 10 Odd numbers 
# a=20
# i=1
# while i<a:
#     print(i)
#     i+=2

# Q3. First 10 Natural numbers 
# a=10
# i=1
# while i<=a:
#     print(i)
#     i+=1

 
# Q4. First 10 Whole numbers 
# a=10
# i=0
# while i<a:
#     print(i)
#     i+=1

# Q5. Write a program to print first 10 integers and their squares using while loop. 
# a=10
# i=1
# while i<=a:
#     print(i**2)
#     i+=1
 
# Q6. Write while loop statement to print the following series: 10, 20, 30 ... ... 300 
# a=300
# i=10
# while i<=a:
#     print(i)
#     i+=10
    
    
# Q7. Write a while loop statement to print the following series 105, 98, 91 .........7. 
# a=7
# i=105
# while i>=a:
#     print(i)
#     i-=7

 
# Q8. Write a program to print the first 10 natural number in reverse order using while loop. 
# a=1
# i=10
# while i>=a:
#     print(i)
#     i-=1
 
 
# Q9. Write a program to print sum of first 10 Natural numbers. 
# a=10
# i=1
# num=0
# while i<=a:
#     num+=i
#     i+=1
# print(num)
 
# Q10. Write a program to print sum of first 10 Even numbers.
# a=20
# i=0
# num=0
# while i<=a:
#     num+=i
#     i+=2
# print(num)

# Q11. Write a program to print table of a number entered from the user. 
# a=int(input('enter the number: '))
# i=1
# while i<=10:
#     num=i*a
#     print(f'{a} X {i} = {num}')
#     i+=1

 
# Q12. Write a program to print all even numbers that falls between two numbers (exclusive 
# both numbers) entered from the user using while loop. 
# a=int(input('enter the number: '))
# b=int(input('enter the number: '))
# while a<b:
#     if a%2==0:
#         print(a)
#         a+=2
#     else:
#         print(a+1)
#         a+=2
        
# Q13. Write a program to check whether a number is prime or not using while loop. 
# a=int(input('enter the number: '))
# i=2
# count=0
# while i<a:
#     if a%i==0:
#         count+=1
#     i+=1
# if count==0 and a>1:
#     print('it is the prime number. ')
# else:
#     print('it is not a prime number. ')
        
        
# Q14. Write a program to find the sum of the digits of a number accepted from the user. 
# a=int(input('enter the number: '))
# num=0
# i=1
# while i<=a:
#     num+=i
#     i+=1
# print(num)

 
# Q15. Write a program to find the product of the digits of a number accepted from the user. 
# a=int(input('enter the number: '))
# num=1
# i=1
# while i<=a:
#     num*=i
#     i+=1
# print(num)
 
 
# Q16. Write a program to reverse the number accepted from user using while loop. 
# a=int(input('enter the number: '))
# num=''
# i=1
# while i<=a:
#     digit=a%10
#     num=num+str(digit)
#     a=a//10
# print(num)
 

 
# Q17. Write a program to display the number names of the digits of a number entered by 
# user, for example if the number is 231 then output should be Two Three One 

# num = input("Enter a number: ")
# i = 0
# while i < len(num):
#     digit = num[i]
#     if digit == '0':
#         print("Zero", end=" ")
#     elif digit == '1':
#         print("One", end=" ")
#     elif digit == '2':
#         print("Two", end=" ")
#     elif digit == '3':
#         print("Three", end=" ")
#     elif digit == '4':
#         print("Four", end=" ")
#     elif digit == '5':
#         print("Five", end=" ")
#     elif digit == '6':
#         print("Six", end=" ")
#     elif digit == '7':
#         print("Seven", end=" ")
#     elif digit == '8':
#         print("Eight", end=" ")
#     elif digit == '9':
#         print("Nine", end=" ")
#     i += 1

 
# Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using 
# while loop. 
# a=int(input('enter the number: '))
# i=0
# j=1
# count=1
# while count<a:
#     print(i,end=' ')
#     next=i+j
#     i=j
#     j=next
#     count+=1    

 
# Q19. Write a program to print the factorial of a number accepted from user. 
# a=int(input('enter the number: '))
# i=1
# num=1
# while i<=a:
#     num*=i
#     i+=1
# print(num)
 
# Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is 
# a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.) 
# a=int(input('enter the number: '))
# num=0
# i=1
# org=a
# while i<=a:
#     digit=a%10
#     num=num+(digit**3)
#     a//=10
# if num==org:
#     print('it is the armstrong number. ')
# else:
#     print('it is not a armstrong. ')

 
# Q21. Write a program to add first n terms of the following series using a while loop: 
# 1/1! + 1/2! + 1/3! + ........ + 1/n! 
# a=int(input('enter the number: '))
# i=1
# num=0.0
# num1=1
# while i<=a:
#     num1*=i
#     num+=1/num1
#     i+=1
# print(num)

 
 
# Q22. Write a program to enter the numbers till the user wants and at the end it should 
# display the sum of all the numbers entered. 
# a=int(input('enter the number: '))
# choice=input('do you want to continue (Y/N): ')
# while choice=='Y'or choice == 'y':
#     b=int(input('enter the number: '))
#     choice=input('do you want to continue (Y/N): ')
#     a+=b
# print("the total sum is ",a)
    
# Q23. Write a program to enter the numbers till the user enter ZERO and at the end it should 
# display the count of positive and negative numbers entered. 
# a=int(input('enter the number (0 to stop): '))
# negative=0
# positive=0
# while a!=0:
#     if a<0:
#         negative+=1
#     else:
#         positive+=1
#     a=int(input('enter the number (0 to stop): '))    
# print('total number of negative numbers are: ',negative)
# print('total number of positive numbers are: ',positive) 


 
# Q24. Write a program to find the HCF of two numbers entered from the user. 
# a = int(input('enter the first number: '))
# b = int(input('enter the second number: '))
# limit = a
# if b < a:
#     limit = b
# i = 1
# hcf = 1  
# while i <= limit:
#     if a % i == 0 and b % i == 0:
#         hcf = i          
#     i += 1
# print('The HCF is:', hcf)


# Q25. Write a program to convert Decimal to Binary.
# a=int(input('enter the number: '))
# i=1
# num=''
# while a>0:
#     digit=a%2
#     num=str(digit)+num
#     a//=2
# print(num)