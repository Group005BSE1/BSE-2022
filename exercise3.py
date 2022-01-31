try:
    a = float(input("Enter marks: "))
    if(0.0 <= a <= 1.0):
        if(a >= 0.9):
            print("A")
        elif(a >= 0.8):
            print("B")
        elif(a >= 0.7):
            print("C")
        elif(a >= 0.6):
            print("D")
        elif(a < 0.6):
            print("F")
    else:
        print("Error, Enter between 0.0 and 1.0")

except:
    print("Not a value")
