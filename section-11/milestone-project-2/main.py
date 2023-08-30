import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
value = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

playing = True


class Card:
    suit: str
    rank: str

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    deck: list[Card]

    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit=suit, rank=rank))

    def __str__(self) -> str:
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    cards: list[Card]
    value: int
    aces: int

    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.value += value[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    total: int
    bet: int

    def __init__(self, total=100) -> None:
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips: Chips):
    while True:
        try:
            chips.bet = int(input("How many chps wuold you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(
                    "Sorry, you do not have enough chips! You have: {}".format(
                        chips.total
                    )
                )
            else:
                break


def hit(deck: Deck, hand: Hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: Deck, hand: Hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s")
        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0].lower() == "s":
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did no understand that, Please enter h or s only!")
            continue
        break


def show_some(player: Hand, dealer: Hand):
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player: Hand, dealer: Hand):
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player: Hand, dealer: Hand, chips: Chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player: Hand, dealer: Hand):
    print("Dealer and player tie! PUSH")


while True:
    print("WELCOME TO BLACKJACK")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\n Player's total chips are at: {}".format(player_chips.total))
    new_game = input("Would you like to play another hand? y/n")

    if new_game[0].lower() == "y":
        playing = True
    else:
        print("Thank you for playing")
        break
