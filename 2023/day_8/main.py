import math

def get_test_data(part):
    text = [
        'RL',
        '',
        'AAA = (BBB, CCC)',
        'BBB = (DDD, EEE)',
        'CCC = (ZZZ, GGG)',
        'DDD = (DDD, DDD)',
        'EEE = (EEE, EEE)',
        'GGG = (GGG, GGG)',
        'ZZZ = (ZZZ, ZZZ)',
    ]

    if part != 1: 
        text = [
            'LR',
            '',
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)',
        ]
    return text

def parse_input(is_test = False, part=1):
    text = []
    if is_test:
        text = get_test_data(part)
    else:
        with open('input.txt', 'r') as file:
            for line in file:
                text.append(line.strip())
    steps = [c for c in text[0]]
    network = {}

    for idx in range(2, len(text)):
        [point, ways] = text[idx].split(' = ')
        network[point] = [ways[1:4:], ways[-4:-1]]

    return (steps, network)

def count_steps(data):
    [steps, network] = data
    i, res = 0, 0
    poisiton = 'AAA'
    is_end_step = False
    while not is_end_step:
        idx = i % len(steps)
        direct = steps[idx]
        move = 1 if direct == 'R' else 0
        next_step = network[poisiton][move]
        if next_step == 'ZZZ':
            is_end_step = True
        poisiton = next_step
        res += 1
        i += 1
    return res

def count_blind_steps(data):
    [steps, network] = data
    i, res = 0, 1
    positions = []

    for point in network:
        if point[2] == 'A':
            positions.append(point)
    
    position = positions.pop()
    desigions = []

    is_end_step = False
    while not is_end_step:
        idx = i % len(steps)
        
        direct = steps[idx]
        move = 1 if direct == 'R' else 0

        next_step = network[position][move]
        if next_step[2] == 'Z':
            if len(positions) == 0:
                desigions.append(res)
                is_end_step = True
                continue
            position = positions.pop()
            desigions.append(res)
            i = 0
            res = 1
            continue
        position = next_step

        i += 1
        res += 1
    
    return math.lcm(*desigions)

if __name__ == '__main__':
    print(count_steps(parse_input(True)))
    print(count_blind_steps(parse_input(True, part=2)))