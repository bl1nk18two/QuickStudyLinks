from time import sleep
from subprocess import Popen
import sys

def prompt():
    # Solicita ao usuário que digite o nome de um site para abrir.
    bot = "Qual site você gostaria de abrir hoje?: "
    soletrar(bot)
    site = input().lower().strip()
    abrir_site(site)

def soletrar(letras):
    # Exibe uma mensagem letra por letra, simulando um efeito de digitação.
    for letra in letras:
        print(letra, end='', flush=True)
        sleep(0.02)

def reprompt():
    #  Solicita ao usuário que digite novamente o nome de um site.
    novo_site = input().lower().strip()
    return novo_site

#  Abre o site solicitado pelo usuário no navegador Chrome.
def abrir_site(site):

    # Constantes para os endereços dos sites
    enderecos = [
        {"name": "youtube", "url": "https://www.youtube.com/"},
        {"name": "google", "url": "https://www.google.com/"},
        {"name": "github", "url": "https://github.com/bl1nk18two"},
        {"name": "chatgpt", "url": "https://chatgpt.com/"},
        {"name": "gemini", "url": "https://gemini.google.com/app"},
        {"name": "aistudio", "url": "https://aistudio.google.com/app/"},
    ]
    try:
        # Procura o site solicitado na lista de endereços
        for endereco in enderecos:
            if site == endereco["name"]:
                site = endereco["url"]
                Popen([f"start", "chrome", site], shell=True)
                cs = "Sair ou Continuar? (s/C): "
                soletrar(cs)
                pergunta = reprompt()
                if pergunta == "c":
                    prompt()
                elif pergunta == "s":
                    sys.exit()
        else:
            pass
    except Exception as e:
            print(e)
    else:    
        # Se o site não for encontrado, solicita ao usuário que digite novamente
        x = "Não Disponível. Digite Novamente: "
        soletrar(x)
        y = reprompt()
        abrir_site(y)
    
prompt()