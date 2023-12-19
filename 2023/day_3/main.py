def get_text(is_test = False):
    if is_test: 
        return [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..',
        ]
    text = []
    with open('input.txt', 'r') as file:
        for line in file:
            text.append(line.strip())
    
    return text

steps = [[-1, -1], [-1, 0], [-1, +1], [0, +1], [+1, +1], [+1, 0], [+1, -1], [0, -1]]

def check_around(arr, i, j):
    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
        return False
    if arr[i][j] != "." and not arr[i][j].isdigit():
        return True
    return False

def sum_parts(arr):
    s = 0
    for i in range(len(arr)):
        data = []
        is_valid = False
        for j in range(len(arr[0])):
            if arr[i][j].isdigit():
                if not is_valid:
                    for step in steps:
                        if check_around(arr, i + step[0], j + step[1]):
                            is_valid = True
                data.append(arr[i][j])
                arr[i][j] = '.'
                continue
            if len(data) != 0 and is_valid:
                s += int(''.join(data))
                data = []
                is_valid = False

    return s

def make_matrix(text):
    arr = [] * len(text)
    for i in range(len(text)):
        arr.append([])
        for j in range(len(text[0])):
            arr[i].append(text[i][j]) 
    return arr

if __name__ == '__main__':
    text = get_text()
    print(sum_parts(make_matrix(text)))
