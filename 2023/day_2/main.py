
def parse_input(is_test = False):
    if is_test: 
        return [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]
    text = []
    with open('input.txt', 'r') as file:
        for line in file:
            text.append(line.strip())
    
    return text

def is_valid_game(game):
    game_and_sets = game.split(':')
    if len(game_and_sets) != 2:
        return False
    sets = game_and_sets[1].split(';')
    for s in sets:
        cubes: list[str] = s.split(',')
        for cube in cubes:
            [number, color] = cube.strip().split(' ')
            if max_cubes[color] < int(number):
                return False
    
    return True


# only 12 red cubes, 13 green cubes, and 14 blue cubes
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

def count_possible(text):
    count = 0
    for i, row in enumerate(text):
        if is_valid_game(row):
            count += i + 1
    return count


def max_power(game):
    game_and_sets = game.split(':')
    if len(game_and_sets) != 2:
        return 1
    sets = game_and_sets[1].split(';')
    cubes_power = {'green': 0, 'blue': 0, 'red': 0}
    for s in sets:
        cubes: list[str] = s.split(',')
        for cube in cubes:
            [number, color] = cube.strip().split(' ')
            if cubes_power[color] < int(number):
                cubes_power[color] = int(number)
    
    m = 1
    for val in cubes_power.values():
        m *= val
    return m


def count_cubes_power(text):
    count = 0
    for row in text:
        count += max_power(row)

    return count

if __name__ == '__main__':
    data = parse_input(True)
    print(count_possible(data))
    print(count_cubes_power(data))
