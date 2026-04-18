# while loop = execute some code WHILE some condition remains true

# age = int(input("Enter your age: ") )

# while age < 0:
#    print("Age can't be negative")
#    age = int(input("Enter your age: "))   
#                                      // this line is used to stop the while loop. 
#                                      // this line is written again because of this.
#                                      // the user gets the chance to stop the looop.                                

# print(f"You are {age} years old")



# WAP number from 1 to 10.
# i=1
# while i<=10:
#     print(i)
#     i=i+1



# WAP to print the squares values between 20 to 50.
# i=20
# while i<=50:
#     print(i**2)
#     i=i+1

# WAP to print the values like 7x1=7..........7x10=70.
# data=int(input('enter the values: '))
# i=1
# while i<=10:
#     print(f'{data}x{i}={i*data}')
#     i=i+1

# WAP to print the even numbers with in the range of 1 to 100.
# i=0
# while i<=100:
#     print(i)
#     i=i+2

# WAP to print the odd number betweeen the range of 1 to 10.
# i=1
# while i<=100:
#     print(i)
#     i=i+2

# WAP to print values 10 to 1.
# i=10
# while i>=0:
#     print(i)
#     i=i-1

# WAP to print the sum of all the values with in the range of 1 to 20.
# i = 1
# n = 0
# while i <= 20:
#     n = n + i
#     i = i + 1
# print(n)
    
    
# WAP to print the product of all odd the numbers in between the range of 1 to 20.
# i = 1
# n = 1
# while i <= 20:
#     n = n * i
#     i = i + 2
# print(n)


# low = 1
# high = 100
# target = 15

# while low <= high:
#     # Use // for integer division to avoid decimals
#     mid = (low + high) // 2

#     if mid == target:
#         print(f"Target found at: {mid}")
#         break
#     elif mid < target:
#         low = mid + 1
#     else:
#         high = mid - 1
