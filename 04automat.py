#! /usr/bin/python

try:
    f = open('konacni_automat.txt','r')
except IOError:
    print 'Neuspesno otvaranje fajla ka.txt'
    exit()

linije = f.readlines()

def nije_komentar(l):
    return l[0]!='#' and l!='\n'

def strip(s):
    return s.strip()

linije = filter(nije_komentar,linije)

import re

azbuka = re.split(',\s*',linije[0])
azbuka = map(strip,azbuka)

stanja = re.split(',\s*',linije[1])
stanja = map(int,stanja)

pocetno = int(linije[2].strip())

if pocetno not in stanja:
    print 'Neispravno pocetno stanje!'
    exit()


zavrsna_stanja = re.split(',\s*',linije[3])
zavrsna_stanja = map(int, zavrsna_stanja)

linije = map(strip,linije)
for stanje in zavrsna_stanja:
    if stanje not in stanja:
        print 'Neispravno zavrsno stanje!'
        exit()

prelazi = {}
for i in range(4,len(linije)):
    stanje1, slovo, stanje2 = re.split("\s+",linije[i])
    stanje1, stanje2 = int(stanje1), int(stanje2)
    if slovo not in azbuka:
        print "Neispravno slovo %c" % slovo
        exit()
    if stanje1 not in stanja:
        print "Neispravno stanje %d" % stanje1
        exit()
    if stanje2 not in stanja:
        print "Neispravno stanje %d" % stanje2
        exit()
    if prelazi.has_key((stanje1,slovo)) and prelazi[(stanja1,slovo)]!=stanje2:
        print "Automat nije DKA jer iz tanja %d po slovu %c postoje vise prelaza!" %(stanja1,slovo)
        exit()
    prelazi[(stanje1,slovo)]=stanje2

import sys
rec = sys.stdin.readline()
rec = rec.strip()

tekuce_stanje = pocetno
for slovo in rec:
    if not prelazi.has_key((tekuce_stanje,slovo)):
        print "Automat ne prihvata rec"
        exit()
    tekuce_stanje = prelazi[(tekuce_stanje,slovo)]

if tekuce_stanje in zavrsna_stanja:
    print "Automat prihvata rec"
else:
    print "Automat ne prihvata rec"
