#﻿System Used:
 Windows 10, 64-bit, 16 GB RAM 
 Python version 3.6.5
 Java 8

#Installations and Configurations:

## Python:
### Windows: https://www.python.org/downloads/
The Python download requires about 30 Mb of disk space; when installed, Python requires about an additional 90 Mb of disk space.

1.	Download Python version --- from the above link.
2.	Double click on the .exe file and follow suitable installation instructions.
3.	Select a desired location for Python in your Internal Storage when installing.
4.	Open Command prompt.
5.	Use ‘cd’ to navigate to the Python location on the system.
6.	Eg: 

		* C:\Users\Nishali>        (Default Directory/Folder when command prompt is launched)
		* C:\Users\Nishali>cd/  (To exit default directory and open OS directory)
		* C:\>cd Python27         ( Since Python is in OS>Python27 on student computer)
		* C:\Python27>              (Now the user is in Python Directory)

7.	Install a text editor like Sublime Text, Notepad ++ ,etc.
8.	Use the text editor to type in the python script.
9.	Save the script as a ‘.py’ file in the Python Folder. 
10.	Now run the following commands in cmd to install libraries needed in this project that are not present in the downloaded Python file.
11.	‘easy_install pip’
12.	‘pip install GitPython’
13.	‘pip install requests’
14.	‘pip install pygithub3’
15.	‘pip install py-github’
16.	'pip install pygit2'
17. 'pip install pytest'
18. 'pip install patch'
19. 'pip install pandas'

### Mac: https://www.python.org/downloads/release/python-365/
Python comes installed along with OS X, although you can make sure you have the latest version of Python by installing it from the above link.

1.	Double-click the python-3-macosx10.6.pkg file in the Downloads folder.
2.	If you have Gatekeeper enabled, the installation will be blocked. Open System Preferences > Security & Privacy and click Open Anyway.
3.	Click Continue, Agree and Install buttons in the Install Python window.
4.	Open Terminal again and enter python --version. It should now read Python 3.6.5
5.	Open the App Store and search for Xcode.
6.	Click Get > Install.
7.	Now that you've got Python and the Command Line Tools up and running, we should get Homebrew installed. Homebrew is a program used to install packages in OS X (it's the equivalent of apt-get, a command common on Unix and Linux computers).
8.	Open a Terminal window
9.	Cut and paste this command: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
10.	Install a text editor like TextWrangler, Sublime Text or Geddit.
11.	Use the text editor to type in the python script.
12.	Save the script as a ‘.py’ file in the Python Folder. 
13.	Now run the following commands in cmd to install libraries needed in this project that are not present in the downloaded Python file.
14.	‘sudo easy_install pip’
15.	‘sudo pip install GitPython’
16.	‘sudo pip install requests’
17.	‘sudo pip install pygithub3’
18.	‘sudo pip install py-github’
19.	'sudo pip install pygit2'
20. 'sudo pip install pytest'
21. 'sudo pip install patch'
22. 'sudo pip install pandas'

### Linux:
1.	First, install some dependencies:
--‘sudo apt-get install build-essential checkinstall’
--‘sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev’
2.	Then download using the following command:
3.	‘version=3.6.5’
4.	‘cd ~/Downloads/’
5.	‘wget https://www.python.org/ftp/python/$version/Python-$version.tgz’
6.	Extract and go to the directory:
‘tar -xvf Python-$version.tgz’
‘cd Python-$version’
7.	Now, install using the command you just tried, using checkinstall instead to make it easier to uninstall if needed:
--‘./configure’
--‘make’
--‘sudo checkinstall’
8.	Now run the following commands in cmd to install libraries needed in this project that are not present in the downloaded Python file.
9.	‘sudo easy_install pip’
10.	‘sudo pip install GitPython’
11.	‘sudo pip install requests’
12.	‘sudo pip install pygithub3’
13.	‘sudo pip install py-github’
14. 'sudo pip install pygit2'
15. 'sudo pip install pytest'
16. 'sudo pip install patch'
17. 'sudo pip install pandas'


## Java

Java SE is freely available from the link Download Java:http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
You can download a version based on your operating system.Follow the instructions to download Java and run the .exe to install Java on your machine. Once you installed Java on your machine, you will need to set environment variables to point to correct installation directories −

### Setting Up the Path for Windows
1. Assuming you have installed Java in c:\Program Files\java\jdk directory −
2. Right-click on 'My Computer' and select 'Properties'.
3. Click the 'Environment variables' button under the 'Advanced' tab.
4. Now, alter the 'Path' variable so that it also contains the path to the Java executable. Example, if the path is currently set to 'C:\WINDOWS\SYSTEM32', then change your path to read 'C:\WINDOWS\SYSTEM32;c:\Program Files\java\jdk\bin'.

### Setting Up the Path for Linux, UNIX, Solaris, FreeBSD
Environment variable PATH should be set to point to where the Java binaries have been installed. Refer to your shell documentation, if you have trouble doing this.
Example, if you use bash as your shell, then you would add the following line to the end of your '.bashrc: export PATH = /path/to/java:$PATH'

### Popular Java Editors
To write your Java programs, you will need a text editor. There are even more sophisticated IDEs available in the market. But for now, you can consider one of the following −

#### Notepad − On Windows machine, you can use any simple text editor like Notepad (Recommended for this tutorial), TextPad.

#### Netbeans − A Java IDE that is open-source and free which can be downloaded from https://www.netbeans.org/index.html.

#### Eclipse − A Java IDE developed by the eclipse open-source community and can be downloaded from https://www.eclipse.org/.