import random  # importing random module to use shuffle function

suits = ("Clubs", "Hearts", "Spades", "Diamonds")
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


class Card:
    """represent a card and must contain a value, dunder str method to show value"""

    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.value}"


class Deck:
    """probably a list containing 52 cards"""

    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank, suit))
            random.shuffle(self.deck)


c1 = Card("A", "Diamonds")
print(c1)
d1 = Deck()
print(d1.deck[1])


"""my own ideas"""


def rank_to_value(rank):
    if rank.isdigit():
        rank_value = int(rank)
    elif rank == "J" or rank == "Q" or rank == "K":
        rank_value = 10
    else:
        rank_value = 11
    return rank_value


print(rank_to_value(ranks[1]))
