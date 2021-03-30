import os

searchfor_in = input("Endswith: ")
path_in = input("Path: ")

path_list = path_in.split(" ")
searchfor_list = searchfor_in.split(" ")

logfile = open("Result.txt", 'w')
logfile.writelines("Searching for: " + searchfor_in + "\n")
logfile.writelines("In: " + path_in + "\n")
for path in path_list:
    for dirs, subdirs, filenames in os.walk(path):
        for filename in filenames:
            fullpath = dirs + os.sep + filename
            for searchfor in searchfor_list:
                if str(filename).endswith(searchfor):
                    logfile.write(os.path.abspath(fullpath) + "\n")
                    print(os.path.abspath(fullpath))

logfile.close()
input("Done")
