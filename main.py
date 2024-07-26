from functions import new_char, casino, bar, house, r, r1, r2

name, age, iq, height, force = new_char()

print(f'Имя персонажа={name}, Возраст персонажа={age}, Интелект персонажа={iq}, Рост персонажа={height}, Сила персонажа={force}')

att = 1
while att <= 5:

    plase = input('Куда вы хотите пойти: ')

    import random

    sel = ['Вы встретили красивую девушку','Вы встретили пушистую собаку','На вас напали гопники']
    event = random.choice(sel)
    print(event)
    if event == 'Вы встретили красивую девушку':
        r()
    if event == 'Вы встретили пушистую собаку':
        r1()
    if event == 'На вас напали гопники':
        r2()

    if plase == 'Казино':
        casino(iq)

    if plase == 'Бар':
        bar(age, force)

    if plase == 'Домой':
        house()

    if plase != 'Бар' and plase != 'Казино' and plase != 'Домой':
        print('Поблизости этого нету.')

    att +=1