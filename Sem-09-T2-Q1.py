def main():
    n = int(input())

    matriz = gerar_matriz(n)

    maior, lma, cma = maior_elemento(matriz, n)
    tupla_maior = lma, cma
    print(tuple(tupla_maior))
    
    menor, lme, cme = menor_elemento(matriz, n)
    tupla_menor = lme, cme
    print(tuple(tupla_menor))


def gerar_matriz(n):
    matriz = []

    for l in range(n):
        linha = []

        for c in range(n):
            num = int(input())
            linha.append(num)
        
        matriz.append(linha)

    return matriz


def maior_elemento(matriz, n):
    maior = matriz[0][0]
    linha = 0
    coluna = 0

    for l in range(n):
        for c in range(n):
            if matriz[l][c] > maior:
                maior = matriz[l][c]        
                linha = l
                coluna = c

    return maior, linha, coluna


def menor_elemento(matriz, n):
    menor = matriz[0][0]
    linha = 0
    coluna = 0

    for l in range(n):
        for c in range(n):
            if matriz[l][c] < menor:
                menor = matriz[l][c]
                linha = l
                coluna = c

    return menor, linha, coluna


if __name__ == "__main__":
    main()