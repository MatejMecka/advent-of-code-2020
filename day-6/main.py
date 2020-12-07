with open('dataset.txt') as f:
    data = {}
    result = 0
    for line in f.readlines():
        if line == "\n":
            result += len(data.keys())
            data = {}    
        else:
            for char in line:
                if char != '\n':
                    data[char] = True
    print(result)
