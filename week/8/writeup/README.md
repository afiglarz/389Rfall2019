# Writeup 8 - Binaries II

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The password is generated from a seed of the current system time. This means that if two instances of the same server were to run then you would generate the same exact admin password. This can especially be exploited when you have the source code for the server.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

In addition to the timing attack revolved around the password generation there are two additional exploits. These include string format vulnerability and a buffer overflow.
The string format vulnerability can be located at line 46 with the call to printf. If you don’t give printf any arguments besides format modifiers, then you can use it to print values below it on the stack. You could use this to print the generated password.
The buffer overflow can be located at line 68 with the call to gets. You can exploit this by writing past the buffer allotted to gets to modify code later in the program. You can use this to overwrite the whitelist created in the program to include cat flag. 

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

There were two steps in obtaining this flag. The first was to crack the password. After many hours trying to fiddle with the format string vulnerability and seemingly getting nowhere, I reevaluated my approach to this assignment. I noticed that the password generation is the same every time the server gets executed. It will generate the same password as another instance of the server binary if they are both run at the exact same time. With this idea in mind I just ripped the password generating code from server.c, created my own c program called run_pass.c and compiled it. The only other modification I made was to include another for loop that repeats the password generation 10 times to account for latency in the network that could cause the password generation to happen on a different second. This program prints each password it generated to stdin so that you can just copy and paste it into the authenticate option on the server. I noticed at home that either the second or third password that gets generated is the correct password, so there is some trial and error to an extent. To help with the programs to run closer in sync with one another I wrote a little bash script called combo.sh that runs the run_pass binary in another tab in kali. This makes switched from program to program easier and doesn’t kill the connection to the server. 

Once you get the password the rest of the assignment is straightforward. Since you know that the program uses gets when reading in a command after selecting the 4th option on the server, you know that you can exploit it with a buffer overflow. The server has a built-in whitelist of commands that prevent you from running cat flag straight from the terminal. To get around this you must realize that the buffer to gets is 33 characters long. What you can do is overwrite the whitelist to include cat flag and then call cat flag immediately after. You can accomplish this by inputting “cat flag{null-terminator/ctrl-@}{25 spaces}cat flag” and hitting return. The 25 spaces account for the remaining size of the buffer and the null-terminator is needed for the program to know that the first cat flag is a string. 
