try:
    with open("measles.txt") as file:
        selectedFile = input("Enter file name: ")
        with open(selectedFile , "w" ) as newFile:
            selectedYear = input("Enter year to querry: ")
            for line in file:
                if selectedYear == "" or selectedYear == "all" or selectedYear == "ALL":
                    newFile.write(line)
                if line[88:].startswith(selectedYear):
                    newFile.write(line)
                else:
                    continue
        print(open(selectedFile).read())
except:
    print("File not Found")