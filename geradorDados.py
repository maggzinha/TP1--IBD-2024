'''utilizei pymysql ao inves de mysql pois estava dando muito erro de conexão'''
import pymysql
from faker import Faker
import random
from datetime import datetime, timedelta

# conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '//ufam2024',
    'database': 'connectme'
}

# conexão com BD
mydb = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

cursor = mydb.cursor()

# iniciar Faker
fake = Faker('pt_BR')

# gerar dados aleatorios


def data_nascimento():
    return fake.date_of_birth(minimum_age=18, maximum_age=65)


def data_hora():
    # -1y intervalo de tempo começa um ano atras a partir do atual
    return fake.date_time_between(start_date="-1y", end_date="now")


def data_hora_mensagem():
    inicio = datetime.now() - timedelta(days=365)  # ultimo ano
    fim = datetime.now()
    data_hora = fake.date_time_between(start_date=inicio, end_date=fim)
    return data_hora.strftime('%Y-%m-%d %H:%M:%S')


def foto_perfil():
    return f"/imagem/usuario/foto_{fake.unique.random_int(min=1, max=10000)}.png"


def foto_grupo():
    return f"/imagem/grupo/foto_{fake.unique.random_int(min=1, max=100)}.png"


def endereco():
    endereco = fake.address()
    return endereco[:255]


# Dados para as tabelas
num_usuarios = 1000
num_grupos = 20
num_mensagens = 2500
num_postagens = 2500

# Tabelas


def Perfil_usuario(num_usuarios):
    for _ in range(num_usuarios):
        cursor.execute(
            "INSERT INTO Perfil_usuario (nome, foto, data_nascimento, endereco, biografia) VALUES (%s, %s, %s, %s, %s)",
            (fake.name(), foto_perfil(), data_nascimento(),
             endereco(), fake.sentence())
        )
        mydb.commit()


def Perfil_grupo(num_grupos):
    for _ in range(num_grupos):
        cursor.execute(
            "INSERT INTO Perfil_grupo (nome, foto, descricao) VALUES (%s, %s, %s)",
            # o catch_phrase cria texto curtos aleatorios/altenativos
            (fake.company(), foto_grupo(), fake.catch_phrase())
        )
        mydb.commit()


def Mensagem(num_mensagens):
    for _ in range(num_mensagens):
        cursor.execute(
            "INSERT INTO Mensagem (conteudo) VALUES (%s)",
            (fake.text(),)
        )
        mydb.commit()


def Grupo(num_grupos):
    for i in range(1, num_grupos + 1):
        cursor.execute(
            "INSERT INTO Grupo (id_perfil_grupo) VALUES (%s)",
            (i,)
        )
        mydb.commit()


def Usuario(num_usuarios):
    for i in range(num_usuarios):
        email = fake.unique.email()  # garantir que o email seja unico
        id_grupo = fake.random_int(min=1, max=num_grupos)
        data_hora_criacaoGrupo = data_hora()
        id_mensagem = fake.random_int(min=1, max=num_mensagens)
        data_hora_mensagem_gerada = data_hora_mensagem()
        id_perfil_usuario = i + 1  # id tabela Perfil_usuario
        cursor.execute(
            "INSERT INTO Usuario (email, id_grupo, data_hora_criacaoGrupo, id_mensagem, data_hora_mensagem, id_perfil_usuario) VALUES (%s, %s, %s, %s, %s, %s)",
            (email, id_grupo, data_hora_criacaoGrupo,
             id_mensagem, data_hora_mensagem_gerada, id_perfil_usuario)
        )
        mydb.commit()


def Postagem(num_postagens):
    for _ in range(num_postagens):
        tipo = fake.random_element(elements=('texto', 'imagem', 'video'))
        arquivo = f"arquivo_{fake.file_name()}" if tipo != 'texto' else None
        texto = fake.sentence() if tipo == 'texto' else None
        cursor.execute("SELECT email FROM Usuario")
        usuarios = cursor.fetchall()  # retorna todas as linhas da  consulta
        email = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        data_hora = fake.date_this_year()
        id_grupo = fake.random_int(min=1, max=num_grupos)
        cursor.execute(
            "INSERT INTO Postagem (tipo, arquivo, texto, email, data_hora, id_grupo) VALUES (%s, %s, %s, %s, %s, %s)",
            (tipo, arquivo, texto, email, data_hora, id_grupo)
        )
        mydb.commit()


def Conecta(num_usuarios):
    for i in range(num_usuarios):
        cursor.execute("SELECT email FROM Usuario")
        usuarios = cursor.fetchall()
        email_usuario = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        email_conexao = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        while email_usuario == email_conexao:
            email_conexao = fake.random_element(
                elements=[usuario[0] for usuario in usuarios])
        cursor.execute(
            "INSERT IGNORE INTO Conecta (email_usuario, email_conexao) VALUES (%s, %s)",
            (email_usuario, email_conexao)
        )
        mydb.commit()


def Participa(num_usuarios):
    for i in range(num_usuarios):
        cursor.execute("SELECT email FROM Usuario")
        usuarios = cursor.fetchall()
        email_usuario = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        id_grupo = fake.random_int(min=1, max=num_grupos)
        cursor.execute(
            "INSERT IGNORE INTO Participa (email_usuario, id_grupo) VALUES (%s, %s)",
            (email_usuario, id_grupo)
        )
    mydb.commit()


def Interesse(num_usuarios):
    for i in range(1, num_usuarios + 1):
        cursor.execute(
            "INSERT INTO Interesse (id_perfil_usuario, descricao) VALUES (%s, %s)",
            (i, fake.sentence())
        )
        mydb.commit()


def Interage(num_postagens):
    for i in range(1, num_postagens + 1):
        cursor.execute("SELECT email FROM Usuario")
        usuarios = cursor.fetchall()
        email_usuario = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        data_hora = data_hora_mensagem()
        cursor.execute(
            "INSERT INTO Interage (id_postagem, email_usuario, data_hora) VALUES (%s, %s, %s)",
            (i, email_usuario, data_hora)
        )
        mydb.commit()


def Chat(num_mensagens):
    for i in range(num_mensagens):
        id_mensagem = i + 1
        cursor.execute("SELECT email FROM Usuario")
        usuarios = cursor.fetchall()
        email_usuario = fake.random_element(
            elements=[usuario[0] for usuario in usuarios])
        id_grupo = fake.random_int(min=1, max=num_grupos)
        data_hora_mensagem_gerada = data_hora_mensagem()
        tipo = fake.random_element(elements=('pessoal', 'grupo'))
        cursor.execute(
            "INSERT INTO Chat (id_mensagem, email_usuario, id_grupo, data_hora_mensagem, tipo) VALUES (%s, %s, %s, %s, %s)",
            (id_mensagem, email_usuario, id_grupo, data_hora_mensagem_gerada, tipo)
        )
        mydb.commit()


# Chamada das funçoes
Perfil_usuario(num_usuarios)
Perfil_grupo(num_grupos)
Mensagem(num_mensagens)
Grupo(num_grupos)
Usuario(num_usuarios)
Postagem(num_postagens)
Conecta(num_usuarios)
Participa(num_usuarios)
Interesse(num_usuarios)
Interage(num_postagens)
Chat(num_mensagens)

print("Banco de dados populado com sucesso!")

cursor.close()
mydb.close()
