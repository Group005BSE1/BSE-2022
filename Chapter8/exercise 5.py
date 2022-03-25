file = input("Please enter file name: ")
verified_emailers = []
count_1 = 0
try:
    with open(file) as emaildata:
        for line in emaildata:
            if line.startswith("From"):
                words_in_line = line.split()
                if words_in_line[0] == "From":
                    verified_emailers.append(words_in_line[1])
                    count_1 += 1
    for i in range(count_1):
        print(verified_emailers[i])
    print(f"\nThere were {count_1} lines in the file that begin with From")
except:
    print("Enter a present file name next time")