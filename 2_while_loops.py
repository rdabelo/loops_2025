# Given:
# while loops = execute some code while some condition remain true
# name  = input( "enter your name: ")

# if name == "":
#     print(" you did not enter your name")
#     name=input("enter your name: ")
# else:
#     print(f"Hello {name}")

# while name == "":
# age = int(input("Enter your age: "))

# while age < 0:
#     print("age cam't be negative")
#     age = int(input("enter your age: "))

# print(f" You are {age} years old")\

# food = input("Enter a food you like (q to quit): ")

# favorite_foodlist = []

# while not food == "quit":
#     print(f"you like {food}")
#     food = input("enter another food youy would like (q to quit): ")
    
# print ("bye")

# favorite_foodlist.append(food)

num = int(input(" Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"your number is {num}")

colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
