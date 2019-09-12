# Writeup 2 - OSINT

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz

## Assignment Writeup

### Part 1 (45 pts)

Part 1
In class you were given an online usertag: ejnorman84
NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))
Use OSINT techniques to learn as much as you can about ejnorman84 and answer the following questions:
1.	What is ejnorman84's real name?
1.	Eric Norman
2.	Where does ejnorman84 work? What is the URL to their website?
1.	Wattsamp Energy
2.	http://wattsamp.net/
3.	List all personal information (including social media accounts, contacts, etc) you can find about ejnorman84. For each, briefly detail how you discovered them.
1.	Eric has an Instagram account. I found this by using https://instantusername.com/#/ from the OSINT Framework website under “Username Search Engines”
2.	Eric has a Reddit account. I found this through the same means of his Instagram account. 
3.	Eric has an email address under ejnorman84@gmail.com. I found this by running whois on “wattsamp.net”
4.	Eric has a relationship with the UMD CSEC Club. He has links to their twitter and umd page on his wattsamp.net website.
4.	List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
1.	157.230.179.99 Is the IP for the wattsamp.net site. I found this information by running nmap on the website’s domain name. By using the MXToolbox reverse lookup tool, I was able to find that the server is hosted in Duluth, GA by a company called DIgitalOcean, LLC.
5.	List any hidden files or directories you found on this website.
1.	I used dirbuster to try and find hidden directories on the website. It includes a /icons/ directory that I do not have access to. This is probably because it is looking for admin credentials to be able to access it. 
2.	Also when you access the /robots.txt/ directory you find a bonus flag
6.	What ports are open on the website? What services are running behind these ports? How did you discover this?
1.	Port 22 over TCP is open. This port is running ssh. Port 80 over TCP is open. This port is running http. I found this by running nmap on “wattsamp.net”
2.	Port 1337 is also open. This is the port that we are trying to attack.
7.	Which operating system is running on the server that is hosting the website? How did you discover this?
1.	The operating system is Ubuntu and it is running an Apache web server. You get this message if you type in an incorrect page on the wattsamp.net domain: Apache/2.4.29 (Ubuntu) Server at wattsamp.net Port 80.
8.	BONUS: Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is *CMSC389R-{}. (Up to 9 pts!)
1.	*CMSC389R-{LOOKING_CLOSELY_PAYS}
2.	*CMSC389R-{html_h@x0r_lulz}
3.	*CMSC389R-{n0_indexing_pls}
4.	*CMSC389R-{Do_you-N0T_See_this}

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

I got to the final solution by using the python script skeleton that you guys provided. I used the username “ejnorman84” and iterated through each password in “rockyou.txt” until I found the correct password. The script itself creates a socket connection to 157.230.179.99 on port 1337. The script has a loop that establishes a new connection to the server for every password in “rockyou.txt.” Since the server connection requires a captcha to be filled out every time a new connection is made, I used a regular expression to be able to parse the different components of the equation and used python to evaluate it and returned the answer. I then sent the username and the password that the loop was on to the server as a password attempt. The server returns “Fail” if the password is wrong, so I perform a check to see if that message is returned, if it is then the program continues and tries another password. If it doesn’t return “Fail” then I know I guessed the correct password. The correct password was “hello1.”