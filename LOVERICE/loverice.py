from aifc import Error

from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def create_connection(rep):
    if not os.path.exists(rep):
        print(f"Le fichier {rep} n'existe pas")
        connection = None
    else:
        try:
            connection = sqlite3.connect(rep)
            print("Connection to SQLite réussi")
        except Error as e:
            print(f"The error {e} occured")
    return connection


def execute_read_query(connection, query):
    with connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def execute_commit(connection, query, params):
    with connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
    return


@app.route('/')
def Accueil():
    return render_template('Accueil.html')


@app.route('/Accueil')
def Accueil1():
    return render_template('Accueil.html')


@app.route('/Articles')
def Articles():
    return render_template('Articles.html')


@app.route('/CasqueBluetooth')
def CasqueBluetooth():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'CasqueBluetooth'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('CasqueBluetooth.html', list=a)


@app.route('/ChoixThème')
def ChoixThème():
    return render_template('ChoixThème.html')


@app.route('/ConsolesDeJeux-Video')
def ConsolesDeJeuxVideo():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'ConsolesDeJeux-Video'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('ConsolesDeJeux-Video.html', list=a)


@app.route('/EcouteursBluetooth')
def EcouteursBluetooth():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'EcouteurBluetooth'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('EcouteursBluetooth.html', list=a)

@app.route('/EnceinteBluetooth')
def EnceinteBluetooth():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'EnceinteBluetooth'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('EnceinteBluetooth.html', list=a)

@app.route('/EcranPC')
def EcranPC():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'EcranPC'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('EcranPC.html', list=a)


@app.route('/OrdinateurPortbale')
def OrdinateurPortbale():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'OrdinateurPortbale'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('OrdinateurPortbale.html', list=a)


@app.route('/Smartphone')
def Smartphone():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'Smartphone'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('Smartphone.html', list=a)


@app.route('/Tablette')
def Tablette():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
    FROM Article, Thème
    where nomthème = 'Tablette'
    and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    return render_template('Tablette.html', list=a)


@app.route('/Thèmes')
def Thèmes():
    return render_template('Thèmes.html')


@app.route('/TV')
def TV():
    con = create_connection("./db/DonnéesLoverice.db")
    query = '''SELECT * 
FROM Article, Thème
where nomthème = 'TV'
and Article.IdThème = Thème.idthème'''
    a = execute_read_query(con, query)
    # print(a)
    return render_template('TV.html', list=a)



# ---------------Contactez-nous----------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recu', methods=['GET', 'POST'])
def recu():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        num = request.form.get('num')
        msg = request.form.get('message')

        # Get the highest idUtilisateur and increment it by 1
        query = '''
            SELECT MAX(idUtilisateur)
            FROM Contacter
        '''
        idUtilisateur = execute_read_query(create_connection("./db/DonnéesLoverice.db"), query)[0][0]
        if idUtilisateur is None:
            idUtilisateur = 1
        else:
            idUtilisateur += 1

        # Get the highest idSAV and increment it by 1
        query = '''
            SELECT MAX(idSAV)
            FROM Contacter
        '''
        idSAV = execute_read_query(create_connection("./db/DonnéesLoverice.db"), query)[0][0]
        if idSAV is None:
            idSAV = 1
        else:
            idSAV += 1

        # Insert the new row into the Contacter table
        query = '''
            INSERT INTO Contacter (idUtilisateur, idSAV, mailUtil, nomUtil, numUtil,msgUtil)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        values = (idUtilisateur, idSAV, email, nom, num, msg)
        execute_commit(create_connection("./db/DonnéesLoverice.db"), query, values)

        return render_template('recu.html')
    else:
        return "Method not allowed"


# -----------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
