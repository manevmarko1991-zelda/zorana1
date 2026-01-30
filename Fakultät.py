a = int(input("Geben Sie a ein: "))

fakultaet = 1

#if a ==0:

# print("Die Fakultät von 0 ist 1")

#else:

for i in range(1, a + 1):

    fakultaet *= i

print(f"Die Fakultät von {a} ist {fakultaet}")