with open("day5/test_input.txt", 'r') as file:
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
            #everything until this point is good, but we now want the non rule following pages.
            if not followsRules:
                newOrder = [pages.pop(0)]
                while len(pages) > 0:
                    added = False
                    nextPage = pages.pop(0)
                    for index, page in enumerate(newOrder):
                        if (nextPage, page) in rules:
                            newOrder.insert(index, nextPage)
                            added = True
                            break
                    if not added: newOrder.append(nextPage)
                print(f"newOrder is: {newOrder}")
                
                count += int(newOrder[len(newOrder) // 2])
    print(count)