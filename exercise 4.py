try:
    age = int(input("Enter age: "))
    if(age >= 18):
        print("You can vote")
    elif (0 <= age <= 17):
        print("Too young to vote")
    elif (age < 0):
        print("You are a time traveller")
except:
    print("Enter an integer next time")
