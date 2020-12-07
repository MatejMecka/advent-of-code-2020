data = {}

def find_golden_bags(searched_bag, counter=0):
    if 'shiny-gold' in [ el[1] for el in data[searched_bag]]:
        return True
    val = False
    for bag in data[searched_bag]:
        val = val or find_golden_bags(bag[1], counter)
    return val

def bag_counter(bag):
    total_counter = 1
    print(data[bag])
    for ele in data[bag]:
        print(ele)
        total_counter += ele[0] * bag_counter(ele[1])
    return total_counter

with open('dataset.txt') as f:
    for line in f.readlines():
        words = line.split()
        bag = f"{words[0]}-{words[1]}"
        
        if words[4] == "no":
            data[bag] = []
        else:
            counter = 4
            processed_bags = 0
            data[bag] = []
            while processed_bags < line.count(',')+1:
                number = words[counter]
                contained_bag = f"{words[counter+1]}-{words[counter+2]}"
                data[bag].append([int(number), contained_bag]) 
                processed_bags+=1
                counter+=4

counter = 0
for key in data.keys():
    if find_golden_bags(key):
        counter+=1
    

print(f"Bags containing a Golden Bag: {counter}")
print(f"Amount of bags to buy: f{bag_counter('shiny-gold')-1})
