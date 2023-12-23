import heapq

from collections import Counter

def parse_input(is_test = False):
    text = []
    if is_test:
        text = [
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483',
        ]
    else:
        with open('input.txt', 'r') as file:
            for line in file:
                text.append(line.strip())

    hands = [''] * len(text)
    bids = [0] * len(text)
    for i, row in enumerate(text):
        [hand, bid] = row.split(' ')
        hands[i] = hand
        bids[i] = int(bid)
    return [hands, bids]

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards_with_joker = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

cards_without_joker = {value: index for index, value in enumerate(cards)}
cards_with_joker = {value: index for index, value in enumerate(cards_with_joker)}

types_priority = ['high', 'one', 'two', 'three', 'full_house', 'four', 'five']

def get_values(hand, with_joker = False):
    count_cards = Counter(hand)
    cards_arr = []

    cards_mapping = cards_without_joker
    if with_joker:
        cards_mapping = cards_with_joker
    
    for card in count_cards:
        cards_arr.append((count_cards[card], cards_mapping[card]))
    hand_priority = sorted(cards_arr, key = lambda x: (x[0], x[1]), reverse=True)
    
    res = [get_hand_type(count_cards, hand_priority, with_joker)]
    for card in hand:
        res.append(cards_mapping[card])
    return res

def get_hand_type(count_cards: Counter, hand_priority, with_joker=False):
    t = len(types_priority)-1
    if hand_priority[0][0] == 1:
        t = 0
    if hand_priority[0][0] == 2:
        if len(hand_priority) > 3:
            t = 1
        else:
            t = 2
    if hand_priority[0][0] == 3:
        if len(hand_priority) == 2:
            t = 4
        else:
            t = 3
    if hand_priority[0][0] == 4:
        t = 5

    if with_joker and hand_priority[0][1] != 0:
        t += count_cards.get('J', 0)

    return t

def count_total_winnings(data, with_joker = False):
    [hands, bids] = data
    h = []
    for idx, hand in enumerate(hands):
        heapq.heappush(h, (get_values(hand, with_joker), idx))
    
    total = 0
    for i in range(len(hands)):
        [vals, idx] = heapq.heappop(h)
        total += (i + 1) * bids[idx]
        # debug
        print(f'hand={hands[idx]} type={vals[0]} bid={bids[idx]} rank={i+1}')
    return total

if __name__ == '__main__':
    data = parse_input(True)
    print(count_total_winnings(data))
    print(count_total_winnings(data, True))
