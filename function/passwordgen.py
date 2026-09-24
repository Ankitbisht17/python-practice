import random
Alpha=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f',
 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l',
 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
 'Y', 'y', 'Z', 'z']
number=[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
print("Welcome to the password generator. ")
alp=int(input("how many letters would you like to have in your password: "))
num=int(input("how many numbers would you like to have in your password: "))
sym=int(input("how many special characters would you like to have in your password: "))

passw=" "
ran=[]

for alp in range(alp):
    ran.append(random.choice(Alpha))

for num in range(num):
    ran.append(random.choice(number))

for sym in range(sym):
    ran.append(random.choice(symbols))

random.shuffle(ran)

passw = "".join(ran)

# print(ran)
print(f"here is your password:  {passw}")