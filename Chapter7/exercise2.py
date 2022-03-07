#Requesting for input of file name
file_to_read = input("Please enter file name: ")
#Initializing sum of the floats
sum = 0
#Intializing total count of lines that start with X-DSPAM-Confidence
count = 0
with open(file_to_read) as file:
    for line in file:
        #Looking for lines that specifically start with X-DSPAM-Confidence and obtaining only the floats
        #To add them to the sum and count how many they are
        if line.startswith("X-DSPAM-Confidence"):
            index_of_colon_character = line.find(":")
            sum += float(line[index_of_colon_character + 1:])
            count += 1
print(f"Average spam confidence: {(round((sum/count), 5))} ")
