mes = int(input('Diga em que mês você nasceu: '))
dia = int(input('Diga em que dia você nasceu: '))
if mes == 1 and dia >= 20  or mes == 2 and dia <= 18:
    print('Seu signo é Aquário')
else:
    if mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
        print('Seu signo é Peixes')
    else:
        if mes == 3 and dia >= 21 or mes == 4 and dia <= 19:
            print('Seu signo é Touro')
        else:
            if mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
                print('Seu signo é Touro')
            else:
                if mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
                    print('Seu signo é Gêmeos')
                else:
                    if mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
                        print('Seu signo é Câncer')
                    else:
                        if mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
                            print('Seu signo é Leão')
                        else:
                            if mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
                                print('Seu signo é Virgem')
                            else:
                                if mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
                                    print('Seu signo é Libra')
                                else:
                                    if mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
                                        print('Seu signo é Escorpião')
                                    else:
                                        if mes == 11 and dia >= 23 or mes == 12 and dia <= 21:
                                            print('Seu signo é sagitário')
                                        else:
                                            if mes == 12 and dia >= 22 or mes == 1 and dia <= 19:
                                                print('Seu signo é Capricórnio')
                                            else:
                                                print('Sua data não faz sentido')