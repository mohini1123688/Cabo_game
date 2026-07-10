import random
from dataclasses import dataclass, field

suits = ["Heart", "Spade", "Club", "Diamond"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

@dataclass
class Card:
    value: int
    suit: str

@dataclass
class Deck:
    game_state: "Game_State"
    cards: list = field(default_factory=list)

    def __post_init__(self):
        self.create_deck()
        self.shuffle_deck()
        self.game_state.deck_order = self.cards

    def create_deck(self):
        for suit_type in suits:
            for value in values:
                self.cards.append(Card(value, suit_type))
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

@dataclass
class Player:
    name: str
    game_state: "Game_State"
    hand: list = field(default_factory=list)
    total: int = 0

    def pick_up_card(self):
        card = self.game_state.deck_order.pop()
    
    def look_at_own_card(self, card_chosen):
        print(f'Own card: {card_chosen}')
    
    def look_at_opponent_card(self, card_chosen, owner):
        print(f'{self.game_state.players[owner]} card: {card_chosen}')

@dataclass
class Opponent(Player):
    def play_turn(self):
        print("played turn")

@dataclass
class Game_State:
    players: list = field(default_factory=list)
    game_winner: str = ""
    current_turn_number: int = 1
    current_turn_player: int = 0
    discard_pile: list = field(default_factory=list) # []
    deck_order: list = field(default_factory=list)
    react: bool = False
    power_time: bool = False

    def __post_init__(self):
            self.players = [
                Player("Player1", self),
                Player("Opponent1", self),
                Player("Opponent2", self),
                Player("Opponent3", self)
            ]

    def deal_cards(self):
        for index, player in enumerate(self.players):
            for card in range(4):
                self.players[index].total = self.players[index].total + self.deck_order[-1]
                self.players[index].hand.append(self.deck_order.pop())
    
    def discard_chosen(self, new_card):
        self.discard_pile.append(new_card)

    def swap_card_picked(self, choice, new_card):
        self.discard_pile.append(self.players[self.current_turn_player].hand[choice])
        self.players[self.current_turn_player].hand[choice] = new_card
    
    def game_finished(self, player_who_called):
        min_score = min(player.total for player in self.players)
        winners = [player.name for player in self.players if player.total == min_score]
        while len(winners) != 1:
            if player_who_called in winners:
                winners.remove(player_who_called)
            min_number_of_cards = min(len(player.hand) for player in winners)
            winners = [player.name for player in self.players if player.total == min_number_of_cards]
            winners.remove(random.choice(winners))
            winners.remove(random.choice(winners))
            
        self.game_winner = winners[0]
        print(f"Winner is... {self.game_winner}")

def main():
    game_state = Game_State()
    game_deck = Deck(game_state)

    #for card in game_state.deck_order:
            #print(f'{card.value} of {card.suit}')

    print(f'Initial card count: {len(game_state.deck_order)}')

    game_state.deal_cards()

    print(f'After cards dealt: {len(game_state.deck_order)}')

    print("START GAME")
    print(f"Turn number: {game_state.current_turn_number}")
    print(f"{game_state.players[game_state.current_turn_player].name} Turn")
    print(f'Revealed Cards {game_state.players[0].hand[2]} and {game_state.players[0].hand[3]}')

    choice = input("Would you like to call Cabo? (y/n)")
    print(f"You chose: {choice}")
    if choice == 'y':
        game_state.game_finished(game_state.players[game_state.current_turn_player].name)

    new_card = game_state.players[0].pick_up_card()
    print(new_card)

    choice = input("Would you like to swap or discard? (s/d)")
    print(f"You chose: {choice}")

    if choice == 'd':
        game_state.discard_chosen(new_card)
    if choice =='s':
        choice = int(input("What card would you like to swap with? Top-left(0) Top-right(1) Bottom-left(2) Bottom-right(3)"))
        game_state.swap_card_picked(choice, new_card) #performs discard
    
    game_state.react = True
    #Runs out after 10 seconds
    #each player can click their card or someone else's to have one less card
    #if u click wrong u get a penalty card (yours or opponent), if u had clicked an opponents card their card is not revealed if u clicked wrong
    #if u clicked opponent card right, you get to give them one of ur cards

    game_state.react = False
    #if u discarded a power card here you get to use it
    if game_state.discard_pile[-1] >7:
        game_state.power_time = True
    '''
    if game_state.discard_pile[-1] == 7 or 8:
        choice = input("Which of YOUR cards would you like to look at")
    if game_state.discard_pile[-1] == 9 or 10:
        choice = input("Which of YOUR OPPONENTS cards would you like to look at")
    if game_state.discard_pile[-1] == 11:
        print("turn skipped")
    if game_state.discard_pile[-1] == 12:
        print("blind swap")
    if game_state.discard_pile[-1] == 13:
        print("seen swap")
    '''
    game_state.power_time = False
    
if __name__ == "__main__":
    main()