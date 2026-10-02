# main.py
from image_fetcher import hae_ja_tallenna_kuva
from wallpaper_applier import aseta_taustakuva

def suorita_automaatio():
    print("========================================")
    print("  AUTOMATIC WALLPAPER CHANGER KÄYNNISTYY  ")
    print("========================================\n")
    
    # 1. Etsitään ja tallennetaan kuva omasta moduulistaan
    ladattu_kuva = hae_ja_tallenna_kuva()
    
    # 2. Jos kuva saatiin haettua onnistuneesti, vaihdetaan se taustakuvaksi
    if ladattu_kuva:
        aseta_taustakuva(ladattu_kuva)
    else:
        print("\n Taustakuvaa ei voitu vaihtaa, koska kuvan haku epäonnistui.")
        
    print("\n========================================")
    print("  SUORITUS PÄÄTTYNYT                    ")
    print("========================================")

if __name__ == "__main__":
    suorita_automaatio()
