a=0
count=0
while True:
    try:
        num=input("enter the number")
        if num == "done":
            break
        if count == 0:
            max_number = int(num)
            min_number = int(num)
        else:
            if int(num) > max_number:
                max_number = int(num)
            elif int(num) < min_number:
                min_number =int(num)
        a += int(num)
        count +=1
    except:
        print("invalid input")
print("Max number: {0} , Minimum number: {1} ".format(max_number, min_number))
