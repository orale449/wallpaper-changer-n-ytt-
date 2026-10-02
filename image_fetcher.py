# image_fetcher.py
import os
import urllib.request
from datetime import datetime
from wallpaper_config import WALLPAPER_URL, DOWNLOAD_DIR
from error_handler import kasittele_virhe

def varmista_kansio():
    """Luo tallennuskansion Pictures-hakemistoon, jos sitä ei ole olemassa."""
    try:
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)
            print(f"📁 Luotu uusi kansio kuville: {DOWNLOAD_DIR}")
    except OSError as e:
        kasittele_virhe("Kansiorakenne", f"Kansiota ei voitu luoda: {e}", poistutaanko=True)

def hae_ja_tallenna_kuva():
    """Hakee kuvan netistä ja tallentaa sen kansioon uniikilla nimellä."""
    varmista_kansio()
    
    # Luodaan tiedostonimi aikaleiman avulla (esim. wallpaper_20261002_131000.jpg)
    # Tämän ansiosta uudet kuvat eivät ikinä ylikirjoita vanhoja, vaan ne säästyvät omassa kansiossaan!
    aikaleima = datetime.now().strftime("%Y%m%d_%H%M%S")
    kuvan_nimi = f"wallpaper_{aikaleima}.jpg"
    tallennuspolku = os.path.join(DOWNLOAD_DIR, kuvan_nimi)
    
    print("🌐 Etsitään ja ladataan uutta kuvaa netistä...")
    try:
        pyynto = urllib.request.Request(WALLPAPER_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(pyynto, timeout=15) as vastaus, open(tallennuspolku, 'wb') as tiedosto:
            tiedosto.write(vastaus.read())
        print(f"💾 Kuva tallennettu onnistuneesti polkuun: {kuvan_nimi}")
        return tallennuspolku
    except urllib.error.URLError as e:
        kasittele_virhe("Verkko", f"Yhteys epäonnistui tai URL on väärä: {e}")
    except TimeoutError:
        kasittele_virhe("Aikakatkaisu", "Palvelin ei vastannut annetussa ajassa.")
    except Exception as e:
        kasittele_virhe("Lataus", f"Tuntematon virhe kuvan tallennuksessa: {e}")
    return None
