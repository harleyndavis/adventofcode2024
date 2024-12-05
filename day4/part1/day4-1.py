
rows = 140
cols = 140
matrix = [[x for x in range(cols)] for y in range(rows)] 
word = "XMAS"

def check4xmas(x,y):
    count = 0
    if matrix[x][y] == word[0]: 
        for x_mod in range(-1, 2):
            for y_mod in range(-1, 2):
                if not (x_mod == 0 and y_mod == 0): 
                    print(f"x: {x}, y: {y}, x_mod: {x_mod}, y_mod: {y_mod}")
                    for i in range(1,4):
                        modded_x = x + x_mod*i
                        modded_y = y + y_mod*i
                        if modded_x < 0 or modded_x >= rows: 
                            print(f"out of bounds X {modded_x}")
                            break                        
                        if modded_y < 0 or modded_y >= cols: 
                            print(f"out of bounds Y {modded_y}")
                            break
                        if matrix[modded_x][modded_y] != word[i]: 
                            print(f"no match: found {matrix[modded_x][modded_y]} at {modded_x}, {modded_y} looking for {word[i]}")
                            break
                        
                        if i == 3: 
                            print(f"found match starting at {x},{y} going {x_mod}{y_mod}")
                            count+=1
                    print()
    return count
                    
                
with open("day4/input.txt", 'r') as file:
    x,y = 0,0
    for line in file:
        y = 0
        for char in line:
            if char == '\n': break
            matrix[x][y]= char
            y += 1
        x +=1

count = 0
for x in range(rows):
    for y in range(cols):
        count += check4xmas(x, y)

print(count)