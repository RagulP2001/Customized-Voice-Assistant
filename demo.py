import newpy
import json

#website name
#newpy.encrypt_files()
jsonvalues = newpy.decrypt_files()
#print(jsonvalues)
jsonvalues = jsonvalues.decode('utf-8')
print(jsonvalues)
jsonvalues = json.loads(jsonvalues)
#print(jsonvalues[3])
#print(jsonvalues["gmail"])
#print(newpy.decrypt(jsonvalues['facebook']['password']))