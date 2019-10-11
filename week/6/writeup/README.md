# Writeup 6 - Binaries I

Name: Andrew Figlarz
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andrew Figlarz

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

The main function of the compiled crackme binary goes through a series of three checks before finally outputting the desired flag. 
I Found out that the first check just looked to see if there was an argument to crackme that was the same as the string “Oh God”. This was apparent by looking at the strings in the data section of the disassembled code. I just took my best guess as to what I had to do with the string, and I ended up passing this check. This check can be passed by running ./crackme “Oh God”.
The second check called getenv and looked for a linux environment variable called FOOBAR. FOOBAR was supposed to be set to some string relating to “seye ym “. I realized that there was a loop within the disassembled code that checked each character in the environment variable starting from the last character of “seye ym “. This meant that FOOBAR was supposed to be set to “ my eyes”. The check then got passed as it read and checked every letter in the string individually. 
The third check was the most difficult to figure out. This one required you to really investigate the code and discover that there were a bunch of cases that each corresponded with a different ASCII encoding of a letter. This check read the first 10 characters from a file that you had to create in the same directory as the binary named “sesame”. It made sure there was a null byte at the end and iterated through each letter to see if it corresponded with the correct position/case combination. If you looked at the number of the cases you could figure out what letter was supposed to go in what spot in the “sesame” string. This string ended up being “ they burn”. After you set up the “sesame” file to contain the correct data, you can execute the crackme binary again and get the flag as output. The flag is: CMSC389R-{di5a55_0r_d13}
The flag is programmed in such away that a part of it gets unveiled every time the update flag function is called. You must pass all three checks so that the function is called enough times and so that the correct flag gets printed out after you run the binary. The flag itself is not stored as a string in memory. 
