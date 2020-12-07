with open('dataset.txt') as f:
    data = {}
    result = 0
    counter = 0
    for line in f.readlines():
        if line == "\n":
            print(data)
            for char in data.keys():
                print(f'{data[char]}\t {counter}')
                if data[char] == counter:
                    result += 1
            data = {}
            counter = 0
        else:
            for char in line:
                if char != '\n':
                    if char in data:
                        data[char] += 1
                    else:
                        data[char] = 1
            counter+=1
    print(result)
