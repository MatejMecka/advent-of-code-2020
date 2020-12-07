with open('dataset.txt') as f:
    counter = 0
    max_value = 0
    ids = []
    for line in f.readlines():
        line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L','0')
        fin_row = int(line[0:7], base=2)
        fin_col = int(line[7:10], base=2)
        
        result = fin_row * 8 + fin_col
        ids.append(result)
        print(f'BOARDING PASS ID {counter} SEAT RESULT: {result}. ROW: {fin_row} COLUMN: {fin_col}')
        if result > max_value:
            max_value = result
        counter+=1
    print(f'ANSWER: {max_value} \t {max(ids)}')

    for id in range(min(ids), max(ids)):
        if id not in ids:
            print(f'LOCATED SEAT! ANSWER: {id}')

