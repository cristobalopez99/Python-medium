def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors        

def run():
    try: 
        num = int(input('Ingresa un numero: '))
        try:
            if num < 0:
             raise ValueError('Debes ingresar un numero positivo')
            print(divisors(num))
            print('Esto ha terminado')
        except ValueError as ve:
            print(ve)
    except ValueError:
        print('Lo que ingreses debe ser un numero')

    try: 
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print('Esto ha terminado')
    except ValueError:
            print('Lo que ingreses debe ser un numero')    


               



if __name__ == '__main__':
    run()


