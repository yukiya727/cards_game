import random

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spade", "Heart", "Spade", "Club"]


# create a deck of cards(52 cards)
def create_deck():
    deck = []
    for suit in suits:
        for card in cards:
            # each card will be stored as a dictionary because the group assignment's requirement
            deck.append({
                "suit": suit,
                "card": card
            })
    return deck


# add 2 jokers to a deck
def add_jokers(deck):
    deck.append({
        "suit": "Joker",
        "card": "Big"
    })
    deck.append({
        "suit": "Joker",
        "card": "Little"
    })
    return deck


# create a hand of cards that has n cards
def get_cards(num, deck, remove):
    if num > len(deck):
        print("Not enough cards left in the deck")
        return []
    else:
        hand = random.sample(deck, k=num)
        # remove the randomly selected cards from a deck
        if remove:
            for card in hand:
                deck.remove(card)
        # return both the hand of cards and the remaining deck of cards
        return hand, deck


# compare two cards which one's bigger
def compare_cards(card1, card2):
    # if one of 2 cards is Joker
    if card1["card"] == "Big" or card1["card"] == "Little":
        # card 1 is bigger
        return 1
    elif card2["card"] == "Big" or card2["card"] == "Little":
        # card 2 is bigger
        return 2
    # if both cards are not Joker
    else:
        # if the card's value is bigger
        if cards.index(card1["card"]) > cards.index(card2["card"]):
            # card 1 is bigger
            return 1
            # if both card's number is the same, compare suits
        elif cards.index(card1["card"]) == cards.index(card2["card"]):
            if suits.index(card1["suit"]) > suits.index(card2["suit"]):
                # card 1 is bigger
                return 1
            else:
                # card 2 is bigger
                return 2
        else:
            # card 2 is bigger
            return 2
