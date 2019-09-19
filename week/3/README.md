# Operational Security and Social Engineering

## Assignment details

ANDREW FIGLARZ - YES I AGREE TO THE HONOR PLEDGE

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

You have been hired by a penetration testing firm and have been asked to collect some specific information about the Wattsamp employee from HW2, Eric Norman. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

- What's his mother's maiden name?
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?

Write up a pretext that you would use to social engineer this information out of Eric Norman. What approach would you take and how would you present yourself to elicit this information under the radar? Use the slides and what we covered in lecture to come up with a plan to obtain this information.


ANSWER:

Pretend that you are calling from the Census Bureau. You are doing a quick home prescreening census phone call to gauge how many census takers we need to deploy to his area (complete bs but it was the best I could think of). You can also spoof the phone number you call from to reflect that of some local government census building. This will bring his guard down and hopefully allow us to collect some information about him and his family. 

Introduce yourself as a census taker conducting a pre-census phone interview. Confirm his credentials by using what you could find with “whois wattsamp.net.” This includes his name: Eric Norman, his address: 1300 Adabel Dr. El Paso, Texas, and his phone number: 2026562837.

After you confirm these details, ask him for his birthdate (there’s a chance that her pin number is the month and year her son was born). After this, ask him about his demographics. Ask him questions about his marital status. If he’s married ask him questions about his wife and any possible his children. If he seems comfortable at this point then transition into asking questions about his father, followed by his mother. 

Be sure to ask the same types of questions across all members of his family to ensure that he doesn’t catch on to the oddly specific questions pertaining to his mother. You should ask for their name and if they have ever gone by any other name (including mother’s maiden name). You should ask about their birthdate and place of birth. From this point on, gauge how he is responding to your questions. If he is starting to give off an off vibe then try to reel him back in with questions that pertain to less sensitive topics and try to give him the chance to speak. If he feels comfortable then ask for a phone number to his father and mother. Contacting his mother would be a better idea because the elderly is often easier to socially engineer. 

Use his mother’s phone number to try and get the additional information out of her. You should maintain the census representative act just in case Eric contacts his mother about your previous phone call. You want to wait a few hours for Eric to contact his mother so that she is more vulnerable to give up vital information provided that your conversation with Eric left off on the right foot. 

Now that you are talking to his mother, introduce yourself the same way you did to Eric and start by asking her general demographic questions and if she can confirm her name and phone number. After you have established some credibility, try to get additional information from her by asking her address, where and when she was born. When you ask her who she lives with, try to pry out additional information about any pets she lives with and their names. For example, if she says she has a dog, try to relate and be like “oh I love dogs, my Australian Shepard lucky loves to play when it snows outside!” Also, you should try to poke and prod at the history of pets she had and ask about her first one. 

The final two pieces of information that you are trying to get will be a little bit trickier (ATM PIN and Browser). First, ask her whether she uses the internet, claiming that the census is starting to investigate how many U.S. citizens are using the internet. Ask her whether she uses her phone or a computer to access the internet. If she responds with “oh I just love using my iPhone” then you can assume she uses Safari. It’s safe to say that an older person doesn’t use an Android powered phone, but you can confirm with her if she does have an iPhone just to rule out that possibility. If she says she uses the computer, you can ask about the logo of at the bottom of her screen whenever she opens Google. If she describes “a blue E” you can assume its edge unless it’s an old computer then its internet explorer. If she describes a fox, then it’s probably Firefox. If it looks like chromes ugly blue, red, green and yellow circle then you know its Chrome. If its anything else, then you can assume that she doesn’t know what she’s talking about and just say she’s using Chrome because it’s the most used browser by far. 

You can potentially obtain her PIN number by asking her to secure her answers to the census questions by locking them with a 4-digit PIN. If you are lucky, she will just give you her bank account PIN, if this doesn’t work then you could try the month and year of her birthday or her home address if it is 4 numbers long (If not then also try padding with zeros). If you are actively trying to hack into her bank account while you are on the phone with her and the PIN that she gave you was invalid, then ask her to provide a different PIN (you could also lie and say something along the lines of “would you be able to provide the PIN you used the last time you spoke with a US Census Official” and she could probably give up her PIN that way).
After that thank her for her time and see if you can hack into her accounts.  








### Part 2

Eric Norman has recently discovered that Watsam's web server has been broken into by the crafty CMSC389R ethical hackers. After reading your published report, he has reached out to you to seek guidance in how he can repair some of the vulnerabilities that you have discovered.
Choose 3 specific vulnerabilities from homework 2 that you have identified (ie. exposed ports, weak passwords, etc.) and write a brief summary of some suggestions you can provide Eric for the Wattsamp web server and admin server. Be as thorough as possible in your answer, use specific examples and citing online research into security techniques that could be applied to the servers (ie. firewall, IDS/IPS, password managers, etc.).

### Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.


ANSWER:


Eric Norman is asking you to help him identify and fix the vulnerabilities that were found with his Watsamp web server. Three vulnerabilities that were found were the exposed port 1337, the weak password used for his admin account (hello1), and the ability to sign in multiple times without any timeout. The exposed port 1337 is significant because it alone allows for a backdoor into the webserver. This would allow anyone with the admin credentials to access data from the webserver that is stored locally and make any modifications they want. The weak password is a crazy huge vulnerability because you can assume that if Eric is using a password like that for his super-secret webserver then his other passwords are equally as weak as this one. This vulnerability is also easy to exploit by hackers who have a brute force script and a word list (like us). The last vulnerability is more so an oversight by Eric when he created the webserver (or whoever made the server for him). The ability to try login after login an infinite amount of times until one works is a poor design choice that can be exploited by hackers. 
Thankfully there are solutions to all these vulnerabilities.
The first thing Eric should do is close port 1337 and move his credentials over to some form of filtered SSH (port 22). SSH is much more secure than a completely open port 1337. In addition to this switch, Eric should turn off remote root access to his server. This will only provide him with additional security and no inconvenience because he will still be able to connect to his server remotely though his server provider (i.e. Digital Ocean) or through the actual machine if he’s hosting it himself. 
The second thing Eric should do is start using more secure passwords and perhaps even a password manager. More secure passwords get more and more important as time goes on because of how easy it is to crack a low security password. Eric can also use a website like https://passwordsgenerator.net/ to obtain a decently secure password. If Eric wishes to overhaul all of the current passwords that he’s using then he might want to start using a password manager like LastPass so that he can have all of the passwords that he uses saved in one spot just in case he forgets one.
The last thing that Eric should do is to install a firewall for his webserver (preferably one with good IPS). The firewall can be configured to filter out traffic that Eric does not want touching the server. This could include unauthenticated attempts to log into the server and can limit how many attempts can go through in a time interval. If a hacker goes about a certain allotted amount of login attempts, then he/she is locked out for a set amount of time or until a manual reset is performed. This will ensure that a hacker does not have a way into Eric’s server from the outside. 






### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
