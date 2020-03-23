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


for m in re.finditer('(([3][0,1]|[0-2]\d)-([1][0-2]|[0]\d)-(\d{4}))|(([3][0,1]|[0-2]\d)/([1][0-2]|[0]\d)/(\d{4}))|(([3][0,1]|[0-2]\d)\.([1][0-2]|[0]\d)\.(\d{4}))',data):
    datum = m.group(0)
    print("%s" %datum)
