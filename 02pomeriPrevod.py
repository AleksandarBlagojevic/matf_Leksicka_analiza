#! /usr/bin/python

# Program pomera prevod

import os,re,sys

# Proveramo da li imamo dovoljno argumenata komande linije
if len(sys.argv)!=3:
    print "Koriscenje: ./proba.py fajl br_milisec"
    exit()

# Proveramo da li je fajl odgovarajuce ekstenzije
if re.match(".*\.srt",sys.argv[1],re.I)==None:
    print "Datoteka mora biti srt ektenzije!"
    exit()

# Procitamo sav sadrzaj fajla i smestimo u listu data
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

# Otvaramo izlazni fajl za upis cije ime
# se dobija nadovezivanjem stringa new na staro ime fajla
izlaz = open('new'+sys.argv[1],'wb')

# Pravimo pattern za datum
pattern = re.compile('(\d\d):(\d\d):(\d\d),(\d+)')
regex = '(\d\d):(\d\d):(\d\d),(\d+)'
for m in re.finditer(regex,data):

    sat = int(m.group(1))
    minut = int(m.group(2))
    sec = int(m.group(3))
    msec = int(m.group(4))

    for i in range(0,abs(int(sys.argv[2]))):

        if int(sys.argv[2]) > 0:
            msec = msec + 1
            if msec > 999:
                msec = 0
                sec += 1
                if sec > 59:
                    sec = 0
                    minut  += 1
                    if minut > 59:
                        minut = 0
                        sat += 1

        if int(sys.argv[2]) < 0:
            msec = msec - 1
            if msec < 0:
                msec = 999
                sec -= 1
                if sec < 0:
                    sec = 59
                    minut  -= 1
                    if minut < 0:
                        minut = 59
                        sat -= 1

    sat = str(sat)
    minut = str(minut)
    sec = str(sec)
    msec = str(msec)

    if int(sat)<10:
        sat = '0'+sat
    if int(minut)<10:
        minut = '0'+minut
    if int(sec)<10:
        sec = "0"+sec
    if int(msec)<10:
        msec = '00'+msec
    if int(msec)<100:
        msec = '0'+msec

    regex1 = m.group(1)+':'+m.group(2)+':'+m.group(3)+','+m.group(4)

    # Menjanje starog vremena novim
    data = re.sub(regex1,(sat+':'+minut+':'+sec+','+msec),data)

# Upisujemo u nov fajl
izlaz.write(data)

# Zatvaramo datoteku
izlaz.close()
