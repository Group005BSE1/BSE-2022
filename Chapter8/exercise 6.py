list = []
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            number =int(num)
            list.append(number)

    except:
        print("Enter a valid number next time")

print(f"Maximum number: {max(list)} \nMinimum number: {min(list)}")