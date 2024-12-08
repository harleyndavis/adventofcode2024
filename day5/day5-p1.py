with open("day5/input.txt", 'r') as file:
    rules = []
    rulesDone = False
    count = 0
    for line in file:
        if line == "\n":
            rulesDone = True
        elif not rulesDone:
            rule1, rule2 = line.strip().split('|')
            rules.append((rule1, rule2))
        else: 
            pages = line.strip().split(",")
            followsRules = True
            for rule in rules:
                if rule[0] in pages and rule[1] in pages:
                    ruleOneIndex = pages.index(rule[0])
                    ruleTwoIndex = pages.index(rule[1])
                    if ruleOneIndex > ruleTwoIndex:
                        followsRules = False
                        break
            if followsRules:
                count += int(pages[len(pages) // 2])
    print(count)