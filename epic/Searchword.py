print("Search a word")
searchword_in = input(":")
print("Show line? y/n")
showline = input(":")
print("Filename")
filename = input(":")
instances = 0

searchword_list = searchword_in.split(", ")

logfile = open('WordSearch.log', 'w')

with open(filename, 'r') as f:
    lines = f.readlines()
    
    count = 0
    for line in lines:
        count += 1
        for searchword in searchword_list:
            if searchword in line or searchword + "\n" in line:
                instances += 1
                if showline == "y":
                    print("Line: " + str(count) + " " + line)
                else:
                    print("Line: " + str(count))
                logfile.write("Line: " + str(count) + " " + line + "\n")
    if instances < 1:
        print("No words found.")
    input()
