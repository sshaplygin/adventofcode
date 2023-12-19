def parse_input(is_test = False):
    if is_test: 
        return [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen'
        ]
    text = []
    with open('input.txt', 'r') as file:
        for line in file:
            text.append(line.strip())
    
    return text

def countCalibrationValue(text):
    count = 0
    for row in text:
        i, j = 0, len(row)-1
        while i <= j:
            if row[i].isdigit() and row[j].isdigit():
                count += int(row[i] + row[j])
                break
            if not row[i].isdigit():
                i += 1
            if not row[j].isdigit():
                j -= 1
    return count

def countRealCalibrationValue(text):
    count = 0
    for row in text:
        count += int(getFirstNumber(row) + getFirstNumber(row, True))
    return count

def getFirstNumber(row: str, is_inversed = False):
    rng = range(len(row))
    if is_inversed:
        rng = reversed(rng)
    
    t = trie
    n = numbers
    if is_inversed:
        t = inversed_trie
        n = inversed_numbers
    buf = []
    for i in rng:
        if row[i].isdigit():
            return row[i]
        buf.append(row[i])
        res = t.search(buf)
        
        if not res[0]:
            buf.pop(0)
            continue
        if res[1]:
            return n[''.join(buf)]

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return (False, False)
            node = node.children[char]
        
        return (True, node.is_end)

trie = Trie()
inversed_trie = Trie()

numbers: dict = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
}

inversed_numbers: dict = {}

def init_vars():
    for number in numbers:
        trie.insert(number)
    
    for word in numbers:
        n = ''.join([word[i] for i in reversed(range(len(word)))])
        inversed_numbers[n] = numbers[word]
        inversed_trie.insert(n)

if __name__ == '__main__':
    init_vars()

    data = parse_input(True)

    print(countCalibrationValue(data))
    print(countRealCalibrationValue(data))
