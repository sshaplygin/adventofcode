from collections import Counter
import heapq

def parse_input(is_test = False):
    text = []
    if is_test:
        text = [
            '32T3K 765', # two [1, 1], 0 rank = 1
            'T55J5 684', # three [2, 3], 1 rank = 4
            'KK677 28',  # two  [1, 11] 2 rank = 3
            'KTJJT 220', # two [1, 8] 3, rank = 2
            'QQQJA 483', # three [2, 10] 4, rank = 5
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
cards_mapping = {value: index for index, value in enumerate(cards)}
types_priority = ['high', 'one', 'two', 'three', 'full_house', 'four', 'five']

def get_values(hand):
    count_cards = Counter(hand)
    cards_arr = []
    for card in count_cards:
        cards_arr.append((count_cards[card], cards_mapping[card]))
    sorted_list = sorted(cards_arr, key = lambda x: (-x[0], -x[1]))
    
    t = len(types_priority)-1
    if sorted_list[0][0] == 1:
        t = 0
    if sorted_list[0][0] == 2:
        if len(sorted_list) > 3:
            t = 1
        else:
            t = 2
    if sorted_list[0][0] == 3:
        if len(sorted_list) == 2:
            t = 4
        else:
            t = 3
    if sorted_list[0][0] == 4:
        t = 5
    res = [t]
    for card in hand:
        res.append(cards_mapping[card])
    return res

def count_total_winnings(data):
    [hands, bids] = data
    h = []
    for idx, hand in enumerate(hands):
        heapq.heappush(h, (get_values(hand), idx))
    
    total = 0
    for i in range(len(hands)):
        [_, idx] = heapq.heappop(h)
        print(f'hand={hands[idx]} bid={bids[idx]} rank={i+1}')
        total += (i + 1) * bids[idx]
    return total

if __name__ == '__main__':
    data = parse_input()
    print(count_total_winnings(data))
