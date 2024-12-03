


def safe(input):
    ascending = all(earlier < later and later-earlier <= 3 for earlier, later in zip(input, input[1:]))
    descending = all(earlier > later and earlier - later <= 3 for earlier, later in zip(input, input[1:]))
    
    return ascending or descending

with open("day2/input.txt", 'r') as file:
    total = 0
    line_count = 0
    for line in file:
        line_count += 1
        input = list(map(int, line.split()))
        
        if (safe(input)): 
            print("SAFE NO REMOVAL")
            total += 1
        else:       
            print(input)     
            for index, num in enumerate(input):
                new_copy = input.copy()
                new_copy.pop(index)
                if (safe(new_copy)):
                    print("SAFE REMOVING: " + str(num)) 
                    total += 1
                    break

    print(total)
    print(line_count)