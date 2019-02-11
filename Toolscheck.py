import os
os.chdir('../Users/Manika/Desktop/jenkins') #Changing the path to the desired location
filelist = os.listdir() #retrieving the files present in the path
#list of variables used for checking Tools type
stage_artifact = 0
maven = 0
jdk = 0
gradle = 0
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
                        line = line.lower()
                        #breaking lines into words and checking with the appropriate words needed
                        for word in line.split():
                                if(word == "maven"):
                                        maven = maven + 1
                                elif(word == "gradle"):
                                        gradle = gradle + 1
                                elif(word == "jdk"):
                                        jdk = jdk + 1


print("Maven commands = ", maven)
print("JDK commands = ", jdk)
print("Gradle = ", gradle)
