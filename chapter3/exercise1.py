a = float(input("Enter Hours: "))
b = float(input("Enter Rate: "))
c = 40
if(a > 40):
    print((c * b) + (1.5 *(a - c) * b))
else:
    print(a * b)