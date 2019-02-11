import os
os.chdir('../Users/Manika/Desktop/jenkins') #Changing the path to the desired location
filelist = os.listdir() #retrieving the files present in the path
#list of variables used for checking timeout
count_file = 0
for x in filelist:
    count_file = count_file + 1
    if x.endswith(".txt"):
            with open(x, "r") as y:
                for line in y:
                        #replacing delimiters with space
                        line = line.replace("(", " ")
                        line = line.replace("'", " ")
                        line = line.replace("}", " ")
                        line = line.replace("-", " ")
                        line = line.replace(":", " ")
                        line = line.replace(";", " ")
                        line = line.replace(")", " ")
                        line = line.replace("{", " ")
                        line = line.replace("_", " ")
                        line = line.replace(",", " ")
                        word = line.split()
                        length = len(word)
                        #Calculating timeout
                        for i in range(length):
                            if length == 3:
                                if word[i]=="timeout":
                                    print("Timeout = ", word[i + 1], "milliseconds")
                            elif length == 5:
                                if word[i]=="timeout":
                                    print("Timeout = ", word[i + 2], word[i+4])


print("Total files parsed = ", count_file)
