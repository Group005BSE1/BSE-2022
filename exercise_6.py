def computepay(hours , rate):
    if(hours >40):
        print((40 * rate) + ((hours-40)*1.5* rate))
    else:
        print(hours*rate)

a = float(input("Enter Hours: "))
b = float(input("Enter Rate: "))

computepay(a , b)
