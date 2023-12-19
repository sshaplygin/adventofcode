def get_text(is_test = False):
    if is_test: 
        return [
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ]
    text = []
    with open('input.txt', 'r') as file:
        for line in file:
            text.append(line.strip())
     
    return text

def parse_nums(parse_nums):
    nums = filter(lambda n: n.isdigit(), [num for num in parse_nums.strip().split(' ')])
    return set([int(num) for num in nums])

def total_points(text: list[str]):
    r = 0
    for row in text:
        [prefix, nums_str] = row.split('|')
        [_, win_nums] = prefix.split(':')
        l = len(parse_nums(win_nums) & parse_nums(nums_str))
        
        r += 1 << (l - 1) if l > 1 else l
    return r

def total_scratchcards(text: list[str]):
    arr = [1] * len(text)
    for idx, row in enumerate(text):
        [prefix, nums_str] = row.split('|')
        [_, win_nums] = prefix.split(':')
        l = len(parse_nums(win_nums) & parse_nums(nums_str))
        for _ in range(arr[idx]):
            for i in range(l):
                arr[idx + i + 1] += arr[idx] + 
    return sum(arr)

if __name__ == '__main__':
    text = get_text()
    print(total_points(text))
    print(total_scratchcards(text))