
import sqlite3

# Connexion à la base de données (création si elle n'existe pas)
conn = sqlite3.connect('gestion_cours.db')
cursor = conn.cursor()

# Création de la table pour les filières
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filieres (
        id INTEGER PRIMARY KEY,
        nom TEXT
    )
''')

# Création de la table pour les niveaux
cursor.execute('''
    CREATE TABLE IF NOT EXISTS niveaux (
        id INTEGER PRIMARY KEY,
        nom TEXT
    )
''')

# Création de la table pour les matières
cursor.execute('''
    CREATE TABLE IF NOT EXISTS matieres (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        volume_horaire INTEGER,
        volume_effectif INTEGER,
        pourcentage REAL
    )
''')

# Création de la table pour la progression des cours
cursor.execute('''
    CREATE TABLE IF NOT EXISTS progression_cours (
        id INTEGER PRIMARY KEY,
        matiere_id INTEGER,
        date DATE,
        progression INTEGER,
        FOREIGN KEY (matiere_id) REFERENCES matieres(id)
    )
''')

# Exemple d'insertion de données dans la table filieres
cursor.execute("INSERT INTO filieres (nom) VALUES ('Informatique')")
cursor.execute("INSERT INTO filieres (nom) VALUES ('Génie Civil')")

# Exemple d'insertion de données dans la table niveaux
cursor.execute("INSERT INTO niveaux (nom) VALUES ('Licence')")
cursor.execute("INSERT INTO niveaux (nom) VALUES ('Master')")

# Exemple d'insertion de données dans la table matieres
cursor.execute("INSERT INTO matieres (nom, volume_horaire, volume_effectif, pourcentage) VALUES ('Mathématiques', 60, 55, 90.0)")
cursor.execute("INSERT INTO matieres (nom, volume_horaire, volume_effectif, pourcentage) VALUES ('Programmation', 80, 75, 85.0)")

# Exemple d'insertion de données dans la table progression_cours
cursor.execute("INSERT INTO progression_cours (matiere_id, date, progression) VALUES (1, '2024-01-15', 50)")
cursor.execute("INSERT INTO progression_cours (matiere_id, date, progression) VALUES (2, '2024-01-15', 70)")

# Validation des modifications et fermeture de la connexion à la base de données
conn.commit()
conn.close()
