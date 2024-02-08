import re

def prettify(hand):
    assert re.search(r'^([2-9TJQKA][SHDC] ?){5}$', hand)
    symbols = {'S': '♠', 'H': '♥', 'D': '♦', 'C': '♣'}
    for let, suit in symbols.items():
        hand = re.sub(let, suit, hand)
    return hand

def cardsort(hand):
    def by_num(card):
        map = {'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E'}
        num = card[0]
        return num if num not in 'AKQJT' else map[num]
    
    def by_suit(card):
        map = {'♣': 1, '♦': 2, '♥': 3, '♠': 4}
        return map[card[1]]
    
    hand = re.split(' ', hand)
    hand.sort(key=by_suit, reverse=True)
    hand.sort(key=by_num, reverse=True)
    return ' '.join(hand)

print(cardsort(prettify('8C AS 4H KS 2C')))