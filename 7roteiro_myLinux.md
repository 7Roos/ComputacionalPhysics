# Objetivo
Did you know that it is possible to automate package installation? This can be done through a shell script, which is nothing more than terminal instructions. I will show you how I built a custom Linux package installation automator and the paths for you to change the script to your needs. 

# Motivação
What led me to do this script, is that over time I solved several problems of installation and configuration very particular, with commands that I did not master and also would not remember. So it would be useful to keep the step by step somewhere. Thus, when making a new installation, I no longer need to be looking in forums the same solutions that I had already found in the past. 

# Introdução
The idea is similar when we create a virtual environment with 'pip' or 'conda' and select the package versions to be installed through a file of type "requirements.txt". But, with the difference that they are Linux packages, they do not always have the same name in different distributions. In addition, they may involve more processes than a simple 'sudo apt install pack'.  A viable way to do this automation is through shell script, where terminal statements can be written into a file with the extension 'sh' and run directly in the terminal, with './shell_script.sh'. I had a clear idea of what I wanted to do, but did not master the syntax, so I had the help of an AI (Gemini) to provide the commands and a minimally readable structure.

# Design
Before I go to the code, I’ll show you the logic behind my choices of All we need to install and configure our programs is just a single script, without any extra files. This was a personal choice, you could adapt it to load a text file with the name of the packages, would make the code more modular but add more files to load together and my rule was to use only one single file. Or else, you could have done it in Python, or with a makefile, maybe... But I had to make a choice, such that it would guarantee me without any doubt that this script would run on any Linux. My program was divided into 4 parts: definition, update, installation and configuration. 

## definição
First, we define which programs will be installed and which package manager between: apt, dnf and pacman. Corresponding to the base distributions: Debian, RHEL and Arch. These choices are necessary because the installation may be different between these package managers. 
## atualização
From these settings we can update the Linux and programs that are already installed. 
## instalação
In the next step we do the installation of packages. I decided to divide the packages into groups, for better organization you can change this. In addition, there are several ways to create the logic for handling exceptions. For example, we can create a vector and run it in a loop by installing the packages one by one. I have added a two second pause between installs of package groups. The reason for this is that it allows the user to stop the installation, if any error occurred during the installation, without stopping abruptly in the middle of an installation, causing a bug difficult to solve (I know from experience, never interrupt an installation process in the middle!). This pause is more useful than doing it through a user’s enter key. Because what does the user want?... That the installation in these two steps is automatic, that he can have a coffee while installing. Then when it returns from its cafe you can check through a log file, which was generated during the installation, if the installation has been successful. As for dependencies, well the package manager will take care of it for us. We can even put the package names side by side in a single installation command (when possible). This way, the package manager will take care of dependencies, and install in order, without risk for conflicts.

## configuração
Finally, in the last step we will make some settings as well as guide in the installation of more complex packages that require the user to go to a site, download the latest version and do another long sequence of steps. This part is quite manual, and its main function will be to guide the user. However, the processes can be automated, but I opted for didactic, so I will keep at first without large automations. Here we set things like git, VS Code and their extensions. Now that the structure has been clarified, let’s go to the code.


# Código
## Parte 1: definição
In line 1, as usual in these cases, I define the Shebang, thus informing the kernel which interpreter to use for this script. It is also a good practice to add a small initial comment section describing, in a clear and simple way, what the purpose of this script is. For while we are producing, everything makes sense and is obvious, but after some time it is not so simple. Thus, with the use of hastags, from line 3 to 5, I make a comment describing briefly the program. At the end, I sign and put the date. Another organizational measure is to put these comment blocks, like between lines 10 and 12, telling in which section we are. I start by defining the packages that will be installed, a good organization practice is divided into sections like 'media' and 'scientific'. For each of these sections we create a dictionary, briefly explaining the use of that package. It is ideal if they are right at the beginning of the script to make it easier to change packages without you having to go looking for the script.

## Parte 2: atualização
Now we can go to the next stage. We update the system and finally print on the screen and write in the log file that the update was executed successfully.

## Parte 3: instalação
Finally, we install the packages. We have to distinguish between different package managers, because the programs may have different names or procedures for installation. This script is general for most Linux systems, but you can simplify it to a single manager compatible with Ubuntu, for example. I set the installation order to start with the managers, like curl, git and pip that will be used in the installation of other packages. Soon after, I do the installation of media programs, less important but fast and easy to install. Finally, the scientific packages, which has the main tools of work. I finish with the optional, a python library and an alternative terminal. The 'program' variable stores the package name, while 'prefix' holds the package manager’s prefix, which can be apt, dnf or pacman. At each end of section we print on the screen and write in the log file the packages that have been installed. The trick here is to freeze the screen for 2 seconds, because it allows the user to see if the program has been installed and which will be installed without having to type enter at each entry, I want this to be very automatic, at most the user is monitoring, but being able to intervene, if you think necessary. Stopping during this pause will not cause errors by abruptly stopping an installation (this is a very laborious error to resolve). Some packages require more steps, or have different names for different package managers, so we deal with this in the branch structures.

## Parte 4: configuração
With all, or with most of the programs installed, we go to the last step that is to configure the programs and make some installations more complex and less important. We can start by asking the user if they want to set up git, then guide the OneAPI installation, which requires several steps. As well as remembering which extensions to add to VS Code.

# Execução
Enough of the talk! Let’s run this script and see if it delivers what it promises.

# GitHub
If you want to use this script, modify it to your needs, or refactor it (there are things to improve), I made this project available on GitHub (link in the description). Happy installation!
