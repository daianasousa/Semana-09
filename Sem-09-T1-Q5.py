def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


def main():
    mes = int(input('Mês: '))
    populacao = int(input('População: '))

    cidades = carrega_cidades()


    meses = ('JANEIRO', 'FEVEREIRO' ,'MARÇO' ,'ABRIL' ,'MAIO' ,'JUNHO' ,'JULHO' ,'AGOSTO' ,'SETEMBRO' , 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
    for i in range(12):
        meses[i]


    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {meses[mes-1]}:')
    for dados in cidades:
        if dados[-1] > populacao and dados[-2] == mes:
            nome = dados[2]
            dia = dados[3]
            uf = dados[0]
            pop = dados[-1]
            print(f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {meses[mes-1].lower()}.')

if __name__ == '__main__':
    main()