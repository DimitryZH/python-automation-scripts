inputFile = open("C:/MyCOURCES/DevOps/Projects/python-automation-linkedin/read_files/inputFile.txt", "r")

for line in inputFile:
    line_split = line.split()
    if line_split[1] == "26":
        print(line)
inputFile.close()