try:
    a = float(input("Enter Hours: "))
    b = float(input("Enter Rate: "))
    if(a >40):
        print((40 * b) + ((a-40)*1.5* b))
    else:
        print(a*b)

except:
    print("Error, please enter numeric input")
