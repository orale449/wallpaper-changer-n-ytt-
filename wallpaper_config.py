# wallpaper_config.py
import os

# URL-osoite, josta satunnainen hieno maisemakuva haetaan
WALLPAPER_URL = "https://unsplash.com"

# Kansio, johon ladatut taustakuvat tallennetaan pysyvästi talteen
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Pictures", "MyAutoWallpapers")
