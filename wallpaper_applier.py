# wallpaper_applier.py
import os
import ctypes
from error_handler import kasittele_virhe

def aseta_taustakuva(kuvan_polku):
    """Vaihtaa Windowsin työpöydän taustakuvan annetusta polusta."""
    if not kuvan_polku or not os.path.exists(kuvan_polku):
        kasittele_virhe("Tiedosto", "Taustakuvatiedostoa ei ole olemassa tai polku on tyhjä.")
        return False

    print("🖼️ Säädetään työpöydän taustakuvaa...")
    try:
        # Käytetään Windowsin SystemParametersInfoW-rajapintaa (SPI_SETDESKWALLPAPER = 20)
        tulos = ctypes.windll.user32.SystemParametersInfoW(20, 0, kuvan_polku, 3)
        if tulos:
            print("🎉 Työpöydän taustakuva vaihdettu onnistuneesti!")
            return True
        else:
            kasittele_virhe("Windows API", "Käyttöjärjestelmä hylkäsi taustakuvan vaihdon.")
    except Exception as e:
        kasittele_virhe("Järjestelmäkutsu", f"Kriittinen virhe taustakuvan asetuksessa: {e}")
    return False
