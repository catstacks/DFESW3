import pdb

# pdb.run('<a statement>')

# pdb.set_trace()

# a = "aaa"
# b = "bbb"
# c = "ccc"

# final = a + b + c
# print(final)

# a = "aaa"
# b = "bbb"
# c = "ccc"

# def final(var1,var2,var3):
#     pdb.set_trace()
#     return(var1+var2+var3)

# print(final(a,b,c))

#Exercise 1

# user_funds = 10.31
# item_price = 10 #burger

# if item_price < user_funds:
#     print("You have enough money!")
# elif item_price == user_funds:
#     print("You have the precise amount of money")
# else:
#     print("Sorry you don't have enough money")

# Exercise 2

# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))

# Exercise 3

# def is_prime(x):
#     # pdb.set_trace()
#     if x == 2 or x == 3:
#         return True
#     elif x < 2:
#         return False
#     else:
#         for n in range(2, x+1):
#             if x % n == 0:
#                 return False
#             return True
# print(is_prime(17))

# Exercise 4

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])

print(item_list[5])