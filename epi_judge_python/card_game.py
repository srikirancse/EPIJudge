import random


class Deck:
    """This is a class for operations on a deck of cards."""
    def __init__(self):
        """The constructor for Deck class."""
        self.cards = [i for i in range(52)]

    def shuffle(self):
        """Shuffles the cards in the deck in-place."""
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.cards)


class Player:
    """
    This is a class representing the player in the game.

    Attributes:
        name (string): The name of the player.
        cards (list): The cards of the player.
    """
    def __init__(self, name, cards):
        """
        The constructor for Player class. 

        Parameters: 
           name (string): The name of the player.
           cards (list): The cards of the player.
        """
        self.name = name
        self.cards = cards

    def cards_empty(self):
        """
        Tells if the cards of the player are empty.

        Returns:
            boolean: The boolean true if the cards are empty and vice versa.
        """
        return len(self.cards) == 0


class Game:
    """
    This is a class representing the game and it's state.

    Attributes:
        player1 (string): The name of the first player.
        player2 (string): The cards of the second player.
    """
    def __init__(self, player1, player2):
        """
        The constructor for Game class.

        Parameters:
           player1 (string): The name of the first player.
           player2 (string): The cards of the second player.
        """
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(player1, self.deck.cards[:26])
        self.player2 = Player(player2, self.deck.cards[26:])
        self.turn = 0
        self.pile = []

    def pick(self):
        """
        The function to pick the card from the active player's cards.

        Returns:
            int: The number of card in the deck.
        """
        if self.turn:
            return self.player2.cards.pop()

        return self.player1.cards.pop()

    def round_winner(self, current_card):
        """
        The function to return the winner of the current round.

        Returns:
            int: 0 if player 1 is the round winner and 1 if player 2 is the round winner.
        """
        return 0 if self.turn and (self.pile[-1] % 13) > (current_card % 13) or not self.turn and (
            self.pile[-1] % 13) < (current_card % 13) else 1

    def play(self):
        """
        The function to play the game between the cards of 2 players. 

        Returns:
            int: 0 if player 1 won and 1 if player 2 won the game. 
        """
        while not self.player1.cards_empty() and not self.player2.cards_empty():
            new_card = self.pick()
            if len(self.pile) == 0 or self.pile[-1] % 13 == new_card % 13:
                self.pile.append(new_card)
                # Toggle the turn.
                self.turn ^= 1
                continue

            round_winner = self.round_winner(new_card)

            # Round winner claims the cards.
            if round_winner:
                self.player2.cards.extend(self.pile)
            else:
                self.player1.cards.extend(self.pile)

            # Empty the pile.
            self.pile = []
            # Toggle the turn.
            self.turn ^= 1

        return 1 if self.player1.cards_empty() else 0


game = Game('sri', 'jason')
print('Jason has won the game' if game.play() else 'Sri has won the game')
