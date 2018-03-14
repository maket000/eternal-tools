import json
import random
import re


CARD_JSON_FILENAME = "cardlist.json"
CARDS_REGEX = re.compile(r"(\d+)\s+.+\s+\(Set(\d+)\s#(\d+)\)")


def generateCard(cardjson):
    print(cardjson)

def generateCardList(card_list_json):
    return {(card["SetNumber"], card["EternalID"]):card for card in card_list_json}

def generatePowerIDList(card_list):
    powers = []
    for c in card_list:
        card = card_list[c]
        if card["Type"] == "Power":
            powers.append(c)
    return powers


def generateRandomDeck(card_list, exclude, count):
    deck = []
    for _ in range(count):
        choice = random.choice(list(card_list.items()))[0]
        while choice in exclude:
            choice = random.choice(list(card_list.items()))[0]
        deck.append(choice)
    return deck

def generateRandomDeckCompact(card_list, exclude, count):
    deck = []
    for _ in range(count//4):
        choice = random.choice(list(card_list.items()))[0]
        while choice in deck or choice in exclude:
            choice = random.choice(list(card_list.items()))[0]
        for _ in range(4):
            deck.append(choice)
    choice = random.choice(list(card_list.items()))[0]
    while choice in deck or choice in exclude:
        choice = random.choice(list(card_list.items()))[0]
    for _ in range(count%4):
        deck.append(choice)
    return deck

def exportDeck(deck, card_list):
    deckstring = ""
    cards = list(set(deck))
    for card in cards:
        card_data = card_list[card]
        count = deck.count(card)
        name = card_data["Name"]
        deckstring += "{} {} (Set{} #{})\n".format(count, name, card[0], card[1])
    return deckstring

def genCard(set_id, card_id):
    return (set_id, card_id)


class Card:
    def __init__(self, name, ):
        pass


class CardTemplate:
    def __init__(self):
        pass


class Deck:
    def __init__(self, deckstring):
        self.cards = []
        for card in CARDS_REGEX.findall(deckstring):
            for count in range(int(card[0])):
                self.cards.append(genCard(int(card[1]), int(card[2])))



with open(CARD_JSON_FILENAME) as f:
    card_list = generateCardList(json.load(f))

power_list = generatePowerIDList(card_list)

rand_deck = generateRandomDeckCompact(card_list, power_list, 50)
print(exportDeck(rand_deck, card_list))
