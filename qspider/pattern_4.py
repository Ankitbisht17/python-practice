# n = 5
# for i in range(1, n+1):
#     for s in range(n - i):
#         print("  ", end="")
#     for j in range(n, n-i, -1):
#         print(j, end=" ")  
#     print()

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        if i % 2 == 0:
            print((num + j) ** 2, end=" ")
        else:
            print(num + j, end=" ")
    num += i
    print()