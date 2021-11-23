import random

def generate_deck():
    deck = []
    suits = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for suit in suits:
        for face in faces:
            deck.append(suit + face)
    return deck

def shuffle_cards(cards):
    random.shuffle(cards)
    return cards

decks = []
decks.append(shuffle_cards(generate_deck()))
for i in range(0,1000):
    workingDeck = generate_deck()
    shuffledDeck = shuffle_cards(workingDeck)
    for a in range(len(decks)-2, 0, -1):
        if decks[a] == shuffledDeck:
            print("Shuffling failed")
            break
    decks.append(shuffledDeck)
    print(shuffledDeck, "\n")

print(len(decks))
