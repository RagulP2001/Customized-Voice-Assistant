import newpy
import getpass
import json
import time
#website name
#newpy.encrypt_files()
#time.sleep(10)
jsonvalues = newpy.decrypt_new()
web = str(input("Enter the name of website: "))
username = str(input("Enter the username: "))
password = newpy.encrypt(getpass.getpass("Enter the password: "))
password = password.decode('utf-8')
web.lower()

jsonvalues = jsonvalues.decode('utf-8')
jsonvalues = json.loads(jsonvalues)

updatejson = {web : {"username" : username , "password" : password}}

jsonvalues.update(updatejson)

jsonvalues = json.dumps(jsonvalues,indent=4,sort_keys=True)
jsonvalues = str(jsonvalues)
newpy.encrypt_new(jsonvalues)
