def new_char():
    name = input('Введите имя персонажу: ')
    age = input('Сколько лет персонажу: ')
    age = int(age)
    iq = input('Какой интелект у персонажа: ')
    height = input('Какой рост у персонажа: ')
    force = input('Какая сила у персонажа: ')
    return name, age, iq, height, force

def casino(iq):
    if iq == ('Высокий'):
        print('У вас высокий интелект, вы выиграли 100000 рублей!!!')
    if iq == ('Средний'):
        print('У вас средний интелект, вы вышли в ноль')
    if iq == ('Низкий'):
        print('У вас низкий интелект, вы всё проиграли.')

def bar(age, force):
    if age < 18:
        print('Канай отсюда, малолетка!')
    if age >= 18:
        print('Проходи')
        think = input('Что вы будете делать? ')
        if think == ('Пить'):
            if force == ('Высокая'):
                print('Вы напились и вас пытались ограбить, но поскольку у вас высокая сила вы отбились.')
            if force != ('Высокая'):
                print('Вы напились и вас ограбили, отбиться вам нехватило сил.')
        if think == ('Болтать'):
            print('Вас заговорила красивая девушка, а её поддельник незаметно вас ограбил')

def house():
    think2 = input('Что вы будете делать? ')
    if think2 == ('Спать'):
        print('Вы проспали до утра')
    if think2 == ('Смотреть видосики'):
        print('Вы поздно легли спать и не выспались')

def r():
    action = input('Что вы будете делать? ')
    if action == ('Поговорю с ней'):
        print('Вы пообщались и пошли по своим делам')

def r1():
    action1 = input('Что вы будете делать? ')
    if action1 == ('Поглажу'):
        print('Вы погладили милую собачку и пошли по своим делам')

def r2():
    action2 = input('Что вы будете делать? ')
    if action2 == ('Убегу'):
        print('Вы успешно убежали от гопников')