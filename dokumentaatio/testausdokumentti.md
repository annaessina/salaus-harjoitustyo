# Testausdokumentti

## Testaus

Kaikki testit on luotu testaamaan kaikkia ohjelman toimintoja erilaisissa skenaarioissa eri syötteillä.

## test_calculate_gcd()

Tämä testi tarkistaa calculate_gcd() - funktion oikean toiminnon suurimman yhteisen tekijän määrittämiseksi.
Useita erilaisia syötteitä syötetään, mukaan lukien suuria alkulukuja M(1279) ja M(2203).

## test_checkIfPrimeNumberMillerRabin()

Tämä testi tarkistaa checkIfPrimeNumberMillerRabin() - funktion, joka käyttää Miller Rabin - algoritmia määrittääkseen, onko annettu luku alkuluku.
Useita erilaisia syötteitä syötetään, mukaan lukien suuria alkulukuja M(1279) ja M(2203)
sekä niiden tulo M(1279) * M(2203).

## test_primeNumberGeneration()

Tämä testi tarkistaa primeNumberGeneration() - funktion oikean alkuluvun löytämiseksi annetulla alueella.
Useita erilaisia syötteitä syötetään, mukaan lukien alue, jossa on suuria lukuja 2 ** 1023: sta 2 ** 1024: ään.

## Testaus ohjeet 

Yksikkötestit saa ajettua komennolla:

```bash
 poetry run coverage run --branch -m pytest src
```
Testikattavuusraportin saa:

```bash
poetry run coverage html
```
Komentoriville testikattavuusraportin saa:

```bash
poetry run coverage report -m
```
