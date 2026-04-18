# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for counter in range(1, 21):
    # if counter == 13:
    #    break
    # else:
#        print(counter)

# string
# a='this is a string data type. '
# for i in a:
#     print(i)

# list
# l=[1,2,3,4,5,6]
# for i in l:
#     print(i)

# tuple
# l=(1,2,3,4,5,6)
# for i in l:
#     print(i)
    
# set 
# l={1,2,3,4,5,5,4,3,2,1}
# for i in l:
#     print(i)

# dictionary
# l={1:2,3:4,5:5,4:3,2:1}
# for i in l:
#     print(i,l[i])

# numerical values 
# for i in range(1, 11):
#     print(i)

# for counter in range(1, 20,2):
#     print(counter)


# 1)find the length of a given collections without using length function.
# value=input('enter the character: ')
# count=0
# for i in value:
#     count=count+1
# print(count)

# 2)program to extract vowels form the given str.
# value=input('enter the character: ')
# for i in value:
#     if i in 'aeiouAEIOU':
#         print(i)  

# 3)program to replace space by an underscrore in a given str.
# value=input('enter the character: ')
# for i in value:
#     if i== ' ':
#         print(i=='_')
# for i in value:
#     r=value.replace(' ','_')
# print(r)           

# 4)to check whether the given string is palindrome or not without using slicing.
# value=input('enter the character: ')
# for i in value:
#     if 


# 5)extract all the integers which are multiple of 5 and has 3 digits in it from the given list.




# 6)program to remove the duplicate value from the list
# value=eval(input('enter the data: '))
# for i in value:
#     if i ==i:
#         print(i)


# 7)program to get the following output.
#    input = l=[12,2.3,'nice',8+8j,'abcdef',8,'py']
#    output=['nice':4,'abcdef':'6','py':'2']
# l=[12,2.3,'nice',8+8j,'abcdef',8,'py']
# d={}
# for i in l:
#     if type(i)==str:
#         d[i]=len(i)
# print(d) 


# 8)to get the following output
# l={'nice':'ne','abcdef':'af','py':'py'} 
# d={}
# for i in l:
#     if type(i)==str:
#         d[i]=i[0]+i[-1]
# print(d) 

# 9)to get the following output
#    s='AppLe#23'
#    out={'A':'a','p':'P','L':'l','e':'E'}
# s='AppLe#23'
# out = {}
# for char in s:
#     if char.isalpha(): 
#         if char.isupper():
#             out[char] = char.lower()
#         else:
#             out[char] = char.upper()
# print(out)

# 10)To create the string with uppercase character from A to Z.
# for i in range(65, 91):
#        print(chr(i)) 