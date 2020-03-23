# matf_Leksicka_analiza
Neki reseni ispitni zadaci iz kursa Leksicka analiza na Matematickom fakultetu. U cilju pomoci, ostalim kolegama,radi lakseg pripremanja ispita iz ovog kursa.


Tekstovi zadataka:

## 1. Zadatak
Napisati Python skript koji kao prvi argument komandne linije prima putanju do fajla sa ekstenzijom ".txt" koji sadrzi u sebi proizvoljan tekst sa nekakvim datumima. Kao drugi argument skript prima broj dana (pozitivan ili negativan) za koliko treba pomeriti sve datume unapred ili u nazad. Skript treba da u istom direktorijumu napravi fajl sa pomerenim datumima. Ekstenzija novog fajla je ista kao i ulaznog, a ime se dobija nadvezivanjem stringa "new" na staro ime fajla.

		Primer ulazne datoteke za prvi zadatak:

		U nedeleju 15.03.2020. u Republici Srbiji je 
		proglaseno vanredno stanje. Od ponedeljka
		16.3.2020. je obustavljena nastava u svim
		skolama i fakultetima.

		Ovaj file je dovoljan za demonstriranje
		rada skripta, a vi mozete probati sa bilo
		kojim vecim file-om.

## 2. Zadatak
Napisati Python skript koji kao prvi argument komandne linije prima putanju do fajla sa ekstenzijom ".srt" koji sadrzi u sebi prevod. Kao drugi argument skript prima broj miliekundi (pozitivan ili negativan) za koliko treba pomeriti sve prevode unapred ili u nazad.  Skript treba da u istom direktorijumu napravi fajl sa pomerenim prevodom. Ekstenzija novog fajla je ista kao i ulaznog, a ime se dobija nadvezivanjem stringa "new" na staro ime fajla.

		Primer ulazne datoteke za drugi zadatak:
        
		1
		00:02:00,955 --> 00:02:04,157
		Leksicka analiza
		
		2
		00:02:04,194 --> 00:02:05,951
		Primer drugog zadatka, 
		koji menja prevod.
        
		3
		00:02:05,962 --> 00:02:07,833
		Jos neki tekst.

## 3. Zadatak
Datoteka cija putanja se navodi kao argument komandne linije, sadrzi e-mailove koje je korisnik slao ali i one koje je primio. E-mail adresa korisnika se zadaje kao drugi argument komandne linije. Napisati Python skript koji prikazuje e-mail adrese na koje je korisnik najcesce slao poruke uredjene po broju poslatih poruka, kao i one adrese sa kojih je dobio najvise poruka, takodje sortirane. Datoteka sadrzi vise poruka u sledecem formatu:

		Date: Mon, 5 Jul 1999 23:46:18 -0500
		From: John Doe <johndoe@students.uiuc.edu>
		To: John Smith <jsmith@staff.uiuc.edu>, user@host.com
		Message-Id: <199907052346.LAA05394@students.uiuc.edu>
		Subject: This is a subject header.

		This is the message body. It is seperated from the headers by a blank
		line. The message body can span multiple lines.

## 4. Zadatak
Napisati Python skript koji kao argument komadne linije prima naziv fajla u kome je zadat konacni automat, u formatu koji je naveden u prilogu zadatka (linije koje pocinju znakom # su komentari, a od ostalih linija, prvapredstavlja azbuku, druga skup stanja, treca pocetno stanje automata, cetvrta skup zavrnih, a ostale prelaze automata). Proveriti da li je automat ispravno zadat (pocetno stanje u skupu stanja, sva zavrsna stanja u skupu stanja, svi prelazi definisati nad datim stanjima i azbukom), i proveriti da li je automat deterministicki. Ako jeste ucitati rec sa standardnog ulaza i proveriti da li je automat prihvata.

		Primer za cetvrti zadatak:

		# ovo je neki komentar
		# prva linija fajla sadrzi azbuku
		a,b
		#drugi linija sadrzi stanja automata
		0, 1, 2
		#treca linija sadrzi pocetno stanje
		0
		#cetvrta linija sadrzi zavrna stanja
		1, 2
		#ostale linije sadrze prelaze automata
		0 a 1
		0 b 2
		1 b 2
		2 b 2

		# Mozeti promeniti fajl konacni_automat.txt
		# i probati sa drugim automatom.

## 5. Zadatak
Napisati Python-skript koji stampa na standardni izlaz autora (−a), cenu (−c), izdavaca (−i) ili godinu izdanja (−g) knjige koja se navodi kao argument komandne linije, u zavinosti od prisutne opcije komandne linije (u slucajuda nema opcija, ispisati sve podatke o trazenoj knjizi). Informacije o knjigama se nalaze u fajlu knjige.xml.

		Primer pozivanja programa:
		
		$./05knjiga.py -a Yacc
		Filip Maric
		
		$./05knjiga.py -c "Python Standard Library"
		50eur

## 6. Zadatak
Napisati Python skript koji iz html fajla koji je zadat kao prvi argument komandne linije izdvaja sve linkove, ili sve slike, u zavisnosti da li je drugi argument komandne linije l ili s.

		Primer fajla za sesti zadatak:

		<html>
			<body>
				<h2> Norwegian Mountain Trip </h2>
				<img border="0" src="/images/pulpit.jpg" width="304"/>
				<h2> One more image </h2>
				<img src="/images/image.jpg"/>
				<a href="http://www.matf.bg.ac.rs/~mirko"> Link </a>
				<h2> Image as link </h2> 
				<a href="http://www.matf.bg.ac.rs/~mirko"> 
					<img src="/images/image.jpg">
				</a>
			</body>
		</html>

## 7. Zadatak.
Napisati Python skript koji iz tekstualnog fajla koji se zadaje kao argument komandne linije, izdvaja sve ispravno zapisane datume. Dan i mesec obavezno sadrze dve cifre, a godina cetiri.  Jednostavnosti radi, pretpostaviti da svaki mesec ima 31 dan. Separator izmedju dana i meseca, kao i meseca i godine, mora da bude isti, i jedan od sledecih . , - ili /.

		Primer za sedmi zadatak:
		
		Ovo je fajl u kome se nalazi neki tekst.
		Tekst sadrzi datume u sebi: 10.02.2011
		Ovo je jos jedan datum: 31-02-0000
		a potom I jos jedan: 13/05/2111. 
		U delu kojinema validnih datuma:
		01/13/2011 32/03/2001 11-11.2011


