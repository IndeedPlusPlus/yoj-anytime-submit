yoj-anytime-submit
==================

A simple tool that can help you to submit your work after deadline to the yoj, the internal online judge system.

Requirements
-------------
Scripts are tested on python 2.7.6.    
Requires requests (python-requests), you may use `pip install requests` to install.

Usage
------
This program contains an interactive command line interface.

1. run `python yoj-anytime-submit.py`.
2. When asked `Website root`, type the base URL of the target online judge system.
3. Type your user name when prompted `Username`. Try your student ID if you are not sure.
4. Type your password when `Password` shows up. Notice that your password will not be echoed in any form.
5. The program now tries to log in with the credential you provides.
6. If successfully logged in, the program ask you for the `Assignment ID`. Check the URI if not sure. (For example, the assignment id is 22 for `/assignment.php?id=22`)
7. Prepare your work as one single file and type the path to the file when prompted `File to send`. Please make sure this file exists and is readable.

Postscript
----------
Be on time next time.
