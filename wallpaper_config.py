# wallpaper_config.py
import os

# URL-osoite, joka antaa suoraan korkealaatuisen maisemakuvan ilman estoja (Picsum Photos)
WALLPAPER_URL = "https://picsum.photos"

# Kansio, johon ladatut taustakuvat tallennetaan pysyvästi talteen
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Pictures", "MyAutoWallpapers")
