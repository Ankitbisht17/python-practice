# number Reversal: Write a Python script using a while loop that takes an integer (e.g., 123) and returns it reversed (321).
# (Hint: Use the modulo % and floor division // operators you've been practicing in SQL/Python).

# num=int(input('enter the number: '))
# rev=''
# while num>0:
#     digit=num%10
#     rev=rev+str(digit)
#     num=num//10
# print(rev)



# Modify your previous reversal logic. Instead of reversing the number, \\
    # write a while loop that calculates the sum of all digits in a number.
# Example: Input 125 Output 8 ($1 + 2 + 5 = 8$)

# num=int(input('enter the number: '))
# total=0
# while num>0:
#     digit=num%10
#     total=total+digit
#     num=num//10
# print(total)


# The "Guessed Number" (Input Validation)
# This tests your ability to use while True and the break statement.
# Write a script where:
# A "secret number" is set (e.g., secret = 7).
# The while loop keeps asking the user to guess the number.
# If the guess is correct, print "Correct!" and break the loop.
# If incorrect, print "Try again."

# secret=7
# num=int(input('guess the sceret number: '))
# while num!=secret:
#     num=int(input('guess the sceret number: '))
# else:
#     print('correct')
    
    
# Binary to Decimal Converter


# num=int(input('enter the number to conver it to binary: '))
# binary=''
# while num>0:
#     digit=num%2
#     binary=str(digit)+binary
#     num=num//2
# print(binary)
 
# binary to decimal converter 

# num=int(input('enter the binary number to convert it to decimal number: '))
# binary=0
# power=0
# while num>0:
#     digit=num%10
#     binary=binary+(digit*(2**power))
#     power=power+1
#     num=num//10
# print(binary)
    
# infinteThe "Infinite" Input Average 

# total_sum = 0
# count = 0
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     total_sum += num
#     count += 1
# if count > 0:
#     average = total_sum / count
#     print(f"Total Sum: {total_sum}")
#     print(f"Average: {average}")
# else:
#     print("No numbers were entered.")


# pattern print
# num=int(input('enter the number: '))
# i=1
# while num >=i:
#     print('*'*i)
#     i=i+1

# print ABCD pattern

# num=int(input('enter the number: '))
# i=1
# alpha='A'
# while num>=i:
#     print(alpha*i)
#     alpha=chr(ord(alpha)+1)
#     i=i+1

# print 1234 pattern
# num=int(input('enter the number: '))
# i=1
# a=1
# while num>=i:
#     print(str(a)*i)
#     a=a+1
    # i=i+1

# The "Factorial" Finder
# Example: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.

# num=int(input('enter the number: '))
# value=1
# i=1
# while num>=i:
#     value=value*i
#     i=i+1
# print(value)

     
# s=[1,2,0,9,0,7]
# t=[]
# g=[]
# d=0

# while d<len(s):
#     if s[d] not in t:
#         if s[d]==0:
#             g.append(s[d])
#         t.append(s[d])
#     d+=1
# print(t.append(g))

# while d<len(s):
#     if s[d]==0:
#         t.append(s[d])
#     d+=1
# print(t)


# strin =78545
# num='78545'
# num=input('enter the number: ')
# i=0
# a=list(num)
# b=[]
# while i>len(a):
#     if a[i]>b[i]:
        
s = input("Enter a string of numbers: ")
num_list = []
i = 0
while i < len(s):
    num_list.append(int(s[i]))
    i += 1
unique_nums = list(set(num_list))
unique_nums.sort()
if len(unique_nums) < 2:
    print("Not enough unique numbers to find the second largest.")
else:
    second_largest = unique_nums[-2]
    print(f"The second largest number is: {second_largest}")