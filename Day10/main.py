
# open and split data by line
with open("input.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
seen = {}


def first_stepper(row, col):
    # finds the 2 connected pipes to S
    left = data[row][col-1]
    right = data[row][col+1]
    up = data[row-1][col]
    down = data[row+1][col]
    ans = []
    # adds the pipe locations that form valid connections
    # to answer
    if up == '|':
        ans.append([row-1,col])
    if down == '|':
        ans.append([row+1,col])
    if right == '-' or right == 'J' or right == '7':
        ans.append([row,col+1])
    if left == '-' or left == 'F' or left == 'L':
        ans.append([row,col-1])
    return ans


def findS(info):
    # scans data for position of S and returns it
    for i in range(len(info)):
        for j in range(len(info[0])):
            if info[i][j] == 'S':
                return [i,j]


def get_next_pos(lastrow, lastcol, row, col,):
    # gets the next valid position given current
    # and most recent past location
    cur = data[row][col]
    if cur == '|':
        # if last was above or below current
        if lastrow > row:
            return [row-1,col]
        else:
            return [row+1, col]
    if cur == '-':
        # if last was to the left or right of current
        if lastcol > col:
            return [row,col-1]
        else:
            return [row, col+1]
    if cur == 'L':
        # read the descriptions in the question mate
        if lastcol > col:
            return [row-1,col]
        else:
            return [row, col+1]
    if cur == 'J':
        if lastcol < col:
            return [row-1,col]
        else:
            return [row, col-1]
    if cur == '7':
        if lastcol < col:
            return [row+1,col]
        else:
            return [row, col-1]
    if cur == 'F':
        if lastcol > col:
            return [row+1,col]
        else:
            return [row, col+1]


def fill_path(lastrow, lastcol, row, col):
    # given starting point, go around circular path
    # and fill distances
    count = 1
    curx = row
    cury = col
    cur = data[curx][cury]
    lastx = lastrow
    lasty = lastcol
    while cur != 'S': # keep going until you get back to start
        if (curx, cury) in seen:
            # keep the smallest of the distances if encountered
            # on another round along the path
            seen[(curx, cury)] = min(seen[(curx, cury)], count)
        else:
            seen[(curx, cury)] = count
        # get the next position and update variables
        cur = get_next_pos(lastx, lasty, curx, cury)
        lastx = curx
        lasty = cury
        curx = cur[0]
        cury = cur[1]
        count += 1
        cur = data[curx][cury]


def fill_both_paths(row, col):
    # check for valid start pos
    if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
        return
    # get surrounding spots
    next_step = first_stepper(row, col)
    next1 = next_step[0]
    # fill the paths
    fill_path(row, col, next1[0], next1[1])
    next2 = next_step[1]
    fill_path(row, col, next2[0], next2[1])
    # get the largest distance among them all
    max_dist = -1
    for point in seen:
        max_dist = max(max_dist, seen[point])
    print(max_dist) # print max distance
    return


initial = findS(data)
fill_both_paths(initial[0], initial[1])
