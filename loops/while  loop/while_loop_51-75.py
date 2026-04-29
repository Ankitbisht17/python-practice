# Q51.Write a program to get the following output - 
  
 
# Q52.Write a program to convert all the lower case charater to upper case 
# characters present in a given string 
# n=input('enter the string: ')
# i=0
# new=''
# while i<len(n):
#     if 'a'<=n[i]<='z':
#         new=new+n[i].upper()
#     else:
#         new=new+n[n]
#     i+=1
# print(new)

 
# Q53.Write a program to convert all the lower case character to upper case 
# character and upper case character to lower  case character by keeping number 
# and special character as it is 
# n=input('enter the string: ')
# i=1
# new=''
# while i<len(n):
#     if n[i].isupper():
#         new+=n[i].lower()
#     else:
#         new+=n[i].upper()
#     i+=1
# print(new)

 
# Q54.Write a program to extract all the lower case character from the given 
# string only if its ascii value is even 
# n=input('enter the string: ')
# i=0
# new=''
# while i<len(n):
#     if 'a'<=n[i]<='z':
#         if ord(n[i])%2==0:
#             new+=n[i]
#     i+=1
# print(new)
            

 
# Q55.Write a program to get the following output 
#        input=’abcd’ 
#        output={‘a’:97,’b’:98,’c’:99,’d’:100} 
# n=input('enter the string: ')
# i=0
# new={}
# while i<len(n):
#     a=n[i]
#     b=ord(a)
#     new[a]=b
#     i+=1
# print(new)
    
 
# Q56.Write a program to get the following output 
#        input=’hello’ 
#        output={0:’h’ , 1:’e’ , 2:’l’ , 3:’l’ , 4:’o’} 
# n=input('enter the string: ')
# i=0
# new={}
# while i<len(n):
#     a=i
#     b=n[i]
#     new[a]=b
#     i+=1
# print(new)
 
# Q57.Write a program to get the following output 
#        input=['hai' , 89 ,3.4 , 'hello' , 90 , 'py'] 
#        output={‘hai’:’hi’ , ‘hello’:’ho’ , ‘py’:’py’} 
# n=eval(input('enter the list: '))
# i=0
# dict={}
# while i<len(n):
#     if type(n[i])==str:
#         a=n[i]
#         b=a[:1:1]+a[-1:-2:-1]
#         dict[a]=b
#     i+=1
# print(dict)
 
# Q58.Write a program to get the following output 
#        input=‘hai hello’ 
#        output=’olleh iah’ 
# a=input('enter the string: ')
# i=0 
# while i<len(a):
#     n=a[i]
#     b=a[::-1]
#     i+=1
# print(b)
    
 
# Q59.write a program to count the number of vowels present in a given string 
# n=input('enter the string: ')
# i=0
# count=0
# while i<len(n):
#     if n[i] in 'AEIOUaeiou':
#         count+=1
#     i+=1
# print(count) 
 
 
# Q60.Write a program to get the following output 
#        input=‘hai hello good morning’ 
#        output={‘hai’:’a’ , ‘hello’: ‘l’ , ‘good’:’gd’ , ‘morning’:’n’} 

# n = input('enter the string: ')
# n += " " 
# i = 0
# dict = {} 
# a = "" 
# while i < len(n):
#     if n[i] != " ":
#         a += n[i] 
#     else:
#         if a != "": 
#             if len(a) <= 3:
#                 b = a[1:2:1]
#                 dict[a] = b                
#             elif len(a) <= 4:  
#                 b = a[0:1:1] + a[3::1]
#                 dict[a] = b                
#             elif len(a) <= 5:
#                 b = a[2:3:1]
#                 dict[a] = b                
#             elif len(a) <= 7:
#                 b = a[3:4:1]
#                 dict[a] = b
#             a = ""  
#     i += 1
# print(dict)
         
# Q61.Write a program to get the following output 
#        input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’] 
#        output=[‘com’ , ’py’ , ‘html’] 
 
         
# Q62.Write a program to get the following output 
#        input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’ , ‘amazon.com’ , ‘text.py’] 
#        output={‘com’:[‘jiocinema’ , ‘amazon’] , ’py’:[ ‘file’ , ‘text’] 
# ,  ‘html’:[‘web’]} 
         
# Q63.Write a program to get the following output(count no of vowels) 
#        input=’hai hello’ 
#        output={‘hai’:2 , ‘hello’:2} 
 
# Q64.Write a program to extract all the string values present in the list collection 
# only if the last character is upper case. Concatenate the extracted output using 
# ‘*’ 
         
 
# Q65.write a program to extract all the list data items present in list collection 
# only if it is having middle value , that value is integer and having even number 
# at start 
         
 
# Q66.Write a program to get the following output 
#        input= ‘just looking like wow’ 
#        output= ‘jusT LOOKING Like a wow’ 
    
# Q67.Program to find the common elements in two sets using a while loop 
# set1 = {1, 2, 3, 4, 5} 
# set2 = {3, 4, 5, 6, 7} 
 
 
# Q68.Program to check if a number is a perfect number or not using while loop 
 
# Q69.Program to find the length of the longest substring without repeating 
# characters in a given string using while loop 
 
 
# Q72.Program to find the maximum and minimum elements in a tuple using while 
# loop 
 
# Q73.Program to find the union, intersection, and difference of two sets using while 
# loop 
# Q74.Program to count the number of occurrences of each character in a string using 
# a dictionary and while loop 
 
# Q75.Write a program to remove duplicate value from collection without converting to set