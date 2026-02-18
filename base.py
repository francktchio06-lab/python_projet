import sqlite3

def creer_base_de_donnees():
    # Connexion a la base de donnees
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    # Creation de la table filieres
    cursor.execute('''CREATE TABLE filieres
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nom TEXT)''')

    # Creation de la table matieres
    cursor.execute('''CREATE TABLE matieres
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nom TEXT)''')

    # Fermeture de la connexion
    conn.close()


def ajouter_filieres():
    # Connexion à la base de donnees
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    # Liste des filieres
    filieres = [
        'gestion', 'industrielle', 'santer', 'engineering', 'technologie', 'business',
        'classe préparatoire', 'licence délocalisee', 'cycle ingénieur'
    ]

    # Insertion des filieres dans la table filieres
    for filiere in filieres:
        cursor.execute("INSERT INTO filieres (nom) VALUES (?)", (filiere,))

    # Fermeture de la connexion
    conn.close()


def ajouter_matieres_universitaires():
    # Connexion à la base de données
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    # Liste des matieres universitaires
    matieres_universitaires = [
        'mathématiques', 'physique', 'chimie', 'biologie', 'informatique', 'langues',
        'histoire', 'géographie', 'philosophie', 'psychologie', 'sociologie',
        'economie', 'droit', 'médecine', 'pharmacie', 'ingénierie', 'architecture',
        'communication', 'journalisme', 'arts', 'musique', 'theatre', 'cinema',
        'sciences politiques', 'sciences de l\'education', 'sciences de la santer',
        'sciences de l\'environnement', 'sciences humaines', 'sciences sociales',
        'sciences de gestion', 'sciences du sport', 'sciences de l\'information',
        'sciences du langage', 'sciences de l\'ingénieur', 'sciences economiques et de gestion'
    ]

    # Insertion des matières universitaires dans la table matieres
    for matiere in matieres_universitaires:
        cursor.execute("INSERT INTO matieres (nom) VALUES (?)", (matiere,))

    # Fermeture de la connexion
    conn.close()








