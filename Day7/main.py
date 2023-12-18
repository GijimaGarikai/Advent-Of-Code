"""General idea is we give each hand a rating. The type of hand it is
   will determine its value primarily, other factors like value of cards
   position of said cards will matter secondarily. I'll use orders of
   magnitude to achieve this. A hand is worth 1000*(it's rank),
   a card is worth 10*(it's rank)"""

with open("input.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split()
    bids = {}
    # split data into bids and hands
    for hand in data:
        bids[hand[0]] = hand[1]
# store values of cards and hands
cards = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8,
         '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
hands = {'five': 7, 'four': 6, 'full': 5, 'three': 4, 'two': 3, 'one': 2, 'high': 1}
positions = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
# primes where the next value is atleast 13X less than previous so
# only position is most important factor
primes = [499979, 39989, 2671, 211, 17]

def get_hand(hand):
    # determine the kind of hand we have
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if len(cards) == 1:
        return 'five'
    elif len(cards) == 2:
        for card in cards:
            if cards[card] == 4:
                return 'four'
            if cards[card] == 3:
                return 'full'
    elif len(cards) == 3:
        for card in cards:
            if cards[card] == 3:
                return 'three'
            if cards[card] == 2:
                return 'two'
    elif len(cards) == 4:
        return 'one'
    else:
        return 'high'

def get_hand_val(hand):
    # hand is the most important attribute so it dominates
    total = hands[get_hand(hand)]*(10**8)
    for i in range(len(hand)):
        card = hand[i]
        # position is next most important so it's second
        total += cards[card]*positions[i]*primes[i]
    return total
# store mapping between a hand, it's bid, and it's value
values = {}
# store values of hands for sorting
values_arr = []
for hand in data:
    bid = int(hand[1])
    hand = hand[0]
    value = get_hand_val(hand)
    values[value] = [hand, bid]
    values_arr.append(value)
values_arr.sort()
total = 0
for i in range(len(values_arr)):
    val = values_arr[i]
    total += values[val][1]*(i+1)
print(total)



