# Toteutusdokumentti
## Projekti

Projektin tavoitteena on kehittää Python-ohjelma, joka käyttää RSA-salausalgoritmia viestien salauksessa ja purkamisessa.

RSA:ssa käyttäjä luo julkisen avaimen kahdesta suuresta alkuluvusta, pitäen nämä luvut salaisina. Viestit voidaan salata kuka tahansa julkisen avaimen avulla, mutta vain ne, jotka tuntevat yksityisen avaimen, voivat purkaa ne. Salaus perustuu suurten alkulukujen tulojen hajottamisen vaikeuteen, tunnettuna "hajotelmaprobleemina".

RSA-algoritmi generoi julkisen ja yksityisen avaimen seuraavasti:
1. Generoi alkuluvut p ja q.
2. Laske n = p*q
3. Laske Carmichaelin totienttifunktio λ(n) = lcm(p − 1, q − 1). lcm(a,b) on kahden kokonaisluvun a ja b pienin yhteinen jaettava.
4. Laske alkuluku e suurimmalla yhteisellä tekijällä (gcd).
5. Laske d siten, että (d*e) mod λ = 1.
- RSA:n julkinen avain on pari e, n.
- RSA:n yksityinen avain on pari d, n.

## Ohjelmassa käytetään seuraavia algoritmeja:

- Miller–Rabinin alkulukutesti varmistaa todennäköisyydellisesti, onko luku alkuluku. Sen aikavaativuus on O(k log3 n), missä k on testattujen kierrosten määrä ja n on testattu luku.
- Laajennettu Eukleideen algoritmi laskee suurimman yhteisen jaollisen lisäksi Bézout'n identiteetin kertoimet x ja y. Sen aikavaativuus on O(log min(a, b)), missä a ja b ovat annetut kokonaisluvut.

## Parannuksia
Graafisen käyttöliittymän lisääminen voi parantaa ohjelman käyttökokemusta. Ohjelmaa voisi kehittää myös niin, että se pystyisi salamaan muutakin kun vain tekstiä.



## Lähteet:

RSA (kryptosysteemi)
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Miller-Rabinin algoritmi
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

Laajennettu Eukleideen algoritmi
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

