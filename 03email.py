#! /usr/bin/python

import os,re,sys

# proveramo da li imamo dovoljno argumenata komande linije
if len(sys.argv)!=3:
    print "Koriscenje: ./proba.py fajl mail_korisnika"
    exit()


# procitamo sav sadrzaj fajla i smestimo u listu data
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

# pravimo patter za mail
regex = 'From: \w+ \w+ <([\w\.-]+@[\w\.-]+\.\w{2,4})>\s'
regex += 'To: \w+ \w+ <([\w\.-]+@[\w\.-]+\.\w{2,4})>'

print "e-mail adrese na koje je korisnik najcesce slao poruke uredjene po broju poslatih poruka"

# lista u kojoj smestamo e-mail adrese koje je korisnik slao
l = list()
# lista u kojoj smestamo e-mail arese koje je korisnik primio
l1 = list()

for m in re.finditer(regex,data):

    mejl_korisnika = str(m.group(1))
    if mejl_korisnika == sys.argv[2]:
        mejl = str(m.group(2))
        l.append(mejl)

# dobijamo elemente liste bez duplikata
l_items = set(l)

# za svaki element kreiramo torku sa brojem pojavljivanja za svaki element
l_counts = [(l.count(x), x) for x in set(l)]

# sortiramo elemente prema broju pojavljivanja u oparajucem poretku
l_counts.sort(reverse=True)

# brisemo broj pojavljivanja iz torke i ostavljamo samo element
l_result = [y for x,y in l_counts]

# stampamo elemente liste
for el in l_result:
    print el


print "e-mail adrese na koje je korisnik dobio najvise poruka uredjene po broju dobijenih poruka"

for m in re.finditer(regex,data):

    mejl_korisnika = str(m.group(1))
    if mejl_korisnika == sys.argv[2]:
        mejl = str(m.group(2))
        l1.append(mejl)

# dobijamo elemente liste bez duplikata
l_items1 = set(l1)

# za svaki element kreiramo torku sa brojem pojavljivanja za svaki element
l_counts1 = [(l1.count(x), x) for x in set(l1)]

# sortiramo elemente prema broju pojavljivanja u oparajucem poretku
l_counts1.sort(reverse=True)

# brisemo broj pojavljivanja iz torke i ostavljamo samo element
l_result1 = [y for x,y in l_counts1]

# stampamo elemente liste
for el in l_result1:
    print el
