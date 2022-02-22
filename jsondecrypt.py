import newpy
import json

#website name
#newpy.encrypt_files()
def decrypt_me(website_name):
    try:
        jsonvalues = newpy.decrypt_files()
        jsonvalues = jsonvalues.decode('utf-8')
        jsonvalues = json.loads(jsonvalues)
        username = jsonvalues[website_name]['username']
        password = str((newpy.decrypt(jsonvalues[website_name]['password'])).decode('utf-8'))
        return username,password
    except Exception as e:
        print(e)
        print("No username and password found for",website_name)