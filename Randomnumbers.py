import random
attempts = 1
print("enter a maximum number :")
max_number = int(input())
random_number = random.randint(0, max_number)
while True:
    print("Enter your guess:")
    guess = int(input())
    if guess < random_number:
        print("your number is smalller than the random number.")
        attempts += 1
    elif guess > random_number:
        print("your nummber is greater than the radnom number ")
        attempts += 1
    else:
        print("bravo:")
        print("your needed", attempts, "treis!")
        break
max_attempts = int(input())