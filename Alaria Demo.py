from random import *
from getFunctions import *
from Move import *
from Combat import *


def main():
    game_intro()
    init_game()
    end = False
    read_tile()
    while not end:
        end = movement()
        rOne = randint(0,3)
        rTwo = randint(0,2)
        if rOne == rTwo:
            end = combat()
            read_tile()
    game_outro()


def game_intro():
    print("""
          ▄████████  ▄█          ▄████████    ▄████████  ▄█     ▄████████ 
          ███    ███ ███         ███    ███   ███    ███ ███    ███    ███ 
          ███    ███ ███         ███    ███   ███    ███ ███▌   ███    ███ 
          ███    ███ ███         ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███ 
        ▀███████████ ███       ▀███████████ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ 
          ███    ███ ███         ███    ███ ▀███████████ ███    ███    ███ 
          ███    ███ ███▌    ▄   ███    ███   ███    ███ ███    ███    ███ 
          ███    █▀  █████▄▄██   ███    █▀    ███    ███ █▀     ███    █▀  
                     ▀                        ███    ███                   
    --------------------------------------------------------------------------------------------
                                        The First Adventure """)
    instructions()


def instructions():
    i = get_yes_no('Do you want to see the instructions? ')
    if i == 'yes':
        print("""
        Controls:
            To Move - Type Up, Down, Left, or Right
            To quit - Type leave
               ----In Combat----
            To Attack - Type Attack
            To Defend - Type Defend
            To Study - Type Study""")


def init_game():
    load = 'loading............'
    with open('Weapon', 'w+') as w:
        w.write('W:Sword +0')
    print(load[0], end='')
    with open('CharacterData', 'w+') as s:
        s.write("""A:5
D:5
H:10
SA:5
SD:5""")
    print(load[1], end='')
    mapPos = [randint(1, 10), randint(0, 9)]
    print(load[2], end='')
    mapPos = [2,9]
    with open('mapPos', 'w+') as m:
        m.write('{},{}'.format(mapPos[0],mapPos[1]))
    with open('InDungeon','w+') as d:
        d.write('d')
    print(load[3:])


def game_outro():
    print("""
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          """)
main()
