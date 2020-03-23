#! /usr/bin/env python

import os,re,sys

if len(sys.argv)<2:
    print "Kroscenje: ./05knjiga.py -opcija naslov_knjige"
    exit()

# procitamo sav sadrzaj fajla i smestamo ga u memoriju
fajl = open('knjige.xml','rb')
data = fajl.read()
fajl.close()

# liste u kojoj smestamo podatke o knjizi (indeksira se od nule)
naslov = []
autor = []
godina = []
izdavac = []
cena = []
br_knjiga = 2

for m in re.finditer('<naslov>\s*(\w+.*?)\s*</naslov>\s*',data):
    naslov.append(m.group(1))
for m in re.finditer('<autor>\s*(.+)\s*</autor>\s*',data):
    autor.append(m.group(1))
for m in re.finditer('<izdavac>\s*(.+)\s*</izdavac>\s*',data):
    izdavac.append(m.group(1))
for m in re.finditer('<godina_izdanja>\s*(.+)\s*</godina_izdanja>\s*',data):
    godina.append(m.group(1))
for m in re.finditer('<cena valuta="(\w+)">\s*(\d+)\s*</cena>\s*',data):
    cena.append(m.group(2)+m.group(1))
for m in re.finditer('<knjiga rdb="(\d+)">\s*',data):
    br_knjiga = int(m.group(1))

for i in range(0,br_knjiga):
    if sys.argv[1]=='-a' and naslov[i]==sys.argv[2]:
        print autor[i]
    elif sys.argv[1]=='-c' and naslov[i]==sys.argv[2]:
        print cena[i]
    elif sys.argv[1]=='-i' and naslov[i]==sys.argv[2]:
        print izdavac[i]
    elif sys.argv[1]=='-g' and naslov[i]==sys.argv[2]:
        print godina[i]
    elif naslov[i] == sys.argv[1]:
        print ("%s %s %s %s " %(str(autor[i]),str(cena[i]),str(izdavac[i]),str(godina[i])))
