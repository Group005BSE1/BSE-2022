a=0
count=0
while True:
    try:
        num=input("enter the number")
        if num == "done":
            break
        a+= int(num)
        count +=1
    except:
        print("invalid input")
b = (a/count)
print(a, count, b)