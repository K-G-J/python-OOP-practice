class Card:
    def __init__(self, word, location):
        # Hold a card that is a short word
        self.card = word
        # Store location of card 
        self.location = location
        # Card is initially not matche
        self.matched = False
    
    # Check if matched or not
    def __eq__(self, other):
        return self.card == other.card
    
    # Ability to print out the card for the player
    def __str__(self):
        return self.card

if __name__ == "__main__":
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')
    
    print(card1 == card2) # True
    print(card1 == card3) # False
    print(card1) # egg