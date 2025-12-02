from carddeck import CardDeck


def main():
    deck = CardDeck()
    deck.shuffle()
    while deck.size() > 0:
        card = deck.getCard()
        print("Card {} has value {}".format(card, card.getValue()))


if __name__ == "__main__":
    main()
