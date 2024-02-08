import re

def prettify(hand):
    assert re.search(r'^([2-9TJQKA][SHDC] ?){5}$', hand)
    symbols = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
    for let, suit in symbols.items():
        hand = re.sub(let, suit, hand)
    return hand

# Given a text that represents cards in a standard card deck.
# For example, a poker hand may be represented as "A♥ 4♥ 4♥ K♦ 3♠".
# The 10 of a suit is represented ad "T", such as "T♠".
# This function sorts a hand in descending order by card rank.
def sort_hand(hand):
    # Split the hand into a list of cards
    cards = re.split(r'\s+', hand)

    # Sort the cards by rank
    cards.sort(key=lambda x: x[0], reverse=True)

    # Return the sorted hand
    return ' '.join(cards)

print(sort_hand(prettify('8C AS 4H KS 2C')))