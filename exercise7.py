Amount = input("Enter an amount to make change for: ")
a = float(Amount)
print("    ")
print("Your change is")

if a >= 20:
    print(str(int(a // 20)) + " Twenties")
else:
    print("0 Twenties")
a = a % 20
if  a >= 10:
    print(str(int(a // 10)) + " Tens")
else:
    print("0 Tens")
a = a % 10
if a >=5:
    print(str(int(a // 5)) + " fives")
else:
    print("0 fives")
a= a % 5
if a >= 1:
    print(str(int(a // 1)) + " Ones")
else:
    print("0 ones")
a = a - int(a)
if a >= 0.25:
    print(str(int(a//0.25)) + " Quarters")
else:
    print("0 Quarters")
a = a%0.25
if  a >= 0.1:
    print(str(int(a//0.1)) + " Dimes")
else:
    print("0 dimes")
a = a%0.1
if a >= 0.05:
    print(str(int(a//0.05)) + " nickels")
else:
    print("0 nickels")
a = a%0.05
if a >=0.01:
    print(str(int(a//0.01)) + " pennies")
else:
    print("0 pennies")
