sum=0
count=0
while True:
    try:
        num=input("enter the number")
        if num == "done":
            break
        sum+= int(num)
        count +=1
    except:
        print("invalid input")
average = (sum/count)
print(sum, count, average)
