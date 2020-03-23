#! /usr/bin/env python

import os,re,sys

if len(sys.argv)!=3:
    print "Netacan broj argumenta komandne linije!"
    exit()

if re.match('.*\.html',sys.argv[1],re.I)==None:
    print "Datoteka mora biti extenzije .html!!!"
    exit()

# procitamo sav sadrzaj fajla i smestamo ga u memoriju
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

if sys.argv[2] == 'l' or sys.argv[2] == '-l':
    for m in re.finditer('http[s]?://([a-zA-Z0-9./~])+',data):
        adresa = m.group(0)
        print ("%s" %adresa)

if sys.argv[2] == 's' or sys.argv[2] == '-s':
    for m in re.finditer('[a-zA-Z0-9]+\.jpg',data):
        slika = m.group(0)
        print ("%s" %slika)
