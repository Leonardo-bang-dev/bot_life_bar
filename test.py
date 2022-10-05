from multiprocessing.forkserver import ensure_running
from tkinter import N


player_dict = dict()
attribute_dict = dict() 

def add(date):
    date = date.split(' ')
    name = date[0]
    # format life
    life = str(date[1])
    life = life.split('/')

    # format energ 
    energ = str(date[2])
    energ = energ.split('/')

    attribute_dict['Life'] = life
    attribute_dict['Energ'] = energ
    player_dict[name] = attribute_dict
    print(player_dict)

def show(name):
    aux = False
    life_bar = ''
    energ_bar = ''
    life = player_dict[name]['Life']
    energ = player_dict[name]['Energ']

    for a in range(1,int(life[0])):
        if int(life[1]) > a:
            life_bar += '#'
        else:
            life_bar += ' '
        aux = False

    return life_bar


add('Jaffry 10/5 12/12')
print(show('Jaffry'))

