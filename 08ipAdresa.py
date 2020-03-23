#! /usr/bin/env python

import os,sys,re

if len(sys.argv)!=2:
    print "Koriscenje: %s ime_datoteke"%sys.argv[0]
    exit()

if re.match(".*\.txt",sys.argv[1],re.I)==None:
    print "Datoteka mora biti u txt formatu!"
    exit()

# procitamo sav sadrzaj i smestamo u memoriju
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

for m in re.finditer(r'\b((2[0-5]{2}|1[0-9]{2}|[0-9]{1,2})\.){3}(2[0-5]{2}|1[0-9]{2}|[0-9]{1,2})\b',data):
    ipadresa = m.group(0)
    print("%s" %ipadresa)
