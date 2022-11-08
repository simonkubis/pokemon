import requests, json

raw = 'https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json'
data = requests.get(raw)
dataJson = json.loads(data.text)

def translate(to):
    return {"super effective":2.0, "normal effective":1.0, "not very effective":0.5, "no effect":0.0}[to]

attack = {"Normal": {}, "Fire": {}, "Water": {}, "Electric": {}, "Grass": {}, "Ice": {}, "Fighting": {}, "Poison": {}, "Ground": {}, "Flying": {}, "Psychic": {}, "Bug": {}, "Rock": {}, "Ghost": {}, "Dragon": {}, "Dark": {}, "Steel": {}, "Fairy": {}}

def transform():
    for power, pokemons in dataJson.items():
        for pokemon, against in pokemons.items():
            for one in against:
                attack[pokemon].update({one:translate(power)})


def convert(string):
    li = list(string.split(","))
    return li

def create(a, b, pokemons, reverse):
    team1, team2 = [], []
    for i in range(0, a):
        team1.append(pokemons.split(",")[i])
    for i in range(a, b + a):
        team2.append(pokemons.split(",")[i])
    if reverse:
        return [team2, team1]
    else:
        return [team1, team2]
    


def fight(a, b): 
    my = 0.0 
    for moj_poke in a:
        if " " in moj_poke: 
            moj_poke = moj_poke.split(" ") 
            for jeho_poke in b: 
                if " " in jeho_poke: 
                    jeho_poke = jeho_poke.split(" ")
                    my += max(attack[moj_poke[0]][jeho_poke[0]]*attack[moj_poke[0]][jeho_poke[1]], attack[moj_poke[1]][jeho_poke[0]]*attack[moj_poke[1]][jeho_poke[1]])
                else: 
                    my += max(attack[moj_poke[0]][jeho_poke], attack[moj_poke[1]][jeho_poke])
        else:
            for jeho_poke in b:
                if " " in jeho_poke:
                    jeho_poke = jeho_poke.split(" ")
                    my += attack[moj_poke][jeho_poke[0]]*attack[moj_poke][jeho_poke[1]]
                else: 
                    my += attack[moj_poke][jeho_poke]
    return round(my,1) 


def start():
    power1 = fight(create(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug", False)[0], create(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug", False)[1])
    power2 = fight(create(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug", True)[0], create(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug", True)[1])
    win = ''
    if(power1 > power2):
        win = 'ME'
    elif(power1 < power2):
        win = 'FOE'
    else:
        win = 'EQUAL'
    return power1, power2, win


transform()
print(start())