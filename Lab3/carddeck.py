from card import Card
import random

class CardDeck:
    def __init__(self):
        self.reset()
    def shuffle(self):
        random.shuffle(self._cards)
    def getCard(self):
        if len(self._cards) == 0:
            return None
        return self._cards.pop()
    def size(self):
        return len(self._cards)
    def reset(self):
        self._cards = [Card(suit, value) for suit in range(1, 5) for value in range(1, 14)] 

#Test code:
if __name__ == "__main__":
    deck = CardDeck()
    print("Deck size:", deck.size())
    deck.shuffle()
    card = deck.getCard()
    print("Drew card:", card)
    print("Deck size after drawing a card:", deck.size())