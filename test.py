from array import array
from traceback import print_tb


player_dict = dict()
attribute_dict = dict()


def add(date):
    date = date.split(' ')

    # format name
    name = date[0]

    # format life
    life = str(date[1])
    life = life.split('/')
    life = list(map(int, life))

    # format energ
    energ = str(date[2])
    energ = energ.split('/')
    energ = list(map(int, energ))

    attribute_dict['Life'] = life
    attribute_dict['Energ'] = energ
    player_dict[name] = attribute_dict.copy()
    #print(player_dict)


def show(name):
    life_bar = ''
    energ_bar = ''
    lifes_bars = []
    energs_bars = []

    if name == 'all':
        names = list(player_dict.keys())
        for a in names:
            life_bar = ''
            energ_bar = ''
            life = player_dict[a]['Life']
            energ = player_dict[a]['Energ']

            for a in range(0, life[0]):
                if a < int(life[1]):
                    life_bar += '█ '
                else:
                    life_bar += '▓ '

            for a in range(0, energ[0]):
                if a < int(energ[1]):
                    energ_bar += '█ '
                else:
                    energ_bar += '▓ '

            lifes_bars.append(life_bar)
            energs_bars.append(energ_bar)

        return names, lifes_bars, energs_bars

    else:
        life = player_dict[name]['Life']
        energ = player_dict[name]['Energ']
        for a in range(0, int(life[0])):
            if a < int(life[1]):
                life_bar += '█ '
            else:
                life_bar += '▓ '

        for a in range(0, energ[0]):
            if a < int(energ[1]):
                energ_bar += '█ '
            else:
                energ_bar += '▓ '
        return life_bar, energ_bar


def sub_(data):
    data = data.split(' ')
    if data[0] == 'life':
        player_dict[data[1]]['Life'][1] = player_dict[data[1]
                                                      ]['Life'][1] - int(data[2])
    if data[0] == 'energ':
        player_dict[data[1]]['energ'][1] = player_dict[data[1]
                                                       ]['energ'][1] - int(data[2])

var = 'all'
add('Jaffry 14/14 12/12')
add('Salomão 10/10 15/15')
add('Alastor 12/12 10/10')

if var == 'all':
    bar = show(var)
    for a in range(0, len(bar[0])):
            print('')
            print(f'**⌠{bar[0][a]}⌡**')
            print(f'Life: ╣{bar[1][a]}╠')
            print(f'Energ: ╣{bar[2][a]}╠')


