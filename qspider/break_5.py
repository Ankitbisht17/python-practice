# prime number 
# n = int(input("Enter number: "))
# if n <= 1:
#     print("is not a Prime number ")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("is not a Prime number")
#             break
#     else:
#         print("it is a Prime number")

# to print the initial index of given char  present in a given string 
s = input("Enter string: ")
ch = input("Enter character: ")
for i in range(len(s)):
    if s[i] == ch:
        print("Index:", i)
        break
else:
    print("Character not found")