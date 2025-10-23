number1=int(input("Enter your number:"))
number2=int(input("Enter your 2 number:"))


if number2 < number1:
    print( f"{number1} is bigger then number {number2}")
elif number2 == number1:
    print("gleich")
else:
    print(f"{number1} is smaller then number {number2}")
