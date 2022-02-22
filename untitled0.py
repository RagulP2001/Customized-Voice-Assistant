# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:27:54 2020

@author: pavit
"""

import json
import newpy
website_name = "gmail"
jsonvalues = newpy.decrypt_files()
jsonvalues = jsonvalues.decode('utf-8')
jsonvalues = json.loads(jsonvalues)
username = jsonvalues[website_name]['username']
password = str((newpy.decrypt(jsonvalues[website_name]['password'])).decode('utf-8'))
print(username,password)







