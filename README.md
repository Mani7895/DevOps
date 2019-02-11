# Course Project

The goal of this course project is to empirically investigate a large number of devops pipeline programs and obtain statistical data that describe the content and patterns in devops pipelines. We have searched and obtained jenkinsfiles pipeline artifacts from open-source repositories on github contains hundreds of pipeline examples and other code artifacts. The result of this investigation is a report that summarizes the data which can be found as Report.pdf in this Repository.


##About 

This project uses JenkinsFiles of repositories from GitHub to analyze the content and patterns in Devops Pipelines.To analyze the Pipeline Artifacts, we have focused on research questions and their answers that were procured after analyzing the obtained Jenkinsfiles. The answers to these questions are documented in the project report : Project Report.pdf 
To analyze the data collected, we have focused on the following research questions:

###1. What are the most and the least frequent operations in pipeline stages?
We Run a Python Script to Parse through all the Jenkinsfiles. This parser parses through the Jenkinsfiles to get the occurrence of the stages and find out which among them occur the least and most frequently.

###2. How often timeout periods are used in the pipeline runs and what are the most frequent intervals?
We use another parser to parse through all the Jenkinsfiles to find out how frequently timeout periods are used. This parser also gives us the most frequent time intervals used in a pipeline.

###3. What tools are the most and the least frequently used in pipelines?
Pipelines support 3 tools : Maven, Gradle and JDK. 
We use a parser to parse through all the collected Jenkinsfiles to find the most and least frequently used Tools.

###4. Which agents are most and least frequently used in pipelines?
Pipelines uses agents like "any" ,none, "node", "label", "docker",etc.
We use a Parser written in python to parse through all the collected Jenkinsfiles to find the most and least frequently used Agents.

## Getting Started
Please Follow Configurations and Installations.md file to configure your system to have the run time environment required by this project.

### Prerequisites
1. Python 3 
2. Java

## Running the Project
Follow the Run.md file to run this project.

## Authors

* **Nishali DMello and Manika Maheshwari** 


