# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:47:29 2019

@author: shuklaas
"""

import urllib.request as req


proxy = req.ProxyHandler({'http': r'http://shuklaas:$Invicible44417@11.164.4.21:8080'})
auth = req.HTTPBasicAuthHandler()
opener = req.build_opener(proxy, auth, req.HTTPHandler)
req.install_opener(opener)
conn = req.urlopen('http://google.com')
return_str = conn.read()
print(conn)