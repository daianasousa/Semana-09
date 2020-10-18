def main():
    t1 = float(input('Temperatura: '))
    e1 = str(input('Escala: ')).upper()[0]
    t2 = float(input('Temperatura: '))
    e2 = str(input('Escala: ')).upper()[0]

    T1 = (t1, e1)
    T2 = (t2,e2)

    a, b = conversao(t1,t2,e1,e2)
    
    if a > b:
        maior = T1
    elif b > a:
        maior = T2
    
    print(maior)

def conversao(t1,t2,e1,e2):
    if e1 == 'C':
        a = t1
        if e2 == 'F':
            b = (t2 - 32) * (5/9)
        elif e2 == 'C':
            b = t2
    elif e1 == 'F':
        a = (t1 - 32) * (5/9)
        if e2 == 'F':
            b = (t2 - 32) * (5/9)
        elif e2 == 'C':
            b = t2

    return a, b

if __name__ == "__main__":
    main()
    

