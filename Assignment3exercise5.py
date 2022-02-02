try:
    number_of_guests = int(input("Enter number of guests: "))
    if(0 <= number_of_guests <= 50):
        print("$4,000")
    elif(50 < number_of_guests <= 100):
        print("$10,000")
    elif(100< number_of_guests <=200):
        print("$15,000")
    elif(number_of_guests > 200):
        print("$20,000")

    else:
        print("Get serious")
except:
    print("Write whole numbers.")