from ast import Expression
import discord
from discord.ext import commands

# Funções
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

    return f'{name}: |{life_bar}|'



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Pronto para uso!')

@bot.command(name = 'add')
async def add_(ctx, *expression):
    expression = ' '.join(expression)
    add(expression)
    await ctx.send('Adicionado com sucesso!')

@bot.command(name = 'show')
async def show_(ctx, *expression):
    expression = ''.join(expression)
    life_bar = show(expression)
    await ctx.send(life_bar)
    
bot.run('MTAyMzk5Nzc1ODQzODM4Nzc4NA.G4dB_q.HGgEzCweEw6z9Wyu_oTm0fUJxkni7dwrdCu2Lo')
