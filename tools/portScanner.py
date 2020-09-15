#/usr/bin/python

import socket, sys
from threading import *

def main():
    args = sys.argv
    if len(args) < 2:
        print("Falta argumentos")
        sys.exit()
    ip = args[1]
    ports = args[2] if len(args >= 3) else "1:65535" #caso nao seja especificada nenhuma porta escaneara todas
    ports = (x for x in range(int(ports.split(":")[0]), int(ports.split(":")[1])+1)) #cria um objeto gerador com as portas a serem escaneadas
    scan(ip, ports)


def scan(ip, ports):
    for c in ports:
        child(ip, c)


def child(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket ipv4, tcp
        s.settimeout(10) #caso o alvo nao responda a tempo uma excecao sera gerada e a funcao chegara ao fim
        if s.connect_ex((ip, port)) == 0:
            print("{}/tcp aberto".format(port), end='|')
            print(banner(s, ip, port))
    except:
        pass


def banner(sckt, ip, port):
    # tenta pegar informacoes do servico rodando na porta
    try:
        sckt.settimeout(1)
        sckt.connect((ip, port))
        banner = sckt.recv(1024).decode().strip()
        assert banner # caso nao tenha recebido nada uma excecao sera gerada
        return banner
    except:
        return 'Unknown'
