# Automatic Wallpaper Changer

## 🎯 Ohjelman tarkoitus
Tämä ohjelma hakee automaattisesti korkealaatuisen kuvan verkosta, tallentaa sen talteen käyttäjän omaan kuvakansioon uniikilla aikaleimalla ja asettaa sen tietokoneen työpöydän taustakuvaksi. Ohjelma on jaettu useaan erilliseen moduuliin parhaan koodauskäytännön mukaisesti.

## 📁 Projektin rakenne (Useampi skriptitiedosto)
Ohjelma on jaettu viiteen tiedostoon, joilla kaikilla on oma selkeä vastuualueensa:
1. `wallpaper_config.py` - Sisältää ohjelman asetukset (URL ja tallennuskansio).
2. `error_handler.py` - Keskistetty moduuli kaikkien virhetilanteiden käsittelyyn.
3. `image_fetcher.py` - Vastaa kuvien hakemisesta netistä ja tallentamisesta uniikeilla nimillä.
4. `wallpaper_applier.py` - Vastaa taustakuvan päivittämisestä käyttöjärjestelmään.
5. `main.py` - Pääohjelma, joka sitoo kaikki moduulit yhteen ja ajaa prosessin.

## 💻 Järjestelmävaatimukset
* **Käyttöjärjestelmä:** Windows (käyttää Windowsin sisäistä `user32.dll`-rajapintaa).
* **Ajoaika:** Python 3.x.
* **Kirjastot:** Standardikirjastot (`os`, `sys`, `ctypes`, `urllib`, `datetime`). Ei vaadi ulkopuolisia `pip`-asennuksia.

## 🚀 Siirrettävyys (Portability)
Ohjelma on täysin siirrettävä. Se käyttää `os.path.expanduser("~")` -funktiota, joten se tunnistaa automaattisesti minkä tahansa Windows-tietokoneen nykyisen käyttäjän `Pictures` (Kuvat) -kansion ja luo sinne alikansion `MyAutoWallpapers`. Mitään polkuja ei tarvitse muuttaa käsin, jos ohjelman siirtää toiselle koneelle.

## ⚠️ Mahdolliset rajoitteet ja virheentarkastus
* **Erillinen virheentarkastus:** Kaikki mahdolliset virheet (verkkokatkokset, puuttuvat kansiot, käyttöjärjestelmävirheet) ohjataan `error_handler.py`-moduulille, joka estää ohjelman kaatumisen ja antaa selvän suomenkielisen virheilmoituksen.
* **Verkkoyhteys:** Vaatii internetyhteyden kuvan lataamiseen. Jos verkkoa ei ole, virheentarkastus huomaa sen, eikä ohjelma yritä väkisin vaihtaa taustakuvaa.
* **Käyttöjärjestelmä:** Rajoitettu Windowsille `ctypes.windll`-kutsun vuoksi.

## 🛠️ Kehitysajatukset
1. **Monialustatuki:** Tehdään taustakuvan asetuksesta dynaaminen tunnistamalla onko kyseessä macOS, Linux vai Windows.
2. **Kuvahistoria / Selaus:** Luodaan yksinkertainen käyttöliittymä, jolla käyttäjä voi selata kansioon kertyneitä vanhoja ladattuja kuvia ja palauttaa jonkin niistä takaisin taustakuvaksi.
