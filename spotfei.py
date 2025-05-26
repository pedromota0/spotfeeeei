

import json
import os

# Caminho do arquivo de banco de dados
CAMINHO_BANCO = "banco_spotifei.json"

# Carregar banco de dados de arquivo 
if os.path.exists(CAMINHO_BANCO):
    with open(CAMINHO_BANCO, "r", encoding="utf-8") as f:
        banco = json.load(f)
else:
    banco = {
        "usuarios": {},
        "musicas": {
            "Shape of You": {"artista": "Ed Sheeran", "genero": "Pop", "ano": 2017},
            "Bohemian Rhapsody": {"artista": "Queen", "genero": "Rock", "ano": 1975},
            "Blinding Lights": {"artista": "The Weeknd", "genero": "Synthpop", "ano": 2019},
            "Levitating": {"artista": "Dua Lipa", "genero": "Pop", "ano": 2020},
            "Peaches": {"artista": "Justin Bieber", "genero": "R&B", "ano": 2021},
            "Happier Than Ever": {"artista": "Billie Eilish", "genero": "Alternative", "ano": 2021},
            "Drivers License": {"artista": "Olivia Rodrigo", "genero": "Pop", "ano": 2021},
            "Bad Guy": {"artista": "Billie Eilish", "genero": "Electropop", "ano": 2019},
            "Stay": {"artista": "The Kid LAROI & Justin Bieber", "genero": "Pop", "ano": 2021},
            "Save Your Tears": {"artista": "The Weeknd", "genero": "Pop", "ano": 2020}
        }
    }

# Sessão atual
usuario_atual = None

# Funções de usuário
def cadastrar_usuario():
    global banco
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if nome in banco["usuarios"]:
        print("Usuário já existe.")
    else:
        banco["usuarios"][nome] = {
            "senha": senha,
            "curtidas": [],
            "descurtidas": [],
            "playlists": {}
        }
        print("Usuário cadastrado com sucesso!")

def login():
    global usuario_atual
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome in banco["usuarios"] and banco["usuarios"][nome]["senha"] == senha:
        usuario_atual = nome
        print(f"\nBem-vindo, {nome}!")
        menu_usuario()
    else:
        print("Usuário ou senha incorretos.")

# Buscar músicas
def buscar_musica():
    nome = input("Digite o nome da música: ")
    resultado = banco["musicas"].get(nome)
    if resultado:
        print(f"Música encontrada: {nome}")
        print(f"Artista: {resultado['artista']} | Gênero: {resultado['genero']} | Ano: {resultado['ano']}")
    else:
        print("Música não encontrada.")

# Adicionar nova música manualmente
def adicionar_musica():
    nome = input("Digite o nome da música: ")
    artista = input("Digite o nome do artista: ")
    genero = input("Digite o gênero: ")
    ano = input("Digite o ano: ")
    banco["musicas"][nome] = {"artista": artista, "genero": genero, "ano": int(ano)}
    print("Música adicionada com sucesso!")

# Curtir e descurtir
def curtir_musica():
    if usuario_atual:
        nome = input("Nome da música para curtir: ")
        if nome in banco["musicas"]:
            if nome not in banco["usuarios"][usuario_atual]["curtidas"]:
                banco["usuarios"][usuario_atual]["curtidas"].append(nome)
                print("Música curtida!")

def descurtir_musica():
    if usuario_atual:
        nome = input("Nome da música para descurtir: ")
        if nome in banco["musicas"]:
            if nome not in banco["usuarios"][usuario_atual]["descurtidas"]:
                banco["usuarios"][usuario_atual]["descurtidas"].append(nome)
                print("Música descurtida!")

# Gerenciar playlist
def criar_playlist():
    if usuario_atual:
        nome = input("Nome da nova playlist: ")
        if nome not in banco["usuarios"][usuario_atual]["playlists"]:
            banco["usuarios"][usuario_atual]["playlists"][nome] = []
            print("Playlist criada.")
        else:
            print("Essa playlist já existe.")

def editar_playlist():
    if usuario_atual:
        nome = input("Nome da playlist a editar: ")
        if nome in banco["usuarios"][usuario_atual]["playlists"]:
            acao = input("Digite 'add' para adicionar ou 'remover' para tirar uma música: ")
            musica = input("Nome da música: ")
            if acao == "add":
                if musica in banco["musicas"]:
                    banco["usuarios"][usuario_atual]["playlists"][nome].append(musica)
                    print("Música adicionada à playlist.")
                else:
                    print("Música não encontrada.")
            elif acao == "remover":
                if musica in banco["usuarios"][usuario_atual]["playlists"][nome]:
                    banco["usuarios"][usuario_atual]["playlists"][nome].remove(musica)
                    print("Música removida da playlist.")
                else:
                    print("Essa música não está na playlist.")
        else:
            print("Playlist não encontrada.")

def excluir_playlist():
    if usuario_atual:
        nome = input("Nome da playlist a excluir: ")
        if nome in banco["usuarios"][usuario_atual]["playlists"]:
            del banco["usuarios"][usuario_atual]["playlists"][nome]
            print("Playlist excluída.")
        else:
            print("Playlist não encontrada.")

def visualizar_playlists():
    if usuario_atual:
        playlists = banco["usuarios"][usuario_atual]["playlists"]
        if playlists:
            print("Suas playlists:")
            for nome, musicas in playlists.items():
                print(f"- {nome}: {musicas if musicas else 'vazia'}")
        else:
            print("Você não tem playlists ainda.")

# Histórico
def visualizar_historico():
    print("Curtidas:", banco["usuarios"][usuario_atual]["curtidas"])
    print("Descurtidas:", banco["usuarios"][usuario_atual]["descurtidas"])

# Menu principal
def salvar_banco():
    with open(CAMINHO_BANCO, "w", encoding="utf-8") as f:
        json.dump(banco, f, indent=2, ensure_ascii=False)

def menu():
    while True:
        print("\n==============================")
        print("         MENU PRINCIPAL")
        print("==============================")
        print("1. Cadastrar\n2. Login\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1": cadastrar_usuario()
        elif opcao == "2": login()
        elif opcao == "3":
            salvar_banco()
            print("Encerrando aplicação.")
            break

def menu_usuario():
    while True:
        print("\n==============================")
        print("      BEM-VINDO AO SPOTIFEI")
        print("==============================")
        print("1. Buscar Música\n2. Curtir Música\n3. Descurtir Música\n4. Criar Playlist\n5. Editar Playlist\n6. Excluir Playlist\n7. Ver Histórico\n8. Adicionar Música\n9. Ver Playlists\n10. Logout")
        opcao = input("Escolha uma opção: ")
        if opcao == "1": buscar_musica()
        elif opcao == "2": curtir_musica()
        elif opcao == "3": descurtir_musica()
        elif opcao == "4": criar_playlist()
        elif opcao == "5": editar_playlist()
        elif opcao == "6": excluir_playlist()
        elif opcao == "7": visualizar_historico()
        elif opcao == "8": adicionar_musica()
        elif opcao == "9": visualizar_playlists()
        elif opcao == "10":
            salvar_banco()
            print("Você saiu da sua conta.")
            break

menu()
