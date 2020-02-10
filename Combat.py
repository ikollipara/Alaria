from random import *
from getFunctions import *


def combat():
    monsterData = init_combat()
    print('{} approaches you!'.format(monsterData[0]))
    win = battle(monsterData)
    if win:
        end = False
        get_loot()
    else:
        end = True
    return end


def init_combat():
    monsterList = find_monsters()
    monster = monsterList[randint(0, len(monsterList) - 1)]
    monsterData = init_monster(monster)
    return monsterData


def find_monsters():
    monsterList = []
    isDungeon = dungeon()
    if isDungeon == False:
        with open(
                r'.\Monsters\Monster List') as m:
            for monster in m:
                monster = monster[0:-1]
                monsterList.append(monster)
    else:
        with open(r'.\Monsters\Dungeon Monsters\Monster List') as d:
            for monster in d:
                monsterList.append(monster[0:-1])
    return monsterList


def init_monster(monster):
    isDungeon = dungeon()
    if isDungeon == True:
        with open(
                r'.\Monsters\Dungeon '
                r'Monsters\{}'.format(monster)) as m:
            for line in m:
                t = line.split(':')
                if t[0] == 'W':
                    w = t[1][0:-1]
                elif t[0] == 'A':
                    a = t[1][0:-1]
                elif t[0] == 'D':
                    d = t[1][0:-1]
                elif t[0] == 'H':
                    h = t[1][0:-1]
                elif t[0] == 'SA':
                    sa = t[1][0:-1]
                elif t[0] == 'SD':
                    sd = t[1]
    else:
        with open(
                r'.\Monsters\{}'.format(
                    monster)) as f:
            for line in f:
                t = line.split(':')
                if t[0] == 'W':
                    w = t[1][0:-1]
                elif t[0] == 'A':
                    a = t[1][0:-1]
                elif t[0] == 'D':
                    d = t[1][0:-1]
                elif t[0] == 'H':
                    h = t[1][0:-1]
                elif t[0] == 'SA':
                    sa = t[1][0:-1]
                elif t[0] == 'SD':
                    sd = t[1]
    monsterData = [monster, a, d, h, sa, sd, w]

    return monsterData


def battle(monsterData):
    userData = init_user()
    health = int(userData[2])
    mHealth = int(monsterData[3])
    a = d = sa = sd = 'Unknown'
    print("""
Monster:     {}                 Your Health: {}/{}
Health:      {}/{}                     Attack:      {}
Attack:      {}                 Defense:     {}
Defense:     {}                 Sp. Attack:  {}
Sp. Attack:  {}                 Sp. Defense: {}
SP. Defense: {}                 Weapon:   {}
            """.format(monsterData[0], health, userData[2], mHealth, monsterData[3], userData[0], a, userData[1], d,
                       userData[3], sa, userData[4], sd, userData[5]))
    while health > 0 and mHealth > 0:
        userAction = user_turn()
        mAction = monster_turn()
        if userAction == 'study':
            a,d,sa,sd = study_seq(a,d,sa,sd,monsterData)
        health, mHealth = outcome(userAction, mAction, userData, monsterData, health, mHealth, a, d, sa,sd)
    if mHealth <= 0:
        win = True
    if health <= 0:
        win = False
    return win


def init_user():
    with open('CharacterData') as c:
        for line in c:
            t = line.split(':')
            if t[0] == 'A':
                c = t[1].strip()
            elif t[0] == 'D':
                d = t[1].strip()
            elif t[0] == 'H':
                h = t[1].strip()
            elif t[0] == 'SA':
                sa = t[1].strip()
            elif t[0] == 'SD':
                sd = t[1].strip()
    with open('Weapon') as a:
        for line in a:
            t = line.split(':')
            if t[0] == 'W':
                weapon = t[1].split(' ')
                w = weapon[0]
    userData = [c, d, h, sa, sd, w]
    return userData


def user_turn():
    done = False
    while not done:
        action = input()
        action = action.lower()
        while action not in ['attack', 'defend', 'study']:
            action = input()
            action = action.lower()
        done = True
    return action


def monster_turn():
    mActions = ['attack', 'defend']
    mAction = mActions[randint(0, 1)]
    return mAction


