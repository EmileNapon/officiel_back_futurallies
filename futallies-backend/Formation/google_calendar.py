# test_load_credentials.py

import os
from google.oauth2 import service_account
import logging

# Le chemin vers ton fichier de credentials
GOOGLE_CREDENTIALS_FILE = '../service_account.json'

# Logger pour les messages
logger = logging.getLogger(__name__)

# La fonction à tester
def load_credentials():
    """Vérifie si le fichier de credentials est bien présent et le charge."""
    if not os.path.exists(GOOGLE_CREDENTIALS_FILE):
        logger.error(f"Le fichier de credentials n'a pas été trouvé à l'emplacement : {GOOGLE_CREDENTIALS_FILE}")
        return None
    try:
        credentials = service_account.Credentials.from_service_account_file(
            GOOGLE_CREDENTIALS_FILE,
            scopes=["https://www.googleapis.com/auth/calendar"]
        )
        logger.info(f"Credentials chargés avec succès depuis {GOOGLE_CREDENTIALS_FILE}")
        return credentials
    except Exception as e:
        logger.error(f"Erreur lors du chargement des credentials : {str(e)}")
        return None


# Test de la fonction
if __name__ == "__main__":
    credentials = load_credentials()
    if credentials:
        print("Credentials chargés avec succès")
    else:
        print("Erreur lors du chargement des credentials")
