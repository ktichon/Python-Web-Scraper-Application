"""
Simulates a deck of cards, with classes to create a card and to create the deck
"""
import random
#Command to generate documentation = 'python -m pydoc -w .\', run from local folder
class Card:
    """
    The card class is a single playing card, initialised with a suit and number
    """
    def __init__(self, suit, number):
        """Initializes the suit and number of the card"""

        self._suit = suit
        self._number = number

    def __repr__(self):
        """Returns a string of the number and suit"""
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """Stores the suit of card"""
        return self._suit

    @suit.setter
    def suit(self, suit):
        """Sets the suit of the card"""
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """Gets the number of the card"""
        return self._number

    @number.setter
    def number(self, number):
        """Validates and sets the number of the card"""
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The deck class repersents a deck, in suit and number order
    """
    def __init__(self):
        """Initializes the deck of cards"""
        self._cards = []
        self.populate()

    def populate(self):
        """Populates the deck with 52 cards in order"""
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """Radomizes the order of cards in the deck"""
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """Removes a numbers of cards from deck and returns a list with the dealt cards"""
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """The 'ToString' method, returns the number of cards in the deck"""
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"

deck = Deck()
print(deck)