from getFunctions import *
from Combat import *
def movement():
    end = False
    moves = ['up', 'down', 'right', 'left', 'leave','r','l','u','d']
    move = input()
    move.lower()
    while move not in moves:
        move = input()
        move.lower()
    if move in ['up','u']:
        up()
        read_tile()
    elif move in ['down','d']:
        down()
        read_tile()
    elif move in ['right','r']:
        right()
        read_tile()
    elif move in ['left','l']:
        left()
        read_tile()
    else:
        end = True
    return end


def right():
    with open('mapPos', 'r') as m:
        pos = eval(m.read())
    x = pos[0]
    y = pos[1]
    newX = int(x) + 1
    if newX > 10:
        print("Developer Laziness blocks you!")
        newX = x
    newPos = '{},{}'
    with open('mapPos', 'w') as f:
        f.write(newPos.format(newX,y))


def left():
    with open('mapPos', 'r') as m:
        pos = eval(m.read())
        x = pos[0]
        y = pos[1]
        newX = int(x) - 1
        if newX < 0:
            print("Developer Laziness blocks you!")
            newX = x
        newPos = '{},{}'
        with open('mapPos', 'w') as f:
            f.write(newPos.format(newX,y))


def down():
    with open('mapPos', 'r') as m:
        pos = eval(m.read())
    x = pos[0]
    y = pos[1]
    newY = int(y) + 1
    if newY > 9:
        print("Developer Laziness blocks you!")
        newY = y
    newPos = '{},{}'
    with open('mapPos', 'w') as f:
        f.write(newPos.format(x,newY))


def up():
    with open('mapPos', 'r') as m:
        pos = eval(m.read())
    x = pos[0]
    y = pos[1]
    newY = int(y) - 1
    if newY < 0:
        print("Developer Laziness blocks you!")
        newY = y
    newPos = '{},{}'
    with open('mapPos', 'w') as f:
        f.write(newPos.format(x,newY))


def read_tile():
    with open('mapPos') as m:
        mapPos = eval(m.read())
    letter = letter_converter(int(mapPos[1]))
    tile = str(str(mapPos[0])+str(letter)+str('.txt'))
    if tile == '10b.txt' or tile == '1j.txt' or tile == '9h.txt':
        with open(r'.\Map Tiles\{}'.format(
                tile)) as f:
            for line in f:
                print(line)
        enter = get_yes_no('Do you want to enter? ')
        if enter == 'yes':
            with open('InDungeon', 'w') as z:
                z.write('{}'.format(mapPos))
            with open('mapPos','w') as m:
                m.write('{},{}'.format(4,9))
            read_tile()
    else:
        isDungeon = dungeon()
        if isDungeon == True:
                with open(r'.\Map Tiles\Dungeon Tiles\{}'.format(tile)) as s:
                    for line in s:
                        print(line)
                if tile == '4j.txt':
                    depart = get_yes_no('Do you want to leave? ')
                    if depart == 'yes':
                        with open('InDungeon','r+') as p:
                            for line in p:
                                mapPos = line[1:-1]
                            p.write('d')
                        mapPos = mapPos.split(',')
                        letter = letter_converter(mapPos[1])
                        tile = str(mapPos[0]) + str(letter) + str('.txt')
                        with open(r'.\Map Tiles\{}'.format(
                                tile)) as f:
                            for line in f:
                                print(line)
        else:
                with open(r'.\Map Tiles\{}'.format(
                        tile)) as f:
                    for line in f:
                        print(line)


def letter_converter(number):
    letters = 'abcdefghij'
    letter = letters[number]
    return letter
