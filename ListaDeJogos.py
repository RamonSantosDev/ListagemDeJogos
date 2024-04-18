from flask import Flask, render_template, request, redirect
from flask import session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


# Novo objeto sendo instanciado
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
        #Rodar a aplicação
        app.run(debug=True)