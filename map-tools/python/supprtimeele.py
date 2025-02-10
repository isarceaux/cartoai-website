import os
import re

def supprimer_passages_ele_time_dossier(dossier_gpx, dossier_sortie):
    try:
        # Vérifier si le dossier source existe
        if not os.path.exists(dossier_gpx):
            print(f"Le dossier spécifié est introuvable : {dossier_gpx}")
            return

        # Créer le dossier de sortie s'il n'existe pas
        if not os.path.exists(dossier_sortie):
            os.makedirs(dossier_sortie)

        # Parcourir tous les fichiers GPX dans le dossier source
        for fichier in os.listdir(dossier_gpx):
            if fichier.endswith(".gpx"):
                chemin_fichier = os.path.join(dossier_gpx, fichier)

                # Lire le contenu du fichier GPX
                with open(chemin_fichier, 'r') as fichier_gpx:
                    contenu = fichier_gpx.read()

                # Supprimer les passages de la forme <ele>float</ele> et <time>date</time>
                contenu_modifie = re.sub(r"<ele>[-+]?[0-9]*\.?[0-9]+</ele>", "", contenu)
                contenu_modifie = re.sub(r"<time>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z</time>", "", contenu_modifie)

                # Préparer le chemin du fichier modifié
                chemin_sortie = os.path.join(dossier_sortie, fichier)

                # Écrire le contenu modifié dans le nouveau fichier
                with open(chemin_sortie, 'w') as fichier_modifie:
                    fichier_modifie.write(contenu_modifie)

                print(f"Fichier modifié enregistré : {chemin_sortie}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    dossier_gpx = input("Entrez le chemin du dossier contenant les fichiers GPX : ")
    dossier_sortie = "C:\\Users\\seyfa\\OneDrive\\Bureau\\stage\\gpx\\temp"

    supprimer_passages_ele_time_dossier(dossier_gpx, dossier_sortie)
