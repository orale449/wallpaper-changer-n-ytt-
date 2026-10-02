# error_handler.py
import sys

def kasittele_virhe(virhetyyppi, viesti, poistutaanko=False):
    """Yhteinen funktio kaikkien ohjelman virheiden käsittelyyn ja tulostamiseen."""
    tuloste = f"⚠️ [VIRHE - {virhetyyppi.upper()}]: {viesti}"
    print(tuloste, file=sys.stderr)
    
    if poistutaanko:
        print("Ohjelman suoritus jouduttiin keskeyttämään virheen vuoksi.", file=sys.stderr)
        sys.exit(1)
