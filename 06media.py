# import OS module
import os

# Get the list of all files and directories
path = "/Users/student/Music"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

for i in range(len(dir_list)):
    print(dir_list[i])

for l in range(len(dir_list)):
    print(str(l) + " " + dir_list[l])

nummer = input("Wählen sie einen Titel")
nummer = int(nummer)
print(dir_list[nummer])

filetoplay = path + "/" + dir_list[nummer]
print(filetoplay)

os.system ("afplay " + filetoplay)

