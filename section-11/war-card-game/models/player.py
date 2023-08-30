from models import Card


class Player:
    name: str
    all_cards: list[Card]

    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    def remove_one(self) -> Card:
        return self.all_cards.pop(0)

    def add_cards(self, new_cards: list[Card] | Card) -> None:
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards"
