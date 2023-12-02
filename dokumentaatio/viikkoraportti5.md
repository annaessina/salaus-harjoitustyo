#Viikkoraportti5

Tällä viikolla: 

- Testataksesi toimintoa checkIfPrimeNumberMillerRabin(n), käytin suurta alkulukua M(1279), joka on yhtä suuri kuin 2^1279 - 1. Tämä on yksi Mersennen alkuluvuista, jotka löydettiin vuonna 1952 Raphael M. Robinsonin toimesta (lähde: https://www.mersenne.org/primes/).

- Miller-Rabin-algoritmin toistojen määrää on lisätty 40:een, jotta olisi riittävän suuri todennäköisyys, että luku on alkuluku.

- Alkuluvun etsimiseksi käyttämällä funktiota primeNumberGeneration(num1,num2), käytin väliä 21278 ja 22282. Tässä välissä on vähintään kolme alkulukua: M(1279), M(2203) ja M(2281).

- Testataksesi toimintoa primeNumberGeneration(num1,num2), käytin samaa väliä 21278 ja 22282.

- Ensi viikolla laajennan vielä hieman sovelluksen toimintoja ja käyttöliittymää.

Käytetyt tunnit 12h