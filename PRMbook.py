def prm_function():
    request_ssr = (input('Введите запрос, нажмите Enter. (выход - q)\n').upper())
    list_counter = open('input.txt')
    counter = list_counter.readline()
    with open('input.txt', 'r', encoding='utf-8') as list_ssr:
        if request_ssr == 'Q' or request_ssr == 'Й':
            return print('Выход!')
        else:
            counter_ssr = 0
            for i in list_ssr:
                i = i.strip().split()
                if request_ssr == i[0]:
                    print(*i[1:])
                    counter_ssr = 0
                    prm_function()
                elif counter_ssr == int(counter):
                    print('Вы ввели некорректное значение.\n'
                          'Повторите пожалуйста.')
                    counter_ssr = 0
                    prm_function()
                counter_ssr += 1
    list_counter.close()

print('Добро пожаловать!\n'
      'Категории пассажиров (например введите WCHR или SVAN)\n'
      'Правила перевозки инвалидных кресел-колясок(например введите WCMP или WCLB)\n'
      'Выходы на посадку по номеру стоянки (например введите 106A или 102B)\n'
      'Коды аэропортов мира ИАТА (например введите LED или AAQ)\n'
      'Контакты сотрудников(например введите Иванов или Петрова)')
prm_function()
