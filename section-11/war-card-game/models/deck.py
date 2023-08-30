from random import shuffle
from models import Card, suits, ranks


class Deck:
    all_cards: list[Card]

    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self) -> None:
        shuffle(self.all_cards)

    def deal_one(self) -> Card:
        return self.all_cards.pop()
