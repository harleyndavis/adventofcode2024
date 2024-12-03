import re


#mul([0-9]{1,3},0-9]{1,3})
with open("day3/input.txt", 'r') as file:
    total = 0
    compute = True
    for line in file:
        x = re.findall("mul\((?P<first>[0-9]{1,3}),(?P<second>[0-9]{1,3})\)|(?P<third>do\(\))|(?P<fourth>don't\(\))", line)
        for tuple in x:
            if tuple[2] == "do()":
                compute = True
            elif tuple[3] == "don't()":
                compute = False
            elif compute:
                total += int(tuple[0]) * int(tuple[1])

    print(total)