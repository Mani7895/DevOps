#Running the Course Project

After configuring your system and installing the necessary software follow these steps to run our project:

1. Clone this repository to your local files using **git clone  https://ndmello@bitbucket.org/ndmello/nishali_dmello_manika_maheshwari_courseproject.git** in the git folder on your computers command prompt/Terminal
2. Now Run the Cloner.java Java program found at **nishali_dmello_manika_maheshwari_courseproject/Repo/Cloner/src/main/java**
3. This will download repositories to your local storage.
4. Copy the  **".py"** files from the Project Folder into your systems Python Folder.
4. We weren't able to extract the Jenkinsfiles from these repositories programmatically so we copied all the Jenkinsfiles to a new folder called 'Jenkins' which is saved on Desktop.
5. Use this path to this Jenkins Folder when running the following parsers.
6. Now we will use Python to analyze these Jenkins Files for Pipeline Artifacts.
7. Open Command Prompt andUse '''cd''' to enter into the Python Directory on your system.
8. Copy and paste the ".py" from our project to your python directory in the local file storage system.
9. Next Run **python timeoutcheck.py** to get the details of the of the imeout intervals and timeout frequency. .
10. Now run **python agent.py** to get the details of the agents used by the pipelines.
11. Now run **python Stagescheck.py** to get the least and most frequently used Pipeline Operations.
12. Now run **python Toolscheck.py** to get the distrbution of the Pipeline tools in the Jenkinsfiles.
13. Next run **python test.py** this parses through one single Jenkins file and gives all the distributions obtained separately in the above executions for one single file. 
14. Enter the path to the folder where repositories are downloaded.
15. The screen will display the classification of the patches.

