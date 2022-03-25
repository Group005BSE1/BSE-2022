def chop(list):
    try:
         first = list[0]
         last = list[-1]
         list.remove(first)
         list.remove(last)
    except:
        print("Please provide a list next time")

def middle(list):
    try:
        return list[1:-1]
    except:
        print("Please provide a list next time")
