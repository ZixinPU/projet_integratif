import sqlite3

# 连接到数据库
conn = sqlite3.connect('./db/donnee.db')

# 数据
themes = [(1, 'TV'), (2, 'Smartphone'), (3, 'Casque audio'), (4, 'Enceinte Bluetooth'), (5, 'Consoles de Jeux-Vidéo'),
          (6, 'Moniteur/Ecran PC'), (7, 'Laptop'), (8, 'Ecouteur Bluetooth'), (9, 'Tablette')]

# 插入数据
cursor = conn.cursor()
for theme in themes:
    cursor.execute("INSERT INTO Thème (IdThème, NomThème) VALUES (?, ?)", theme)

# 提交更改并关闭连接
conn.commit()
conn.close()