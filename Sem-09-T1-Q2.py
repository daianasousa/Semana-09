def main():
    t1 = float(input('Temperatura: '))
    e1 = str(input('Escala: ')).upper()[0]
    t2 = float(input('Temperatura: '))
    e2 = str(input('Escala: ')).upper()[0]

    T1 = (t1, e1)
    T2 = (t2,e2)

    s, e = conversao(t1,t2,e1,e2)
    soma = (s, e)
    print(soma)
    

def conversao(t1,t2,e1,e2):
    if e1 == 'C':
        if e2 == 'C':
            e = 'C'
        elif e2 == 'F':
            t1 = fh(t1)
            e = 'F'
    elif e1 == 'F':
        if e2 == 'F':
            e = 'F'
        elif e2 == 'C':
            t1 = cels(t1)
            e = 'C'

    s = soma(t1,t2)

    return s, e




def soma(p, s):
    return round(p + s, 4)


def cels(t):
    return (t - 32) * (5/9)


def fh(t):
    return (t * (9/5)) + 32

if __name__ == "__main__":
    main()