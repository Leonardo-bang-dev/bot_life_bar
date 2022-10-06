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
    life = list(map(int, life))

    # format energ
    energ = str(date[2])
    energ = energ.split('/')
    energ = list(map(int, energ))

    attribute_dict['Life'] = life
    attribute_dict['Energ'] = energ
    player_dict[name] = attribute_dict.copy()
    print(player_dict)


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
                    life_bar += '░ '

            for a in range(0, energ[0]):
                if a < int(energ[1]):
                    energ_bar += '█ '
                else:
                    energ_bar += '░ '

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
                life_bar += '░ '

        for a in range(0, energ[0]):
            if a < int(energ[1]):
                energ_bar += '█ '
            else:
                energ_bar += '░ '
        return name, life_bar, energ_bar


def sub(data):
    data = data.split(' ')
    if data[0] == 'life':
        player_dict[data[1]]['Life'][1] = player_dict[data[1]
                                                      ]['Life'][1] - int(data[2])
    if data[0] == 'energ':
        player_dict[data[1]]['Energ'][1] = player_dict[data[1]
                                                       ]['Energ'][1] - int(data[2])
    print(player_dict)
    return 'executado com sucesso!'


def adi(data):
    resp = ''
    data = data.split(' ')
    if data[0] == 'life'and player_dict[data[1]]['Life'][1] < player_dict[data[1]]['Life'][0]:
        player_dict[data[1]]['Life'][1] = player_dict[data[1]
                                                      ]['Life'][1] + int(data[2])
        resp = 'Executado com sucesso!'
    else: 
        resp = 'Falha ao executar!'

    if data[0] == 'energ'and player_dict[data[1]]['Energ'][1] < player_dict[data[1]]['Energ'][0]:
        player_dict[data[1]]['Energ'][1] = player_dict[data[1]
                                                       ]['Energ'][1] + int(data[2])
        resp = 'Executado com sucesso!'
    else: 
        resp = 'Falha ao executar!'

    print(player_dict)
    return resp


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Pronto para uso!')


@bot.command(name='clear')
async def clear_(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Chat limpo!')


@bot.command(name='add')
async def add_(ctx, *expression, amount=100):
    expression = ' '.join(expression)
    add(expression)
    await ctx.send('Adicionado com sucesso!')

    # Limpando chat
    await ctx.channel.purge(limit=amount)


@bot.command(name='show')
async def show_(ctx, *expression, amount=100):
    expression = ''.join(expression)
    await ctx.channel.purge(limit=amount)
    if expression == 'all':
        bar = show(expression)
        for a in range(0, len(bar[0])):
            await ctx.send('-----------------------------------------------------------------')
            await ctx.send(f'**⌠{bar[0][a]}⌡**')
            await ctx.send(f'Life:     ╣ {bar[1][a]}╠')
            await ctx.send(f'Energ: ╣ {bar[2][a]}╠')
    else:
        bar = show(expression)
        await ctx.send('-----------------------------------------------------------------')
        await ctx.send(f'**⌠{bar[0]}⌡**')
        await ctx.send(f'Life:     ╣ {bar[1]}╠')
        await ctx.send(f'Energ: ╣ {bar[2]}╠')


@bot.command(name='sub')
async def sub_(ctx, *expression, amount=100):
    expression = ' '.join(expression)
    print(expression)
    resp = sub(expression)
    await ctx.send(resp)
    await ctx.channel.purge(limit=amount)

    bar = show('all')
    for a in range(0, len(bar[0])):
        await ctx.send('-----------------------------------------------------------------')
        await ctx.send(f'**⌠{bar[0][a]}⌡**')
        await ctx.send(f'Life:     ╣ {bar[1][a]}╠')
        await ctx.send(f'Energ: ╣ {bar[2][a]}╠')

@bot.command(name='adi')
async def sub_(ctx, *expression, amount=100):
    expression = ' '.join(expression)
    print(expression)
    resp = adi(expression)
    await ctx.send(resp)
    await ctx.channel.purge(limit=amount)

    bar = show('all')
    for a in range(0, len(bar[0])):
        await ctx.send('-----------------------------------------------------------------')
        await ctx.send(f'**⌠{bar[0][a]}⌡**')
        await ctx.send(f'Life:     ╣ {bar[1][a]}╠')
        await ctx.send(f'Energ: ╣ {bar[2][a]}╠')

bot.run('MTAyMzk5Nzc1ODQzODM4Nzc4NA.GYPO0G.QjTtIuwDWvv5zpV-peK4cp_0YbbxkGpRXOwNIU')
