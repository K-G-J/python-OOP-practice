from cards import Card
import random


class Game:
    def __init__(self):
        # Grid size
        self.size = 4
        # Card options (if grid size is 4x4 then 16 cards in grid and since we are matching we need 8 options of words the same length)
        self.card_options = ['Add', 'Boo', 'Cat',
                             'Dev', 'Egg', 'Far', 'Gum', 'Hut']
        # Columns (need 4 columns name)
        self.columns = ['A', 'B', 'C', 'D']
        # Empty list to hold card instances for the game once created
        self.cards = []
        # List of all the locations in the grid
        self.locations = []
        for column in self.columns:
            # Need locations 1-4 for each letter column
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')

    # Methods

    # Create cards
    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            # Create 2 cards for every word
            for i in range(2):
                # Make lists into sets to remove duplicates and then subract them
                available_locations = set(
                    self.locations) - set(used_locations)
                # Convert back to a list to use random
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                # Create card instance
                card = Card(word, random_location)
                self.cards.append(card)

    # Create grid
    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
        return row

    def create_grid(self):
        # |  A  |  B  |  C  |  D  |
        header = ' |  ' + '  |  '.join(self.columns) + '  |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + ' |'
            print(print_row)

    # Check for matches
    def check_matches(self, loc1, loc2):
        cards = []
        for card in self.cards:
            # See what cards match the user choosen locations
            if card.location == loc1 or card.location == loc2:
                # Add choosen cards to list
                cards.append(card)
       # Check if choosen cards are matches
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f'{card.location}: {card}')
            return False

    # Check if the game is won
    def check_win(self):
        for card in self.cards:
            # Game hasn't been won
            if card.matched == False:
                return False
            else:
                # Game is won (all card.matched == True)
                return True

    # Make sure player input is a correct location
    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card?  ")
            if guess.upper() in self.locations:
                # Guess is a location to return it
                return guess.upper()
            else:
                # Guess is not a valid location
                print("That's not a valid location. It should look like this: A1")

    # Run the game
    def start_game(self):
        game_running = True
        print('Memory Game')
        # First, create the cards
        self.set_cards()
        while game_running:
            # Print grid for the player to see and guess
            self.create_grid()
            # Ask player for guess
            guess1 = self.check_location('first')
            guess2 = self.check_location('second')
            # After player guesses locations, check card matches
            if self.check_matches(guess1, guess2):
                # If cards match, see if game is won
                if self.check_win():
                    print('Congrats!! You have guessed them all!')
                    self.create_grid()
                    # Stop the game while loop
                    game_running = False
            else:
                # The cards were not a match
                input('Those cards are not a match. Press enter to continue')

        print('GAME OVER')


# Dunder main
if __name__ == "__main__":
    # Create game instance
    game = Game()
    # Call the start method
    game.start_game()
