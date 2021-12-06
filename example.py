import Deck

if __name__ == '__main__':
    decks = [Deck.create_deck()]
    hands = []
    for i in range(4):
        hand, decks[0] = Deck.get_cards(13, decks[0], remove=True)
        hands.append(hand)

    for i in range(4):
        print("Player {}'s cards:".format(i + 1))
        print(hands[i])

    print("\n--P1 Vs P2--")
    choices = []
    for i in range(2):
        print("Player {}'s choice of card:".format(i+1))
        choice, hands[0] = Deck.get_cards(1, hands[0], remove=True)
        choices.append(choice[0])
        print(choices[i])

    result = Deck.compare_cards(choices[0], choices[1])
    print("**Player {} wins!**".format(result))


