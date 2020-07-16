def prm_function():
    """Contains Reservation codes for walking disabilities.
    Special Service Request (SSR) Codes"""
    counterSsr = 0 # if you changed the values to 'inputssr.txt', please change the counterSsr
    counterIata = 0 # if you changed the values to 'inputiata.txt', please change the counterIata
    print('Введите запрос и нажмите Enter: (например - SSR) \n'
    'SSR - Категории пассажиров/Перевозка инвалидных кресел \n'
    'IATA - Коды аэропортов мира ИАТА\n'
    'N - Выход')
    requestMenu = input().upper()
    if requestMenu == 'SSR':
        print('Введите запрос: (например - WCMP или WCLB).\n'
              'Для выхода введите N')
        listSsr = open('inputssr.txt', 'r', encoding='utf-8')
        requestSsr = input().upper()
        for i in listSsr:
            i = i.strip().split()
            if requestSsr == i[0]:
                print(*i[1:])
                counterSsr = 0
            elif counterSsr == 12:
                print('Вы ввели некорректное значение.\n'
                      'Повторите пожалуйста.')
                counterSsr = 0
                prm_function()
            counterSsr += 1
    elif requestMenu == 'IATA':
        print('Введите запрос: (например - LED)')
        listIata = open('inputiata.txt', 'r', encoding='utf-8')
        requestIata = input().upper()
        for i in listIata:
            i = i.strip().split()
            if requestIata == i[0]:
                print(*i[1:])
                counterIata = 0
            elif counterIata == 9374:
                print('Вы ввели некорректное значение.\n'
                      'Повторите пожалуйста.')
                counterIata = 0
                prm_function()
            counterIata += 1
    elif requestMenu == 'N':
        print('Выход.')
    else:
        print('Вы ввели некорректное значение.\n'
              'Повторите пожалуйста.')
        prm_function()


prm_function()
