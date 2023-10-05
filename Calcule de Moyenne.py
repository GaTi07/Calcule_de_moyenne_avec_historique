# Tiago
# Importez les bibliothèques tkinter nécessaires
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

# Liste pour stocker l'historique des calculs et des moyennes
historique = []

# Palette de couleurs personnalisée
palette = {
    'federal_blue': '#03045e',
    'marian_blue': '#023e8a',
    'honolulu_blue': '#0077b6',
    'blue_green': '#0096c7',
    'pacific_cyan': '#00b4d8',
    'vivid_sky_blue': '#48cae4',
    'non_photo_blue': '#90e0ef',
    'non_photo_blue_2': '#ade8f4',
    'light_cyan': '#caf0f8',
}

expression_calcul = ""

# Fonction pour calculer la moyenne
def calculer_moyenne():
    global expression_calcul
    valeurs = entry.get()

    if not valeurs:
        messagebox.showerror("Erreur", "Veuillez entrer au moins un nombre.")
        return

    valeurs = valeurs.split(',')

    try:
        valeurs = [float(val.strip()) for val in valeurs]
        somme = sum(valeurs)
        nombre_de_valeurs = len(valeurs)
        moyenne = somme / nombre_de_valeurs
        expression_calcul = f"({'+'.join(map(str, valeurs))}) / {nombre_de_valeurs}"

        resultat_label.config(text=f"Moyenne : {moyenne:.2f}")

        # Ajoutez le calcul à la colonne "Action" et la moyenne à la colonne "Valeur" de l'historique
        historique.append((expression_calcul, f"{moyenne:.2f}"))
        afficher_historique()

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

# Fonction pour afficher l'historique des calculs et des moyennes dans le tableau
def afficher_historique():
    historique_tree.delete(*historique_tree.get_children())
    for i, (action, valeur) in enumerate(historique, start=1):
        historique_tree.insert("", "end", values=(action, valeur))

# Fonction pour enregistrer tous les logs dans un fichier texte
def enregistrer_tout_logs():
    try:
        fichier = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])

        if fichier:
            # En-tête du tableau
            fichier.write("Action\tValeur\n")

            for i, (action, valeur) in enumerate(historique, start=1):
                # Écrivez chaque ligne du tableau avec des onglets pour séparer les colonnes
                fichier.write(f"{action}\t{valeur}\n")

            messagebox.showinfo("Succès", "Tous les logs enregistrés avec succès dans le fichier.")
            fichier.close()
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'enregistrement des logs : {str(e)}")

# Fonction pour afficher les crédits
def afficher_credits():
    global fenetre
    fenetre.withdraw()  # Masquer la fenêtre principale

    # Créez une nouvelle fenêtre pour les crédits
    fenetre_credits = tk.Toplevel()
    fenetre_credits.title("Crédits")

    largeur_fenetre_credits = 400
    hauteur_fenetre_credits = 200

    fenetre_credits.geometry(f"{largeur_fenetre_credits}x{hauteur_fenetre_credits}")

    cadre_credits = tk.Frame(fenetre_credits, bg=palette['federal_blue'])
    cadre_credits.pack(fill="both", expand=True)

    # Ajoutez les informations de crédits
    credits_label = tk.Label(cadre_credits, text="Crédits", font=("Helvetica", 16, "bold"), bg=palette['federal_blue'], fg=palette['vivid_sky_blue'])
    credits_label.pack(pady=20)

    auteur_label = tk.Label(cadre_credits, text="Auteur : PEREIRA TIAGO", font=("Helvetica", 12), bg=palette['federal_blue'], fg=palette['vivid_sky_blue'])
    auteur_label.pack()

    # Bouton pour revenir en arrière
    retour_button = tk.Button(cadre_credits, text="Retour", command=lambda: retourner_fenetre(fenetre_credits), font=("Helvetica", 12), bg=palette['blue_green'], fg="white", borderwidth=3)
    retour_button.pack(pady=10)

    fenetre_credits.mainloop()

# Fonction pour revenir à la fenêtre principale depuis la fenêtre des crédits
def retourner_fenetre(fenetre_a_afficher):
    global fenetre
    fenetre_a_afficher.destroy()  # Fermer la fenêtre actuelle
    fenetre.deiconify()  # Réafficher la fenêtre principale

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de moyenne avec historique")

largeur_fenetre = 600
hauteur_fenetre = 580  # Ajustement de la hauteur minimale

fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
fenetre.minsize(width=largeur_fenetre, height=hauteur_fenetre)  # Définir la taille minimale

cadre_principal = tk.Frame(fenetre, bg=palette['federal_blue'])
cadre_principal.pack(fill="both", expand=True)

instructions_label = tk.Label(cadre_principal, text="Entrez les nombres séparés par des virgules :", font=("Helvetica", 12), bg=palette['federal_blue'], fg=palette['vivid_sky_blue'])
instructions_label.pack(pady=10)

entry = tk.Entry(cadre_principal, font=("Helvetica", 12), borderwidth=3)
entry.pack(pady=10)

# Créez un cadre pour les boutons
cadre_boutons = tk.Frame(cadre_principal, bg=palette['federal_blue'])
cadre_boutons.pack(fill="both", expand=True)

calculer_button = tk.Button(
    cadre_boutons,
    text="Calculer la moyenne",
    command=calculer_moyenne,
    font=("Helvetica", 12),
    bg=palette['blue_green'],
    fg="white",
    borderwidth=3
)
calculer_button.pack(padx=10, pady=10)

# Créez un cadre pour afficher le résultat de la moyenne
cadre_resultat = tk.Frame(cadre_principal, bg=palette['federal_blue'])
cadre_resultat.pack(pady=10)

resultat_label = tk.Label(cadre_resultat, text="", font=("Helvetica", 14, "bold"), bg=palette['federal_blue'], fg=palette['vivid_sky_blue'], borderwidth=3)
resultat_label.pack()

# Créez un cadre pour le tableau d'historique
cadre_historique = tk.Frame(cadre_principal, bg=palette['federal_blue'])
cadre_historique.pack(pady=10, fill="both", expand=True)

# Créez une étiquette pour l'historique des calculs et des moyennes
historique_label = tk.Label(cadre_historique, text="Historique des calculs et des moyennes :", font=("Helvetica", 12), bg=palette['federal_blue'], fg=palette['vivid_sky_blue'])
historique_label.pack()

# Créez un tableau (Treeview) pour afficher l'historique des calculs et des moyennes
historique_tree = ttk.Treeview(cadre_historique, columns=("Action", "Valeur"), show="headings")
historique_tree.heading("Action", text="Action")
historique_tree.heading("Valeur", text="Valeur")
historique_tree.pack(fill="both", expand=True)

# Créez un cadre pour les boutons Enregistrer tous les Logs et Crédits
cadre_boutons2 = tk.Frame(cadre_principal, bg=palette['federal_blue'])
cadre_boutons2.pack(fill="both", expand=True)

enregistrer_tout_logs_button = tk.Button(
    cadre_boutons2,
    text="Enregistrer tous les Logs",
    command=enregistrer_tout_logs,
    font=("Helvetica", 12),
    bg=palette['blue_green'],
    fg="white",
    borderwidth=3
)
enregistrer_tout_logs_button.pack(padx=10, pady=10)

credits_button = tk.Button(
    cadre_boutons2,
    text="Crédits",
    command=afficher_credits,
    font=("Helvetica", 12),
    bg=palette['blue_green'],
    fg="white",
    borderwidth=3
)
credits_button.pack(padx=10, pady=10)

# Lancer la boucle principale
fenetre.mainloop()



