import random
user_val = 0
generate_val = random.randint(1, 100)
# print(generate_val)
while user_val != generate_val:
    user_val = eval(input("Enter a number:"))
    if user_val < generate_val:
        print("Sorry,the value is too low")
    elif user_val == generate_val:
        print("Hurray !! The value is equal")
    else:
        print("Sorry, the value is too High")
