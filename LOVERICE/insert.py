import sqlite3

# Connectez à la base de données
conn = sqlite3.connect('./db/donnee.db')

# données à insérer
themes = [(1, 'TV'), (2, 'Smartphone'), (3, 'Casque audio'), (4, 'Enceinte Bluetooth'), (5, 'Consoles de Jeux-Vidéo'),
          (6, 'Moniteur/Ecran PC'), (7, 'Laptop'), (8, 'Ecouteur Bluetooth'), (9, 'Tablette')]

# insérer des données
cursor = conn.cursor()
for theme in themes:
    cursor.execute("INSERT INTO Thème (IdThème, NomThème) VALUES (?, ?)", theme)

# Valider les modifications et fermer la connexion
conn.commit()
conn.close()