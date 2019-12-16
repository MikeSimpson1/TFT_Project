import json


# INITIALIZER CLASSES AND FUNCTIONS ############################################
class Champion:
    def __init__(self, name, cost, traits, image):
        self.name = name
        self.cost = cost
        self.traits = traits
        self.image = image
    def __str__(self):
        return "Champion: {0:8} Cost: {1:1} \tTraits: {2:20}".format(self.name, self.cost, self.traits)

    def printName(self):
        return self.name

class Trait:
    def __init__(self, name, description, sets):
        self.name = name
        self.description = description
        self.sets = sets

class Item:
    def __init__(self, name):
        self.name = name

def importChamps():
    with open('TFT_Program/champions.json','r') as f:
        jsonChamps = json.load(f)
    champsList = {}
    for champ in jsonChamps:
        champsList[champ["champion"]] = Champion(champ["champion"], champ["cost"], champ["traits"], champ["image"])
    return champsList

def importTraits():
    with open('TFT_Program/traits.json','r') as f:
        jsonTraits = json.load(f)
    traitsList = []
    for trait in jsonTraits:
        traitsList.append(Trait(trait["name"], trait["description"], trait["sets"]))
    return traitsList

def importItems():
    with open('TFT_Program/items.json','r') as f:
        jsonItems = json.load(f)
    itemsList = []
    for item in jsonItems:
        itemsList.append(Item(item["name"]))
    return itemsList

def initializeProgram():
    return importChamps(), importTraits(), importItems()
################################################################################


#Groups champions based on their common traits, prints based on printBool
def groupByTraits(champDeck, printBool):
    groupedTraits = {}

    for champ in champDeck:
        name = champ.name
        traits = champ.traits
        for x in traits:
            if x not in groupedTraits:
                groupedTraits[x] = []
            groupedTraits[x].append(champ)

    if (printBool):
        for trait in groupedTraits:
            print(("{0:" + str(len(trait)) + "}[{1:1}]:").format(trait, len(groupedTraits[trait])))
            champs = groupedTraits[trait]
            for champ in champs:
                print("\t" + champ.printName())
    return groupedTraits


# Counts number of champs with specified trait, if number matches last entry in the array then the trait is gold tier and returned true


def isTraitGold(deck, trait):
    counter = 0
    for champ in deck:
        if trait.name in champ.traits:
            counter+=1

    return counter >= trait.sets[len(trait.sets)-1]

def getChamp(strName):
    if strName in championsList:
        return championsList[strName]
    throwError(2, strName)
    return Champion("ERROR",0,[],"")

def getChampList(strList):
    champions = []
    for champ in strList:
        champions.append(getChamp(champ))
    return champions

def getTrait(strName):
    for trait in traitsList:
        if trait.name == strName:
            return trait
    throwError(1, strName)
    return Trait("ERROR","",[99])

def throwError(errorCode, argument):
    errorDict = {
        1: "ERROR: TRAIT NOT FOUND: " + argument,
        2: "ERROR: CHAMPION NOT FOUND: " + argument,
        3: "ERROR: ITEM NOT FOUND: " + argument
    }
    print(errorDict.get(errorCode))


###########################
def main():
    testDeck = getChampList(["KogMaw","RekSai","Skarner","Annie", "LeBlanc"])


    print(getChamp("Veigar"))



# INITIALIZE GLOBAL VARIABLES
championsList , traitsList , itemsList = initializeProgram()

# RUN FILE
main()
