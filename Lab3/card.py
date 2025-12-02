class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value
    
    def getValue(self):
        return  self._value
    def getSuit(self):
        return self._suit
    def __str__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"
                  , "Nine", "Ten", "Jack", "Queen", "King"]
        return f"{values[self._value - 1]} of {suits[self._suit - 1]}"

#Test code:
if __name__ == "__main__":
    card = Card(1, 1)
    print(card)
    print("Value:", card.getValue())
    print("Suit:", card.getSuit())