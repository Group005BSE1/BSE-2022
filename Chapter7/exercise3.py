#Requesting for input of file name
file_to_read = input("Please enter file name: ")
if file_to_read == "na na boo boo":
    print(f"{file_to_read.upper()} - You have been punk'd!")
else:
    try:
        with open(file_to_read) as file:
            print(f"There were {len(file.readlines())} subject lines in {file_to_read}")
    except:
        print(f"File cannot be opened: {file_to_read}")