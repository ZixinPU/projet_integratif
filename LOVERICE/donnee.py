import sqlite3

#sqlite

# Se connecter à une base de données, la créer si elle n'existe pas
conn = sqlite3.connect('./db/donnee.db')

# 创建一个游标对象，用于执行SQL语句
c = conn.cursor()

# 创建Site_Marchand表格
c.execute('''CREATE TABLE Site_Marchand
             (URLSite VARCHAR(255) PRIMARY KEY NOT NULL,
             NomSite VARCHAR(255) NOT NULL)''')

# 创建Utilisateur表格
c.execute('''CREATE TABLE Utilisateur
             (idUtilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
             IdThème INTEGER NOT NULL,
             FOREIGN KEY(IdThème) REFERENCES Thème(IdThème))''')

# 创建Service_Client表格
c.execute('''CREATE TABLE Service_Client
             (IdSAV INTEGER PRIMARY KEY AUTOINCREMENT)''')

# 创建Thème表格  
c.execute('''CREATE TABLE Thème
             (IdThème INTEGER PRIMARY KEY AUTOINCREMENT,
             NomThème VARCHAR(255) NOT NULL)''')

# 创建Article表格
c.execute('''CREATE TABLE Article
             (IdArt INTEGER PRIMARY KEY AUTOINCREMENT,
             NomArt VARCHAR(255) NOT NULL,
             PrixArt DECIMAL(10, 2) NOT NULL,
             descriptionArt TEXT NOT NULL,
             URLArt VARCHAR(255) NOT NULL,
             IdThème INTEGER NOT NULL,
             FOREIGN KEY(IdThème) REFERENCES Thème(IdThème))''')

# 创建Proposer表格
c.execute('''CREATE TABLE Proposer
             (IdArt INTEGER NOT NULL,
             URLSite VARCHAR(255) NOT NULL,
             PRIMARY KEY(IdArt, URLSite),
             FOREIGN KEY(IdArt) REFERENCES Article(IdArt),
             FOREIGN KEY(URLSite) REFERENCES Site_Marchand(URLSite))''')

# 创建Suggérer表格
c.execute('''CREATE TABLE Suggérer
             (IdArt INTEGER NOT NULL,
             idUtilisateur INTEGER NOT NULL,
             PRIMARY KEY(IdArt, idUtilisateur),
             FOREIGN KEY(IdArt) REFERENCES Article(IdArt),
             FOREIGN KEY(idUtilisateur) REFERENCES Utilisateur(idUtilisateur))''')

# 创建Rechercher表格
c.execute('''CREATE TABLE Rechercher
             (IdArt INTEGER NOT NULL,
             idUtilisateur INTEGER NOT NULL,
             PRIMARY KEY(IdArt, idUtilisateur),
             FOREIGN KEY(IdArt) REFERENCES Article(IdArt),
             FOREIGN KEY(idUtilisateur) REFERENCES Utilisateur(idUtilisateur))''')

# 创建Contacter表格
c.execute('''CREATE TABLE Contacter
             (idUtilisateur INTEGER NOT NULL,
             IdSAV INTEGER NOT NULL,
             mailUtil VARCHAR(255) NOT NULL,
             NomUtil VARCHAR(255) NOT NULL,
             NumUtil VARCHAR(255) NOT NULL,
             PRIMARY KEY(idUtilisateur, IdSAV),
             FOREIGN KEY(idUtilisateur) REFERENCES Utilisateur(idUtilisateur),
             FOREIGN KEY(IdSAV) REFERENCES Service_Client(IdSAV))''')


# 提交更改
conn.commit()

# 关闭游标和连接
c.close()
conn.close()