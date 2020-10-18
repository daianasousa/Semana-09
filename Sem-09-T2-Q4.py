def main():
    matriz = []

    for l in range(4):
        linha = []

        for c in range(6):
            num = int(input())
            linha.append(num)
        
        matriz.append(linha)

    ano = int(input())
    maior, empresa = maior_venda_ano_especifico(ano, matriz)

    print('A fabricante que mais vendeu em {} foi a {} com {} mil unidades.'.format(ano, empresa, maior))

    a, maior = maior_venda_todos_anos(matriz)
    print('O ano de maior volume geral de vendas foi {} com {} mil unidades.'.format(a, maior))

    m_fiat, m_ford, m_gm, m_wolkswagen = medias(matriz) 
    print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
    print('A Fiat vendeu em média {} unidades por ano.'.format(m_fiat))
    print('A Ford vendeu em média {} unidades por ano.'.format(m_ford))
    print('A GM vendeu em média {} unidades por ano.'.format(m_gm))
    print('A Wolkswagen vendeu em média {} unidades por ano.'.format(m_wolkswagen))


def anos(ano):
    if ano == 2013:
        c = 0
    elif ano == 2014:
        c = 1
    elif ano == 2015:
        c = 2
    elif ano == 2016:
        c = 3
    elif ano == 2017:
        c = 4
    elif ano == 2018:
        c = 5            

    return c


def maior_venda_ano_especifico(ano, matriz):
    c = anos(ano)
    maior = [0][0]

    for l in range(4):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            
            if l == 0:
                empresa = 'Fiat'
            if l == 1:
                empresa = 'Ford'
            if l == 2:
                empresa = 'GM'
            if l == 3:
                empresa = 'Wolkswagen'
            
    return maior, empresa


def total_vendas_anos(matriz):
    ano_2013 = []
    soma_2013 = 0
    ano_2014 = []
    soma_2014 = 0
    ano_2015 = []
    soma_2015 = 0
    ano_2016 = []
    soma_2016 = 0
    ano_2017 = []
    soma_2017 = 0
    ano_2018 = []
    soma_2018 = 0

    for l in range(4):
        if matriz[l][0]:
            ano_2013.append(matriz[l][0])
            soma_2013 += matriz[l][0]

        if matriz[l][1]:
            ano_2014.append(matriz[l][1])
            soma_2014 += matriz[l][1]

        if matriz[l][2]:
            ano_2015.append(matriz[l][2])
            soma_2015 += matriz[l][2]

        if matriz[l][3]:
            ano_2016.append(matriz[l][3])
            soma_2016 += matriz[l][3]

        if matriz[l][4]:
            ano_2017.append(matriz[l][4])
            soma_2017 += matriz[l][4]

        if matriz[l][5]:
            ano_2018.append(matriz[l][5])
            soma_2018 += matriz[l][5]


    l = soma_2013, soma_2014, soma_2015, soma_2016, soma_2017, soma_2018
    lista = list(l)
    return lista


def maior_venda_todos_anos(matriz):
    lista = total_vendas_anos(matriz)
    maior = 0

    i = 2013
    while i <= 2018:
        for num in lista:
            if num > maior:
                a = i
                maior = num

            i += 1

    return a, maior


def total_venda_cada_fabricante(matriz):
    fiat = []
    ford = []
    gm = []
    wolkswagen = []
    
    for c in range(6):
        fiat.append(matriz[0][c])
        ford.append(matriz[1][c])
        gm.append(matriz[2][c])
        wolkswagen.append(matriz[3][c])

    return fiat, ford, gm, wolkswagen


def medias(matriz):
    fiat, ford, gm, wolkswagen = total_venda_cada_fabricante(matriz)
    
    soma = 0
    for num in fiat:
        soma += num
    m_fiat = soma / 6
    m_fiat = round(m_fiat, 2)

    soma = 0
    for num in ford:
        soma += num
    m_ford = soma / 6
    m_ford = round(m_ford, 2)

    soma = 0
    for num in gm:
        soma += num
    m_gm = soma / 6
    m_gm = round(m_gm, 2)

    soma = 0
    for num in wolkswagen:
        soma += num

    m_wolkswagen = soma / 6
    m_wolkswagen = round(m_wolkswagen, 2)

    return m_fiat, m_ford, m_gm, m_wolkswagen


if __name__ == "__main__":
    main()