a=0
count=0
c = []
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
        c.append(num)
    except:
        print("invalid input")

print(a, count)
print(max_number, min_number)