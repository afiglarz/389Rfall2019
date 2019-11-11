# Writeup 9 - Forensics II

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz


## Assignment details

### Part 1 (45 Pts)

1.	Warmup: what IP address has been attacked?
1.	142.93.136.81 is being attacked by 159.203.113.181
2.	What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
1.	The beginning TCP stream shows a port scan being conducted by the attacker against the server. Every other packet shows a different port scanned. They more than likely used a tool like nmap. 
3.	What are the hackers' IP addresses, and where are they connecting from?
1.	159.203.113.181 is the hacker IP address and they are connecting from some DigitalOcean server located in New York.
4.	What port are they using to steal files on the server?
1.	They are using ports 20 and 21. The data is getting sent over port 20 and the server authentication happened over port 21.
5.	Which file did they steal? What kind of file is it? Do you recognize the file?
1.	They stole a jpeg file. This file is called “find me.” You can get location data from the file by running exiftool on it. The file itself is in my writeup folder.
6.	Which file did the attackers leave behind on the server?
1.	They left a file behind called “greetz.fpff.” You need to write the parser in part two of the project to make sense of it. 
7.	What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is not an option.
1.	You can close port 21 (FTP) or filter out its allowed traffic so that attacks like this can’t happen. You should also change the password to the FTP server because this attacker knows a set of approved credentials

### Part 2 (55 Pts)

i.	When was greetz.fpff generated?
i.	March 27th 2019
ii.	Who authored greetz.fpff?
i.	Fl1nch
iii.	List each section, giving us the data in it and its type.
i.	1. ASCII OUTPUT: Hey you, keep looking :)
ii.	2. COORDS OUTPUT: (52.336035, 4.880673)
iii.	3. Image/gif generated with name extracted_png.png
i.	Image located in writeup directory
iv.	4. ASCII OUTPUT: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
v.	5. Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=
iv.	Report at least one flag hidden in greetz.fpff. Any other flag found will count as bonus points towards the competition portion of the syllabus
Flags:
CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}
CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}
