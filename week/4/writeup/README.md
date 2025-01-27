# Writeup 2 - Pentesting

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz

## Assignment Writeup

### Part 1 (45 pts)

* The right flag
CMSC389R-{p1ng_as_a_$erv1c3}
* Showing what input you used to obtain the flag.
nc wattsamp.net 1337
; cat home/flag.txt
* Describing your thought process.
Based off of my knowledge from previous classes (CMSC 330), I realized that command injection can be as simple as placing a semicolon to symbolizing the end of an input to the running command, then following that up with any command that you would like. In this example I first tried “; ls” to see the list of directories on the server. This was more so a test to see if a simple command injection like that would even work on the server. After I figured out that it would work, I decided to check the /home directory. This was where the flag was on the last assignment so I figured that would be a good starting point. I got lucky and found the flag.txt file in that directory. I then used cat to see the inside of the file in the output of the command line and got the flag. 
* Any suggested precautions ejnorman84 could implement to prevent this vulnerability?
Eric Norman can prevent this vulnerability by checking for several characters and banning them (blacklist). These characters would include the semi-colon. He could also sanitize the input received by his server to remove characters like “;” so that it doesn’t allow for commands to be injected anymore. 


### Part 2 (55 pts)

I used the provided python stub code to help establish a socket connection to the wattsamp.net server through port 1337. Since I recognized that you could run arbitrary Unix commands by prepending them with a “;” character, I wrote my program on that premise. I implemented the shell portion by having a global variable store the current path of the shell and use it when issuing future commands through the shell. The program itself loops and sends requests to the server until shell is exited with the input “quit” and when the script itself is exited with the input “quit.” I spoke to Mitchell to try and get clarification as to how to implement the “pull” functionality. Instead of trying to implement something like scp into this script, I worked off the assumption that all files that are to be ripped from the server are to be in text format. So, when you send a request to pull from the server, it actually sends a cat command to that specific file, returns the output of stdout, and uses it to write it to a new file called “result.txt” at the path designated by the second command argument. This script, albeit clunky, performs the required functions outlined in the project details. You can run the script using “python stub.py”.