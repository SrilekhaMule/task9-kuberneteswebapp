#!/usr/bin/python3 
print("content-type:text/plain")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
command= form.getvalue("cmd")
output=sp.getoutput(command+"  --kubeconfig /home/student/admin.conf")
print(output)
