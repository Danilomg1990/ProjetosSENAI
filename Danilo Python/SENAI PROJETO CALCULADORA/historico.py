#P111 - Autor: Caune
# "Criar novo arquivo para armazenamento do historico"
# Revisor - André
#P122 - Autor:Viviane
# "Criar função que verifica se ja existe arquivo"
# Revisor - Nathan

import os


def arquivo(nome_do_arquivo):
    if os.path.isfile(nome_do_arquivo):
        return True
    return False

def salvar_historico(conteudo):
    if not arquivo("historico.txt"):
        with open('historico.txt', 'w', encoding='utf-8') as hist:
            pass
    with open('hitorico.txt', 'a', encoding='utf-8') as hist:
        hist.write(f'{conteudo}\n')
    