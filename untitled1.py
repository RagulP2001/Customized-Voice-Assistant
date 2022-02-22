# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:03:40 2020

@author: pavit
"""

import json
#weather = urllib2.urlopen('url')
#wjson = weather.read()
wjson = '''
{
  "gmail": {
     "username" : "pavithran",
     "password" : "Pass"
     }
}
'''
wjdata = json.loads(wjson)
print(wjdata['gmail']['username'])
print(wjdata['gmail']['password'])
