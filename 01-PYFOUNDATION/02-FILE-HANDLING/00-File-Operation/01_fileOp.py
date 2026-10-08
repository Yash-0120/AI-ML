# WRITE MODE

file = open("../data.txt", "w")

file.write("Welcome")

file.close()


# APPEND MODE

appendFile = open("../data.txt", "a")

appendFile.write("\nYASH")

appendFile.close()


# READ MODE

files = open("../data.txt", "r")

content = files.read()

# print(content)

files.close()


# PROFESSIONAL WAY

with open("../student.txt", "w") as info:

    info.write("Name: Yash Varpe")
    info.write("\nBranch: Computer Engineering")
    info.write("\nLearning AI/ML")


with open("../student.txt", "r") as studentInfo:

    content = studentInfo.read()

# print(content)


# ------------ readline & readlines -----------------

with open("../student.txt", "r") as details:

    lines = details.readlines()

    # print(details.readline())

print(lines)

# for line in lines:

#     # print(line)