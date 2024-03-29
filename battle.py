import math

weakness = {
'grass' : 'fire',
'fire' : 'water',
'water' : 'grass'
}

class Pokemon:
    def __init__(self, name, type, level, hp, atk, defe, spatk, spdefe, spd, *args, **kwargs):
        self.name = name
        self.type = type
        self.level = int(level)
        self.hp = int(hp)
        self.atk = int(atk)
        self.defe = int(defe)
        self.spatk = int(spatk)
        self.spdefe = int(spdefe)
        self.spd = int(spd)
        self.weakness = weakness[type]
        self.moves = []

    def moveset(self):
        self.moves = []

    def describe(self):
        return f"""Type: {self.type}\nWeak Against: {self.weakness}"""

    def add(self, move, *args, **kwargs):
        self.moves.append(move)

class BattlePokemon(Pokemon):
    def __init__(self, name, *args, **kwargs):
        self.name = name

class Attack:
    def __init__(self, name, movetype, power):
        self.name = name
        self.movetype = movetype
        self.power = int(power)


def view_pokemon():
    for item in available_pokemon:
        print(f"""\nPOKEMON NAME: {item.name}
Type: {item.type}
Level: {item.level}
STATS:
  HP: {item.hp}  Attack: {item.atk}  Defense: {item.defe}  Special Attack: {item.spatk}  Special Defense: {item.spdefe}  Speed: {item.spd}""")
        print("MOVES:")
        for move in item.moves:
            print(f"""  {move.name}  Type: {move.movetype}  Power: {move.power}""")

def choose_battle_pokemon_1():
    print("\n\nPerfect! The Pokemon that are available for you to battle with are listed above. Take a look and choose your battle Pokemon!")
    battle_pokemon_1 = input("\nNow, go ahead and choose your first Pokemon:\n")
    for pokemon1 in available_pokemon:
        if pokemon1.name == battle_pokemon_1:
            print(f'Great! {pokemon1.name} is a great choice!')
            battle_pokemon_1 = pokemon1
            return battle_pokemon_1
        
def choose_battle_pokemon_2():
    battle_pokemon_2 = input("Now, choose your second Pokemon:\n")
    for pokemon2 in available_pokemon:
        if pokemon2.name == battle_pokemon_2:
            print(f"{pokemon2.name} is a great choice, too! Ready to battle? Let's do it!")
            battle_pokemon_2 = pokemon2
            return battle_pokemon_2

def battle(battle_pokemon_1, battle_pokemon_2):
    while battle_pokemon_1.hp > 0 and battle_pokemon_2.hp > 0:
        if battle_pokemon_2.hp >0:
            print(f'Choose the attack {battle_pokemon_1.name} will use:')
            for move in battle_pokemon_1.moves:
                print(f"""  {move.name}  Type: {move.movetype}  Power: {move.power}""")
            attack = input('Choose your attack!  ')
            for attack1 in battle_pokemon_1.moves:
                if attack1.name == attack:
                    if battle_pokemon_2.weakness == attack1.movetype:
                        modifier = int(4)
                    else:
                        modifier = int(1)
                    damage = math.floor((((((2 * battle_pokemon_1.level) / 5) + 2) * attack1.power * (battle_pokemon_1.atk / battle_pokemon_2.defe)) / 50) + 2) * modifier
                    battle_pokemon_2.hp -= damage
                    if battle_pokemon_2.hp > 0:
                        print(f'\nthe attack did {damage} damage!')
                        print(f'** {battle_pokemon_2.name} has {battle_pokemon_2.hp} HP remaining! **\n')
                    else:
                        print(f'\nthe attack did {damage} damage!')
                        print(f'** {battle_pokemon_2.name} has 0 HP remaining! **\n')
                        print(f'\n{battle_pokemon_2.name} has fainted! {battle_pokemon_1.name} is the winner!')


        if battle_pokemon_2.hp > 0:
            print(f'Choose the attack {battle_pokemon_2.name} will use:')
            for move in battle_pokemon_2.moves:
                print(f"""  {move.name}  Type: {move.movetype}  Power: {move.power}""")
            attack = input('Choose your attack!\n')
            for attack1 in battle_pokemon_2.moves:
                if attack1.name == attack:
                    if battle_pokemon_1.weakness == attack1.movetype:
                        modifier = int(4)
                    else:
                        modifier = int(1)
                    damage = math.floor((((((2 * battle_pokemon_2.level) / 5) + 2) * attack1.power * (battle_pokemon_2.atk / battle_pokemon_2.defe)) / 50) + 2) * modifier
                    battle_pokemon_1.hp -= damage
                    if battle_pokemon_1.hp > 0:
                        print(f'\nthe attack did {damage} damage!')
                        print(f'** {battle_pokemon_1.name} has {battle_pokemon_1.hp} HP remaining! **\n')
                    else:
                        print(f'\nthe attack did {damage} damage!')
                        print(f'** {battle_pokemon_1.name} has 0 HP remaining! **\n')
                        print(f'\n{battle_pokemon_1.name} has fainted! {battle_pokemon_2.name} is the winner!\n')



available_pokemon = []

charmander = Pokemon('charmander', 'fire', 5, 39, 52, 43, 60, 50, 65)
available_pokemon.append(charmander)
bulbasaur = Pokemon('bulbasaur', 'grass', 5, 45, 49, 49, 65, 65, 45)
available_pokemon.append(bulbasaur)
squirtle = Pokemon('squirtle', 'water', 5, 44, 48, 65, 50, 64, 43)
available_pokemon.append(squirtle)

tackle = Attack('tackle', 'normal', 15)
watergun = Attack('water gun', 'water', 40)
ember = Attack('ember', 'fire', 40)
vinewhip = Attack('vine whip', 'grass', 45)

squirtle.add(watergun)
squirtle.add(tackle)
charmander.add(ember)
charmander.add(tackle)
bulbasaur.add(vinewhip)
bulbasaur.add(tackle)

print("""Welcome to the world of Pokemon!
... welp, enough talk! Let's FIGHT!""")

battle_choice = input("Hold on... Darnit, it looks like you don't have any pokemon in your party! That's OK, I have a few you can use for now. Would you like to pick one of mine? (y/n)  ")
if battle_choice == 'y':
    view_pokemon()
else:
    print("That's OK! Peace out girlscout!")

choose_battle_pokemon_1
battle_pokemon_1 = choose_battle_pokemon_1()
choose_battle_pokemon_2
battle_pokemon_2 = choose_battle_pokemon_2()
battle(battle_pokemon_1,battle_pokemon_2)
