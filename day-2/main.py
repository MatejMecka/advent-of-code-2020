import os

f = open("dataset_2.txt", "r")
results = 0
results_verification_other = 0

for line in f.readlines():
    part = line.split()
    ranges = part[0].split('-')
    
    password = part[2]
    letter = part[1].replace(':', '')

    mini = int(ranges[0])
    maxi = int(ranges[1])

    ##### Part 1 ##########
    temp_score = 0
    for let in password:
       if let == letter:
           temp_score+=1

    if temp_score >= mini and temp_score <= maxi:
        results+=1
        print(f'MATCH PART 1: {password}')

    ##### Part 2 ##########
    mini -= 1
    maxi -= 1
    if password[mini] == letter:
        if password[maxi] != letter:
            print(f'MATCH PART 2: {password}')
            results_verification_other+=1
    elif password[maxi] == letter:
        if password[mini] != letter:
            print(f'MATCH PART 2: {password}')
            results_verification_other+=1

print(f'Results from Part 1: {results}\n Results from Part 2: {results_verification_other}')

