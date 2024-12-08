# day six part one
# finding unique squares guard visits on map.
# guard's starting position is denoted by '^' on map.
# guard starts heading "up" ( negative x direction)
# guard goes straight unless encountering obstruction
# when encountering obstruction guard turns right 90 degrees.
# example, first obstruction, guard turns to positive y direction.
# map consists of '.' representing empty space and '#' denoting obstructions
# when visiting a location, going to denote that with 'X'

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0
map = []
starting_position = None
with open("day6/input.txt", 'r') as file:
    # read in input, and create map
    for x, line in enumerate(file):
        newChars = []
        for y, char in enumerate(line.strip()):
            # when starting position is found, record and replace as visited.
            if char == '^':
                starting_position = (x, y)
                char = 'X'
            newChars.append(char)

        map.append(newChars)

    for line in map:
        print(line)

off_map = False
x = starting_position[0]
y = starting_position[1]
dist_pos = 1
while not off_map:
    # check next position
    next_x = x + directions[curr_dir][0]
    next_y = y + directions[curr_dir][1]
    if (next_x < 0 or next_x >= len(map)) or (next_y < 0 or next_y >= len(map[0])):
        off_map = True
    elif map[next_x][next_y] == '.':
        # move to spot, mark as visited.
        x = next_x
        y = next_y
        map[x][y] = "X"
        dist_pos += 1
    elif map[next_x][next_y] == 'X':
        # already visited, keep going
        x = next_x
        y = next_y
    else: 
        # found barrier, turning
        curr_dir = (curr_dir + 1) % 4

for line in map:
        print(line)
print(dist_pos)