from random import *

def main():
    colunas = int(input())
    linhas = int(input())

    matriz = gerar_matriz(linhas, colunas)
    soma_linha = soma_primeira_linha(matriz, linhas)
    soma_coluna = soma_ultima_coluna(matriz, linhas, colunas)
    menor = menor_elemento(matriz)
    maior = maior_elemento(matriz)
    media = media_matriz(matriz, linhas, colunas)

    tupla = soma_linha, soma_coluna, media, menor, maior
    print(tuple(tupla))
    

def gerar_matriz(linhas, colunas):
    matriz = []

    for c in range(colunas):
        coluna = []

        for l in range(linhas):
            num = int(input())
            coluna.append(num)
        
        matriz.append(coluna)

    return matriz


def elementos(matriz):
    todos_elementos = []

    for linha in matriz:
        for elemento in linha:
            todos_elementos.append(elemento)

    return todos_elementos


def soma_primeira_linha(matriz, linhas):
    todos_elementos = elementos(matriz)

    soma_linha = 0
    for c in range(linhas):
        soma_linha += todos_elementos[c]

    return soma_linha


def soma_ultima_coluna(matriz, colunas, linhas):
    todos_elementos = elementos(matriz)

    soma_coluna = 0

    for c in range(colunas - 1, linhas * colunas, colunas):
        soma_coluna += todos_elementos[c]

    return soma_coluna


def menor_elemento(matriz):
    todos_elementos = elementos(matriz)
    me = 1000000

    for elemento in todos_elementos:
        if elemento < me:
            me = elemento
        
    return me


def maior_elemento(matriz):
    todos_elementos = elementos(matriz)
    ma = 0

    for elemento in todos_elementos:
        if elemento > ma:
            ma = elemento
        
    return ma


def media_matriz(matriz, colunas, linhas):
    todos_elementos = elementos(matriz)
    soma = 0

    for e in todos_elementos:
            soma += e
   
    media = soma / (colunas * linhas)
    media = round(media, 4)

    return media


if __name__ == "__main__":
    main()