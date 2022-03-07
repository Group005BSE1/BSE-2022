with open("mbox-short.txt") as file_to_read:
    for line in file_to_read:
        print(line.upper())