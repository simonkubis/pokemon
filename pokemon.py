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
    for key, value in attack.items():
        print(key, value, end="\n\n")

def convert(string):
    li = list(string.split(","))
    return li

def checkSimple(string):
    if(len(string.split(" ")) < 2):
        return True
    else:
        return False

def max(a, b):
     
    if a >= b:
        return a
    else:
        return b

def fight(first, second, pokemons):
    team1, team2 = [], []
    power1, power2 = -1, -2
    pokemonsList = convert(pokemons)
    for i in range(0, first + second):
        if(i < first):
            team1.append(pokemonsList[i])
        else:
            team2.append(pokemonsList[i])
    print(team1, team2)
    for main in range(0, first):
        for i in range(0, first + second):
            temp = [1, 1, 1, 1]
            for x in range(0, len(team2[main].split(" "))):
                currentDruhyteam = team2[main].split(" ")[x]
                for y in range(0, len(team1[main].split(" "))):
                    currentPrvyteam = team1[main].split(" ")[y]
                    if(True):
                        print(currentPrvyteam, " vs ", currentDruhyteam)
                        temp[x + y] = attack[currentPrvyteam][currentDruhyteam]
                        power1 += max(temp[0] * temp[2], temp[1] * temp[3])/4
                        power2 += max(temp[0] * temp[2], temp[1] * temp[3])/4
    if(power1 > power2):
        return (power1, power2, "ME")
    elif(power1 < power2):
        return (power1, power2, "FOE")
    else:
        return (power1, power2, "EQUAL")
transform()
fight(2,6,"Psychic Dark,Fire Electric,Ghost Ice,Fairy Electric,Normal Steel,Ghost Steel,Poison Fire,Dark Bug")