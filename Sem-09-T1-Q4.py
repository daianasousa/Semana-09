def main():
    populacao = int(input('População: '))

    cidades = carrega_cidades()
    
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for dados in cidades:
        if dados[-1] > populacao:
            nome = dados[2]
            ibge = dados[1]
            uf = dados[0]
            pop = dados[-1]
            print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}')

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


if __name__ == '__main__':
    main()