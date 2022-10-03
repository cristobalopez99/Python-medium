def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors 



def run():
    num = input('Ingresa un numero aqui: ')
    assert num.isnumeric(), 'Debe ser un numero positivo'
    print(divisors(int(num)))
    print('Esto ha terminado')



if __name__ == '__main__':
    run()

    