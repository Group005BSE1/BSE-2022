try:
    a = input("location: ")
    b = int(input("pay: "))
    if(a == "Mbarara"):
        if(b >= 4000000):
            print("without adoubt,i will take it")
        else:
            print("No thanks, I'll get a better one ")
    elif(a == "Kampala"):
        if(b >= 10000000):
            print("without adoubt,i will take it")
        else:
            print("No thanks, I can find something better.")
    elif(a == "Space"):
        if(b >= 0):
            print("Without adoubt,i will take it")
    else:
        if(b >= 6000000):
            print("Sure, I can work with this")
        else:
            print("No thanks, I'll get a better one ")
except:
    print("Type valid data")
