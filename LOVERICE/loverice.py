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
def Acceuil():
    return render_template('Acceuil.html')


@app.route('/Acceuil')
def Acceuil1():
    return render_template('Acceuil.html')


@app.route('/Articles')
def Articles():
    return render_template('Articles.html')


@app.route('/CasqueBluetooth')
def CasqueBluetooth():
    return render_template('CasqueBluetooth.html')


@app.route('/ChoixThème')
def ChoixThème():
    return render_template('ChoixThème.html')


@app.route('/ConsolesDeJeux-Video')
def ConsolesDeJeuxVideo():
    return render_template('ConsolesDeJeux-Video.html')


@app.route('/EcouteursBluetooth')
def EcouteursBluetooth():
    return render_template('EcouteursBluetooth.html')


@app.route('/EcranPC')
def EcranPC():
    return render_template('EcranPC.html')


@app.route('/OrdinateurPortbale')
def OrdinateurPortbale():
    return render_template('OrdinateurPortbale.html')


@app.route('/Smartphone')
def Smartphone():
    return render_template('Smartphone.html')


@app.route('/Tablette')
def Tablette():
    return render_template('Tablette.html')


@app.route('/Thèmes')
def Thèmes():
    return render_template('Thèmes.html')


@app.route('/TV')
def TV():
    return render_template('TV.html')


# ---------------Contactez-nous----------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/recu', methods=['GET', 'POST'])
def recu():
    nom = request.form['nom']
    email = request.form['email']
    num = request.form['num']

    query = '''SELECT idUtilisateur
FROM Contacter
order by idUtilisateur DESC 
LIMIT 1'''
    idUtilisateur = execute_read_query(create_connection("./db/DonnéesLoverice.db"), query)
    print('dcd')
    idUtilisateur = idUtilisateur[0][0] + 1

    query = '''SELECT idSAV
    FROM Contacter
    order by idSAV DESC 
    LIMIT 1'''
    idSAV = execute_read_query(create_connection("./db/DonnéesLoverice.db"), query)
    idSAV = idUtilisateur[0][0] + 1

    query1 = '''INSERT INTO Contacter 
                VALUES (?, ?, ?, ?, ?)'''
    values1 = (idUtilisateur, idSAV, email, nom, num)
    execute_commit(create_connection("./db/DonnéesLoverice.db"), query1, values1)

    return render_template('recu.html')


# -----------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
