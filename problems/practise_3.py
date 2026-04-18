# The Problem 1):
#             Write a program that takes a string of letters and "compresses" it by 
#             counting how many times a character appears in a row. You will then build 
#             a new string that shows the character followed by its count.
#             For example:
#                 If the input string is "aaabbc", your code should output "a3b2c1".
#                 If the input string is "xyyzzzz", your code should output "x1y2z4".
#                 Notice that if a character appears only once (like the "c" or "x"), it still gets a "1" next to it.

a = input('enter the character: ')
compressed = ""
count = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        compressed += a[i - 1] + str(count)
        count = 1
compressed += a[-1] + str(count)
print(compressed) 
