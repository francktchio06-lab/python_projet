import sqlite3
import matplotlib.pyplot as plt
def diagrame():
    

# Connexion à la base de données
    conn = sqlite3.connect('my_data_base.db')
    curseur = conn.cursor()

# Récupération des données de chaque matière par semestre
    curseur.execute('''
        SELECT m.nom, m.semestre, COUNT(*)
        FROM Matiere m
        GROUP BY m.nom, m.semestre
        ORDER BY m.semestre, m.nom
                      ''')
    donnees = curseur.fetchall()
    conn.close()

# Préparation des données pour le diagramme à barres
    matieres = []
    semestres = []
    effectifs = []

    for data in donnees:
        matieres.append(data[0])
        semestres.append(data[1])
        effectifs.append(data[2])

# Création du diagramme à barres
        x = range(len(matieres))
        width = 0.35

    fig, ax = plt.subplots()
    rects = ax.bar(x, effectifs, width)

# Ajout des étiquettes d'axe et de titre
    ax.set_xlabel('Matière')
    ax.set_ylabel('Effectif')
    ax.set_title('Effectif des matières par semestre')

# Ajout des étiquettes des matières en x
    ax.set_xticks(x)
    ax.set_xticklabels(matieres, rotation=90)

# Affichage du diagramme à barres
    plt.show()
