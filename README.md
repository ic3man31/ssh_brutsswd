<img alt="Coding" width="100%" height="100" style="margin-bottom: 20px" src="https://llllllll.co/uploads/default/original/3X/c/5/c5a75e9659127da35d8d13783a26eb130f14874a.gif">

# ssh_brutsswd

This is a Python script that allows you to perform a SSH bruteforce attack by trying different ***passwords*** against a target host. It uses the `paramiko` library for SSH connections and the `pwn` and `colorama` libraries for enhanced output formatting.

## Disclaimer

**The following script is intended for educational purposes only**. The creator of this script, do not condone or support any illegal or illicit activities that may result from its use. The script is meant to be used as a learning tool and any misuse of it is solely the responsibility of the user. We will not be held liable for any damages or legal issues that may arise from the use of this script in any unauthorized or illegal activities. By using this script, you agree to assume all responsibility and liability for its use and to use it in accordance with all applicable laws and regulations.

## Prerequisites

-   Python 3.x
-   `pwn` library
-   `colorama` library
-   `paramiko` library

## Usage

1.  Clone the repository or download the script.
2.  Install the required dependencies by running the following command:

`pip install pwn colorama paramiko`

3.  Run the script using the following command:

`python3 ssh_brutesswd.py`

4.  Follow the prompts to enter the target's IP address, port number, username, and the filename for the password list.
5.  The script will iterate through each password in the list and attempt to connect to the target SSH server using the provided credentials.
6.  If a valid password is found, it will be displayed on the screen, and the script will stop.

**Note:** This script should only be used for educational or authorized testing purposes. Unauthorized use of this script is illegal and unethical.

## Authors

[J.Rosales](https://github.com/ic3man31/ic3man31)

## License
[LICENSE](LICENSE)
