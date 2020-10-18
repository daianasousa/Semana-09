def main():
    dia = int(input('Dia: '))
    mes = int(input('mês: '))


    informacao = carrega_cidades()

    meses = ('JANEIRO', 'FEVEREIRO' ,'MARÇO' ,'ABRIL' ,'MAIO' ,'JUNHO' ,'JULHO' ,'AGOSTO' ,'SETEMBRO' , 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
    for i in range(12):
        meses[i]

    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {meses[mes-1]}:')
    for dado in informacao:
        if dado[3] == dia and dado[4] == mes:
            nome = dado[2]
            uf = dado[0]
            print(f'{nome}({uf})')


def carrega_cidades():
    informacao = []

    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            informacao.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()


    informacao = tuple(informacao)
    return informacao


if __name__ == '__main__':
    main()





