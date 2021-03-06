import requests
import sys
import getpass
import os.path
s = requests.Session()
web_root = raw_input("Website root [http://202.112.113.8]: " )
if not web_root:
	web_root = "http://202.112.113.8"
user = raw_input("Username: ")
password = getpass.getpass()
r = s.post(web_root + '/user_status.php' , data = {'url_target': '/courselist.php' , 'id': user , 'password': password } , allow_redirects=False)
r.raise_for_status()
try:
	print >> sys.stderr, "logged in as %s"%r.cookies['yoj_user_id']
except:
	print >> sys.stderr, "ERROR: Failed to log in."
	quit()
assignment_id = int(raw_input("Assignment ID: "))
filename = raw_input("File to send: ").decode(sys.stdin.encoding);
if not filename:
	print >> sys.stderr, "ERROR: You must enter a file name."
	quit()
if not os.path.isfile(filename):
	print >> sys.stderr, "ERROR: %s does not exist or is not a file."
	quit()
print >> sys.stderr, "Submitting your work, please wait."
file_extension = os.path.splitext(filename)[1]
normalized_filename = "homework" + file_extension
r = s.post(web_root + '/assignment.php?id=%d'%assignment_id, data = {'uploadthisafile':'uploadthisafile'}, files = {'file' : (normalized_filename, open(filename, 'rb') ) })
r.raise_for_status()
print >> sys.stderr, "Your work has been submitted."

