unique_words = []
checked_list = []

with open("romeo.txt") as work_file:
    for line in work_file:
        unique_words += line.split()

        for word in unique_words:
            if word in checked_list:
                continue
            else:
                checked_list.append(word)

checked_list.sort(key = str.lower)
print(checked_list)