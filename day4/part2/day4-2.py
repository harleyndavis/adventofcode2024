rows = 140
cols = 140
matrix = [[x for x in range(cols)] for y in range(rows)] 
word = "XMAS"

def check4xmas(x,y):
    count = 0
    if matrix[x][y] == 'A':
        print(f"Found an 'A' at {x}, {y}") 
        
        if x > 0 and x < rows - 1 and y > 0 and y < cols- 1:
            print(f"{matrix[x-1][y-1]} {matrix[x-1][y+1]}")
            print(f" {matrix[x][y]} ")
            print(f"{matrix[x+1][y-1]} {matrix[x+1][y+1]}")
            if (matrix[x-1][y-1] == "M" and matrix[x+1][y+1] == "S" and \
                matrix[x+1][y-1] == "M" and matrix[x-1][y+1] == "S") or \
               (matrix[x-1][y-1] == "M" and matrix[x+1][y+1] == "S" and \
                matrix[x+1][y-1] == "S" and matrix[x-1][y+1] == "M") or \
               (matrix[x-1][y-1] == "S" and matrix[x+1][y+1] == "M") and \
                matrix[x+1][y-1] == "M" and matrix[x-1][y+1] == "S" or \
               (matrix[x-1][y-1] == "S" and matrix[x+1][y+1] == "M" and \
                matrix[x+1][y-1] == "S" and matrix[x-1][y+1] == "M"):
                return 1
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