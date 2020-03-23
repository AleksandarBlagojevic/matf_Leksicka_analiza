#! /usr/bin/python

import os,sys,re

# Proveravamo da li imamo dovljno argumenata komandne linije
if len(sys.argv)!=2:
    print('Koriscenje: %s fajl.tex' %sys.argv[0])
    exit()

# Proveravamo da li je prosledjen tex fajl
if re.match(r'.*\.tex',sys.argv[1],re.I)==None:
    print 'Datoteka mora biti tex fajl'
    exit()

# Otvaramo datotu i sav sadrzaj smestamo u memoriju
fajl = open(sys.argv[1],'rb')
data = fajl.read()
fajl.close()

mapa1 = {}

# Otvaramo html fajl za pisanje
izlaz = open('index.html','w')

izlaz.write('<html>\n<title><head>')
izlaz.write('Kolokvijum iz LA</head></title>\n<body>\n<table>\n')

if re.finditer('\caption{[a-zA-z ]+}',data):
    for m in re.finditer('\caption{([a-zA-z ]+)}',data):
        izlaz.write('<caption>'+m.group(1)+'</caption>\n')

kol1='c'
kol2='l'
kol3='r'
kol4='l'
kol5='l'

if re.finditer('{tabular}{\s*([rcl])\s*([rcl])\s*([rcl])\s*([rcl])\s*([rcl])\s*}',data):
    for m in re.finditer('{tabular}{\s*([rcl])\s*([rcl])\s*([rcl])\s*([rcl])\s*([rcl])\s*}',data):
        kol1 = str(m.group(1))
        kol2 = str(m.group(2))
        kol3 = str(m.group(3))
        kol4 = str(m.group(4))
        kol5 = str(m.group(5))

def align(kol):
    if kol=='c':
        return 'center'
    elif  kol=='r':
        return 'right'
    else:
        return 'left'

kol1 = align(kol1)
kol2 = align(kol2)
kol3 = align(kol3)
kol4 = align(kol4)
kol5 = align(kol5)

#print kol1, kol2, kol3, kol4, kol5

if re.finditer('([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*[&]\s*([a-zA-Z]+)\s*\\\\',data):
    for m in re.finditer('([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*[&]\s*([a-zA-Z]+)\s*\\\\',data):
        izlaz.write('<tr><th align="'+kol1+'">'+m.group(1)+'</th><th align="'+kol2+'">'+m.group(2)+' '+m.group(3)+'</th><th align="'+kol4+'">Ocena</th></tr>\n')

for m in re.finditer('(\d+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*([a-zA-Z]+)\s*[&]\s*(\d+)\s*[&]\s*[&]\s*(\d+)\s*\\\\',data):

    ocena = int(m.group(4))+int(m.group(5))
    if ocena>90 and ocena<101:
        ocena = 10
    elif ocena>80 and ocena<91:
        ocena = 9
    elif ocena>70 and ocena<81:
        ocena = 8
    elif ocena>60 and ocena<71:
        ocena = 7
    elif ocena>50 and ocena<61:
        ocena = 6
    else:
        ocena = 5

    mapa1[m.group(2)+' '+m.group(3)] = ocena

def poredi(x, y):
    return cmp(mapa1[x],mapa1[y])

# Sotiramo studente po broju poena
keys = mapa1.keys()
keys.sort(poredi,reverse=True)

i=0
for k in keys:
    i=i+1
    izlaz.write('<tr><th>'+str(i)+' </th><th>'+k+' </th><th>'+str(mapa1[k])+'</th ></tr>\n')

if re.finditer('/end{table}',data):
    izlaz.write('</tabela>\n')

izlaz.write('</body></html>\n')

# Zatvaramo fajl
izlaz.close()
