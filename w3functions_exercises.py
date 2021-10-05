# 1. Write a Python function to find the Max of three numbers. 

# def num_max(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y 
#     else:
#         return z       
# print(num_max(5, -7, 2))

# 2. Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7) Expected Output : 20

# def sum_list(terms):
#     total = 0
#     for x in terms:
#         total += x
#     return total    
# print(sum_list((8, 2, 3, 0, 7)))

# 3. Write a Python function to multiply all the numbers in a list. Sample List : (8, 2, 3, -1, 7). Expected Output : -336

# def multiply_list(terms):
#     total = 1
#     for x in terms:
#         total *= x
#     return total    
# print(multiply_list((8, 2, 3, -1, 7)))

# 4. Write a Python program to reverse a string. Sample String : "1234abcd". Expected Output : "dcba4321"

# word = str(input("Input a word to reverse: "))

# def reverse_str(word):
#     for char in range(len(word) - 1, -1, -1):
#         print(word[char], end="")
#         #print("\n")
# print(reverse_str())

# Sample solution below 
# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# 6. Write a Python function to check whether a number falls in a given range. Go to the editor
# Click me to see the sample solution

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# Click me to see the sample solution

# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# Click me to see the sample solution

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# 10. Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
# Click me to see the sample solution

# 11. Write a Python function to check whether a number is perfect or not. Go to the editor
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
# Click me to see the sample solution

# 12. Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# Click me to see the sample solution

# 13. Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

# 14. Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Click me to see the sample solution

# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
# Click me to see the sample solution

# 16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). Go to the editor
# Click me to see the sample solution

# 17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. Go to the editor
# Click me to see the sample solution

# 18. Write a Python program to execute a string containing Python code. Go to the editor
# Click me to see the sample solution

# 19. Write a Python program to access a function inside a function. Go to the editor
# Click me to see the sample solution

# 20. Write a Python program to detect the number of local variables declared in a function. Go to the editor
# Sample Output:
# 3
# Click me to see the sample solution

# 21. Write a Python program that invoke a given function after specific milliseconds. Go to the editor
# Sample Output:
# Square root after specific miliseconds:
# 4.0
# 10.0
# 158.42979517754858
# Click me to see the sample solution