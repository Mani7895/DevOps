import os
os.chdir('../Users/Manika/Desktop/jenkins') #Changing the path to the desired location
filelist = os.listdir() #retrieving the files present in the path
#list of variables used for checking Stages type
stage_build = 0
stage_test = 0
stage_deploy = 0
stage_run = 0
stage_checkout = 0
stage_prep = 0
stage_artifact = 0
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
                                if(word == "build"):
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
        


print("Build commands = ",stage_build)
print("Deploy commands = ",stage_deploy)
print("Test commands = ",stage_test)
print("Run Commands = ", stage_run)
print("Checkout commands = ",stage_checkout)
print("Preparation commands = ",stage_prep)
print("Artifact commands = ", stage_artifact)

