# matf_Leksicka_analiza
Neki reseni ispitni zadaci iz kursa Leksicka analiza na Matematickom fakultetu. U cilju pomoci, ostalim kolegama,radi lakseg pripremanja ispita iz ovog kursa.


Tekstovi zadataka:

## 1. Zadatak
Napisati Python skript koji kao prvi argument komandne linije prima putanju do fajla sa ekstenzijom ".txt" koji sadrzi u sebi proizvoljan tekst sa nekakvim datumima. Kao drugi argument skript prima broj dana (pozitivan ili negativan) za koliko treba pomeriti sve datume unapred ili u nazad. Skript treba da u istom direktorijumu napravi fajl sa pomerenim datumima. Ekstenzija novog fajla je ista kao i ulaznog, a ime se dobija nadvezivanjem stringa "new" na staro ime fajla.

		Primer ulazne datoteke za prvi zadatak:

		U nedeleju 25.03.2020. u Republici Srbiji je 
		proglaseno vanredno stanje. Od ponedeljka
		26.3.2020. je obustavljena nastava u svim
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