def outcome(userAction, mAction, userData, monsterData, health, mHealth, a, d, sa, sd):
    defense = int(userData[1])
    mDefense = int(monsterData[2])
    sDefense = int(userData[4])
    mSDefense = int(monsterData[5])
    if userAction == 'defend' or mAction == 'defend':
        if userAction == 'defend':
            defense = defense + 2
            sDefense = sDefense + 2
            print("You defended yourself!")
        if mAction == 'defend':
            mDefense = mDefense + 2
            mSDefense = mSDefense + 2
            print("{} defended itself!".format(monsterData[0]))
    elif userAction == 'attack' or mAction == 'attack':
        if userAction == 'attack':
            damage = attack_seq(userData[0], userData[3], mSDefense, mDefense, userData[5])
            mHealth = mHealth - damage
            print("You did {} damage!".format(damage))
        if mAction == 'attack':
            damage = attack_seq(monsterData[1], monsterData[4], sDefense, defense, monsterData[6])
            health = health - damage
            print("{} did {} damage to you!".format(monsterData[0], damage))
    else:
        pass
    print("""
    Monster:     {}                 Your Health: {}/{}
    Health:      {}/{}                     Attack:      {}
    Attack:      {}                 Defense:     {}
    Defense:     {}                 Sp. Attack:  {}
    Sp. Attack:  {}                 Sp. Defense: {}
    SP. Defense: {}                 Weapon:   {}
                """.format(monsterData[0], health, userData[2], mHealth, monsterData[3], userData[0], a, userData[1], d,
                           userData[3], sa, userData[4], sd, userData[5]))
    return health, mHealth


def attack_seq(attack, sAttack, sDefense, defense, weapon):
    aWeapons = ['Sword', 'Mace', 'Scimitar', 'Axe', 'Knife', 'Spear', 'Teeth', 'Claw']
    sWeapons = ['Wand', 'Staff', 'Tome', 'Gloves']
    if weapon in aWeapons:
        damage = int(attack) - defense
        if damage < 0:
            damage = 0
    elif weapon in sWeapons:
        damage = int(sAttack) - sDefense
        if damage < 0:
            damage = 0
    return damage


def get_loot():
    lootList = []
    with open(r'.\Items\Loot') as loot:
        for line in loot:
            t = line.split(':')
            if t[0] == 'C':
                for placeholder in range(0, 14):
                    lootList.append(t[1])
            elif t[0] == 'U':
                for placeholder in range(0, 9):
                    lootList.append(t[1])
            elif t[0] == 'R':
                lootList.append(t[1])
    loot = lootList[randint(0, len(lootList) - 1)]
    lootStats = loot.split(' ')
    addLoot = get_yes_no("Do you want to keep {}? ".format(loot))
    if addLoot == 'yes':
        with open('Weapon', 'w') as f:
            f.write('W:{}'.format(loot))
        attackPower = lootStats[1][1]
        typeOfAttack = lootStats[1][2]
        if typeOfAttack == 'A':
            with open('CharacterData', 'w+') as c:
                    c.write("""A:{}
D:5
H:10
SA:5
SD:5""".format(5+int(attackPower)))
        elif typeOfAttack == 'S':
            with open('CharacterData','w') as c:
                c.write("""A:5
D:5
H:10
A:{}
SD:5""".format(5 + int(attackPower)))

def dungeon():
    with open('InDungeon') as m:
        for line in m:
            mapPos = line
    if mapPos == '(10, 1)':
        isDungeon = True
    elif mapPos == '(1, 9)':
        isDungeon = True
    elif mapPos == '(9, 7)':
        isDungeon = True
    else:
        isDungeon = False
    return isDungeon


def study_seq(a,d,sa,sd,monsterData):
    stats = ['a', 'd', 'sd', 'sa']
    reveal = stats[randint(0, 3)]
    if reveal == 'a':
        a = monsterData[1]
    elif reveal == 'd':
        d = monsterData[2]
    elif reveal == 'sa':
        sa = monsterData[4]
    elif reveal == 'sd':
        sd = monsterData[5]
    return a,d,sa,sd