import os
from datetime import datetime

def convertir_rs3_vers_gpx(fichier_rs3, fichier_gpx):
    try:
        with open(fichier_rs3, 'r') as fichier:
            lignes = fichier.readlines()

        # Début du fichier GPX
        gpx_contenu = """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="PythonGPX" xmlns="http://www.topografix.com/GPX/1/1">
<trk>
  <name>Parcours Converti</name>
  <trkseg>"""

        for ligne in lignes:
            # Nettoyer et extraire les valeurs selon le format RS3
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue  # Ignorer les lignes vides ou commentaires

            # Extraire les champs en se basant sur le format donné
            try:
                elements = ligne.split()
                if len(elements) < 4:
                    print(f"Ligne ignorée (format incorrect) : {ligne}")
                    continue
                time_str = elements[0] + "T" + elements[1] + "Z"  # Combinaison date et heure
                latitude = elements[2]  # 3e colonne : latitude
                longitude = elements[3]  # 4e colonne : longitude
                elevation = elements[4]  # 5e colonne : élévation

                # Ajouter un point GPS avec temps et élévation
                gpx_contenu += f"    <trkpt lat=\"{latitude.strip()}\" lon=\"{longitude.strip()}\">\n"
                gpx_contenu += f"      <ele>{elevation.strip()}</ele>\n"
                gpx_contenu += f"      <time>{time_str.strip()}</time>\n"
                gpx_contenu += "    </trkpt>\n"
            except ValueError:
                print(f"Ligne ignorée (erreur de parsing) : {ligne}")

        # Fin du fichier GPX
        gpx_contenu += "  </trkseg>\n</trk>\n</gpx>"

        # Écrire dans le fichier GPX dans le dossier spécifié
        sortie_path = "C:\\Users\\seyfa\\OneDrive\\Documents\\sortie"
        if not os.path.exists(sortie_path):
            os.makedirs(sortie_path)  # Crée le dossier si nécessaire
        fichier_gpx_complet = os.path.join(sortie_path, fichier_gpx)

        try:
            with open(fichier_gpx_complet, 'w') as fichier:
                fichier.write(gpx_contenu)

            print(f"Le fichier GPX a été créé avec succès : {fichier_gpx_complet}")
        except IOError as e:
            print(f"Erreur lors de l'écriture du fichier : {e}")

    except FileNotFoundError:
        print(f"Le fichier RS3 spécifié est introuvable : {fichier_rs3}")
    except Exception as e:
        print(f"Erreur : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    fichier_rs3 = input("Entrez le chemin du fichier RS3 contenant les coordonnées : ")
    fichier_gpx = input("Entrez le nom du fichier GPX de sortie (ex: sortie.gpx) : ")

    convertir_rs3_vers_gpx(fichier_rs3, fichier_gpx)
