import os
os.chdir('../Users/Manika/Desktop/jenkins') #Changing the path to the desired location
filelist = os.listdir() #retrieving the files present in the path
#list of variables used for checking Agent type
stage_artifact = 0
anycommand = 0
node = 0
docker = 0
label = 0
none = 0
windows = 0
#Accessing all files with txt format one by one
for x in filelist:
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
                        line = line.lower()
                        #breaking lines into words and checking with the appropriate words needed 
                        for word in line.split():
                                if(word == "docker"):
                                        docker = docker + 1
                                elif(word == "label"):
                                        label = label + 1
                                elif(word == "node"):
                                        node = node + 1
                                elif(word == "any"):
                                        anycommand = anycommand + 1
                                elif(word == "windows"):
                                        windows = windows + 1


print("Any commands = ", anycommand)
print("Node commands = ", node)
print("Label commands = ", label)
print("Docker commands = ", docker)
print("Windows Commands = ", windows)
