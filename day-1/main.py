numbers_raw = input()
numbers = numbers_raw.split()
numbers = [int(i) for i in numbers] 

index = 0
number_atm = numbers[index]

iteration = 0
something_map = []

while iteration < len(numbers):
    if len(numbers)-1 == iteration:
        index+=1
        number_atm = numbers[index]
        iteration = index+1

    if numbers[iteration] + number_atm == 2020:
        print(numbers[iteration] * number_atm)
  
    something_map.append([number_atm + numbers[iteration],[number_atm, numbers[iteration]]])
    iteration+=1

for elem in numbers:
    for sum_elem in something_map:
        if elem + sum_elem[0] == 2020:
            print(f"{elem*sum_elem[1][0]*sum_elem[1][1]}\t{elem}-{sum_elem[1]}")

