# Write an expression to print "gnimmargorp" using slicing only.
# s = "programming"
# print(s[::-1])


# Extract "etmre" using slicing and indexing only.
# s = "intermediate"
# print(s[-1:-3:-1]+s[-7:-10:-1])



# Get "HTO" using negative indexing and step slicing.
# s = "PYTHONISTA"
# print(s[-7:-8:-1]+s[-8:-9:-1]+s[-6:-7:-1])


# Write a single expression to remove first and last character, then reverse the result.
# s="development"
# print(s[-2:-11:-1])



# Get "kigeca" using step slicing.
# s = "abcdefghijk"
# print(s[::-2])



# Extract every second character from the middle section only (ignore first and last character).
# s = "mississippi"
# print(s[2:11:2])
# Right Answer: print(s[1:-1:2]) (Outputs: isisp)


# Extract "SCIENCE" using dynamic slicing with len().
# s = "COMPUTERSCIENCE"
# print(s[8:len(s)]) RIght answer
# print(s[8:15:1])
# s=s[8:15:1]
# print(len(s))


# Write an expression to print characters from index 2 to second-last index in reverse order.
# s = "character"
# print(s[7:1:-1])


# Extract "clpe" using multi-step slicing (example style: s[1:-1][::-1]).
# s = "encyclopedia"
# print(s[4:6:1]+s[7:9:1])




# Write an expression that prints the string except the last 3 characters using len() dynamically.
# s = "datastructure"
# print(s[:len(s)-3])
# print(s[:10:1])
# print(len(s))


# Extract [70, 50, 30, 10] using slicing only.
# lst = [10, 20, 30, 40, 50, 60, 70]
# print(lst[-1::-2])




# Get [8,6,4,2] using negative indexing and step slicing.
# lst = [1,2,3,4,5,6,7,8,9]
# print(lst[-2::-2])





# Write expression to remove first two and last element using slicing only.
# lst = [5,10,15,20,25,30]
# print(lst[2:5:1])




# Extract ['f','d','b'] using reverse step slicing.
# lst = ['a','b','c','d','e','f','g']
# print(lst[-2::-2])






# Extract middle 4 elements dynamically using len().
# lst = [100,200,300,400,500,600]
# print(lst[1:5:1])
# print(lst[1:len(lst)-1]) Right answer




# Extract [7,5,3] using slicing only.
# lst = [9,8,7,6,5,4,3,2,1]
# print(lst[2:7:2])


# Write an expression to reverse list except first element.
# lst = ['p','y','t','h','o','n']
# print(lst[-1:-5:-1])
# Right Answer: print(lst[-1:0:-1]) or simply print(lst[:0:-1])




# Extract elements from index 1 to second-last index and reverse them in a single expression.
# lst = [11,22,33,44,55,66,77,88]
# print(lst[-2:-8:-1])





# Using dynamic slicing with len(), extract [8,10,12].
# lst = [2,4,6,8,10,12,14]
# print(lst[3:len(lst)-1]) Right answer
# print(lst[3:6:1])




# Write a multi-step slicing expression that removes first and last elements, then selects every second element from the remaining list.
# lst = ['A','B','C','D','E','F','G','H']
# print(lst[-2:-8:-1])
# Right Answer: print(lst[1:-1][::2]) (Outputs: ['B', 'D', 'F'])



# Question 1: The "Ghost" Slice
# Predict exactly what this code will print, and explain why it does that.

# Python
# lst = [10, 20, 30, 40, 50, 60, 70]
# print(lst[-2:-6:1])
# this will provide the syntax error because 



# Question 2: The Odd-Jump Extraction
# Write a single slicing expression (no concatenation!) to extract the exact string "geca" from the variable below.

# Python
# s = "a-b-c-d-e-f-g"

# Your code here:






# Question 3: The List Mutilator (Slice Assignment)
# Predict what the list lst will look like after this slice assignment executes.

# Python
# lst = [1, 2, 3, 4, 5, 6, 7]
# lst[1:6:2] = [99, 88, 77]

# What is the output of print(lst)?
# Question 4: The Ultimate Dynamic Slice
# You have a list of an unknown length, but you know the length is always an odd number greater than 3. Write a single dynamic slicing expression using len() to extract the exact middle three elements.
# (Hint: You will need to use integer division // inside the brackets!)

# Python
# Example 1: lst = [1, 2, 3, 4, 5] -> should output [2, 3, 4]
# Example 2: lst = [10, 20, 30, 40, 50, 60, 70] -> should output [30, 40, 50]

# Your dynamic expression here:
# print(lst[???])

