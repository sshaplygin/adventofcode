def parse_input(is_test = False, is_ignore = False):
    text = []
    if is_test:
        text = [
            'Time:      7  15   30',
            'Distance:  9  40  200',
        ]
    else:
        with open('input.txt', 'r') as file:
            for line in file:
                text.append(line.strip())
    if is_ignore:
        t = [int(text[0].split(":")[1].replace(' ', ''))]
        dist = [int(text[1].split(":")[1].replace(' ', ''))]
        return (t, dist)
    
    t = [int(c) for c in text[0].split(":")[1].split()]
    dist = [int(c) for c in text[1].split(":")[1].split()]

    return (t, dist)
        

def count_max_ways(data):
    res = 1
    for race_idx in range(len(data[0])):
        left, right = -1, -1
        for i in range(1, data[0][race_idx]-1):
            if float(data[0][race_idx]) - (i + float(data[1][race_idx]/i)) > 0:
                left = i - 1
                break

        for i in range(data[0][race_idx]-1, 0, -1):
            if float(data[0][race_idx]) - (float(data[1][race_idx]/i) + i) > 0:
                right = i
                break
        res *= right - left
    return res

if __name__ == '__main__':
    data = parse_input(True)
    print(count_max_ways(data))

    data = parse_input(True, is_ignore=True)
    print(count_max_ways(data))
