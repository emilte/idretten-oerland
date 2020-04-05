
DEV_SETTINGS = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r46@%640s-p^c^ni3ea(ajgplhe)uq*woa_3ylyq9%fb21yb_g'

GOOGLE_CLIENT_ID = "351210640104-supqlac2upkdjia4qoc1sugf0ctq0ilb.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "J9IaSe4lwjzT-J7uyXCdgfOZ"

SITE_ID = 8

if DEV_SETTINGS:
    try:
        from .dev_settings import *
        print("|\n== local_settings was overwritten by dev_settings ==")
    except:
        pass
