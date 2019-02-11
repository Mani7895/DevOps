import os
os.chdir('../Users/Manika/Desktop/jenkins') #Changing the path to the desired location
filelist = os.listdir() #retrieving the files present in the path
#list of variables
stage_artifact = 0
anycommand = 0
node = 0
docker = 0
label = 0
none = 0
windows = 0
count_file = 0
maven = 0
jdk = 0
gradle = 0
stage_build = 0
stage_test = 0
stage_deploy = 0
stage_run = 0
stage_checkout = 0
stage_prep = 0
stage_artifact = 0
#Opening one file in read mode
y = open("jenkinsfile0.txt", "r")
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
        elif(word == "maven"):
            maven = maven + 1
        elif(word == "gradle"):
            gradle = gradle + 1
        elif(word == "jdk"):
            jdk = jdk + 1
        elif(word == "build"):
            stage_build = stage_build + 1
        elif(word == "test"):
            stage_test = stage_test + 1
        elif(word == "deploy"):
            stage_deploy = stage_deploy + 1
        elif(word == "checkout"):
            stage_checkout = stage_checkout + 1
        elif(word == "run"):
            stage_run = stage_run + 1
        elif(word == "preparation"):
            stage_prep = stage_prep + 1
        elif(word == "artifact"):
            stage_artifact = stage_artifact + 1
        elif(word == "maven"):
            maven = maven + 1
        elif(word == "gradle"):
            gradle = gradle + 1
        elif(word == "jdk"):
            jdk = jdk + 1
    words = line.split()
    length = len(words)
    for i in range(length):
        if length == 3:
            if words[i]=="timeout":
                print("Timeout = ", words[i + 1], "milliseconds")
        elif length == 5:
            if words[i]=="timeout":
                print("Timeout = ", words[i + 2], words[i+4])



print("Any commands = ", anycommand)
print("Node commands = ", node)
print("Label commands = ", label)
print("Docker commands = ", docker)
print("Windows Commands = ", windows)
print("Maven commands = ", maven)
print("JDK commands = ", jdk)
print("Gradle = ", gradle)
print("Build commands = ",stage_build)
print("Deploy commands = ",stage_deploy)
print("Test commands = ",stage_test)
print("Run Commands = ", stage_run)
print("Checkout commands = ",stage_checkout)
print("Preparation commands = ",stage_prep)
print("Artifact commands = ", stage_artifact)
print("Total files parsed = ", count_file)
