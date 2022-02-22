# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:44:32 2020

@author: Dell
"""

def remover(dellist,query):
    querywords = query.split(" ")
    resultwords  = [word for word in querywords if word.lower() not in dellist]
    result = ' '.join(resultwords)
    return result