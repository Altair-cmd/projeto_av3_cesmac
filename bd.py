import sqlite3
import hashlib

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('sistema.db')

# Função para criar a tabela de usuários
def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Função para criar a tabela de produtos
def criar_tabela_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute('''
        INSERT INTO usuarios (nome, email, senha)
        VALUES (?, ?, ?)
    ''', (nome, email, senha_hash))

    conn.commit()
    conn.close()

# Função para realizar login
def login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute('''
        SELECT * FROM usuarios
        WHERE email=? AND senha=?
    ''', (email, senha_hash))

    usuario = cursor.fetchone()

    conn.close()

    return usuario

# Função para cadastrar um novo produto
def cadastrar_produto(nome, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco)
        VALUES (?, ?)
    ''', (nome, preco))

    conn.commit()
    conn.close()

# Função para buscar produtos pelo nome
def buscar_produto_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM produtos
        WHERE nome LIKE ?
    ''', ('%' + nome + '%',))

    produtos = cursor.fetchall()

    conn.close()

    return produtos

# Função para exibir um produto pelo ID
def exibir_produto_por_id(produto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM produtos
        WHERE id=?
    ''', (produto_id,))

    produto = cursor.fetchone()

    conn.close()

    return produto

# Função para atualizar um produto pelo ID
def atualizar_produto(produto_id, nome, preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE produtos
        SET nome=?, preco=?
        WHERE id=?
    ''', (nome, preco, produto_id))

    conn.commit()
    conn.close()

# Função para remover um produto pelo ID
def remover_produto(produto_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM produtos
        WHERE id=?
    ''', (produto_id,))

    conn.commit()
    conn.close()

# Criar tabelas se não existirem
criar_tabela_usuarios()
criar_tabela_produtos()