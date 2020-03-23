#! /usr/bin/python

# Promeni datum

import os
import re
import sys

# Proveravamo da li je dovoljno argumenata komandne linije

if len(sys.argv) != 3:
    print "Koriscenje: ./proba.py fajl br_dana"
    exit()

# Proveravamo da li je fajl extenzije .txt
if re.match(".*\.txt",sys.argv[1], re.I) == None:
    print "Datoteka mora biti .txt"
    exit()

# Procotamo sav sadrzaj iz fajla i smetamo ga u data
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

# Otvaramo izlazni fajl za upis cije ime
# se dobija nadovezivanjem stringa new na staro ime fajla
izlaz = open('new'+sys.argv[1],'wb')

# Pravimo pattern za datum

pattern = re.compile('(?P<DAY>([1-2][0-9])|([0-9])|(3[0-1])).(?P<MONTH>(1[0-2])|([1-9])).(?P<YEAR>[0-9]{4})')
regex = '(?P<DAY>([1-2][0-9])|([0-9])|(3[0-1])).(?P<MONTH>(1[0-2])|([1-9])).(?P<YEAR>[0-9]{4})'

for m in re.finditer(regex,data):

    dan = int(m.group('DAY'))
    mesec = int(m.group('MONTH'))
    godina = int(m.group('YEAR'))

    for i in range(0,abs(int(sys.argv[2]))):

        if int(sys.argv[2]) > 0:
            dan = dan + 1
            if dan > 31:
                dan = 1
                mesec = mesec + 1
                if mesec > 12:
                    mesec = 1
                    godina = godina + 1

        if int(sys.argv[2]) < 0:
            dan = dan - 1
            if dan < 1:
                dan = 31
                mesec = mesec - 1
                if mesec < 1:
                    mesec = 12
                    godina = godina - 1

    dan = str(dan)
    mesec = str(mesec)
    godina = str(godina)

    regex1 = m.group('DAY')+'.'+m.group('MONTH')+'.'+m.group('YEAR')

    # Stampanje pomerenih datuma u terminal radi evidencije
    print("dd. mm. gggg. -> %s.%s.%s" %(dan,mesec,godina))

    # Menjanje starog datuma navim
    data = re.sub(regex1, dan+"."+mesec+"."+godina,data)

# Upisujemo u nov fajl
izlaz.write(data)

# Zatvaramo fajl
izlaz.close()
