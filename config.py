import os
# Chave secreta para a aplicação
# (utilizada para proteger sessões e outras coisas)
SECRET_KEY = 'Rsant'

#URI de conexão com o banco de dados utilizando SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'.format(
        username = 'root',
        password = 'toor',
        host = 'localhost',
        port = '0000',
        database_name = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'