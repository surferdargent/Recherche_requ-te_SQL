import tkinter as tk
import csv

def rechercher():
    # Ouvrir le fichier CSV en lecture avec l'encodage UTF-8
    with open('fichier.csv', 'r', encoding='iso-8859-1') as f:
        reader = csv.DictReader(f)
        requetes = []

        # Vérifier si le champ de saisie n'est pas vide
        if motcle.get():
            # Parcourir chaque ligne du fichier CSV et vérifier si le mot-clé est présent dans la colonne "Commentaires"
            for row in reader:
                if row['Commentaires'].lower().find(motcle.get().lower()) != -1 or row['Requête SQL'].lower().find(motcle.get().lower()) != -1:


                    requetes.append((row['Commentaires'], row['Requête SQL']))

        # Afficher les requêtes SQL correspondantes dans la zone de texte
        resultats.delete('1.0', tk.END)
        if len(requetes) == 0:
            resultats.insert(tk.END, "Aucune requête ne correspond à votre recherche.")
        else:
            for commentaire, requete in requetes:
                resultats.insert(tk.END, commentaire + "\n")
                resultats.insert(tk.END, requete + "\n\n")

def ajouter_requete():
    # Créer une nouvelle fenêtre pour ajouter une requête
    fenetre_ajout = tk.Toplevel(fenetre)
    fenetre_ajout.title("Ajouter une requête")

    # Créer les widgets
    etiquette_commentaire = tk.Label(fenetre_ajout, text="Commentaire :")
    commentaire = tk.Entry(fenetre_ajout, width=100)
    etiquette_requete = tk.Label(fenetre_ajout, text="Requête SQL :")
    requete = tk.Text(fenetre_ajout, height=10)
    bouton_enregistrer = tk.Button(fenetre_ajout, text="Enregistrer", command=lambda: enregistrer_requete(commentaire.get(), requete.get(1.0, tk.END)))

    # Ajouter les widgets à la fenêtre
    etiquette_commentaire.pack()
    commentaire.pack()
    etiquette_requete.pack()
    requete.pack()
    bouton_enregistrer.pack()

    def enregistrer_requete(commentaire, requete_sql):
    # Ajouter la nouvelle requête au fichier CSV
        with open('fichier.csv', 'a', newline='', encoding='iso-8859-1') as f:
            writer = csv.writer(f)
            writer.writerow([commentaire, requete_sql])

      

        # Fermer la fenêtre d'ajout de requête
        fenetre_ajout.destroy()

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Recherche de requêtes SQL")

# Créer les widgets
etiquette = tk.Label(fenetre, text="Entrez un mot-clé à rechercher :")
motcle = tk.Entry(fenetre,width=100)
bouton_rechercher = tk.Button(fenetre, text="Rechercher", command=rechercher)
bouton_ajouter = tk.Button(fenetre, text="Mise à jour requête", command=ajouter_requete)
resultats = tk.Text(fenetre, width=200)

# Ajouter les widgets à la fenêtre
etiquette.pack()
motcle.pack()
bouton_rechercher.pack()
bouton_ajouter.pack()
resultats.pack()

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
