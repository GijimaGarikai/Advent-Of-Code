with open("day3.txt") as f:
    data = f.read().strip()
    lines = data.split("\n")
char_data = []
# symbol positions
sym_pos = set()
# added_num
seen = set()

for i in range(len(lines)):
    # go through each line
    line = lines[i]
    newline = []
    # go through each character on each line
    for j in range(len(line)):
        # split each line into characters
        newline.append(line[j])
        # if it's a symbol, add position to sym_pos
        if not(line[j].isnumeric()) and line[j] != '.':
            sym_pos.add((i,j))
    # append characterized line to dataset
    char_data.append(newline[:])

def build_num(row, col):
    # Given a position we know contains a number, build the rest of that number
    num = [char_data[row][col]]
    seen.add((row, col))
    ini_col = col
    col -= 1
    # build it leftside
    while col > -1 and char_data[row][col].isnumeric():
        num = [char_data[row][col]] + num
        seen.add((row, col))
        col -= 1
    # build it rightside
    col = ini_col+1
    while col < len(char_data[0]) and char_data[row][col].isnumeric():
        num = num + [char_data[row][col]]
        seen.add((row, col))
        col += 1

    return int("".join(num))
# find numbers at the given position
def find_num(row, col):
    # if seen, skip
    if (row, col) in seen:
        return 0
    # if out of bounds, skip
    if row >= len(char_data) or row < 0 or col < 0 or col >= len(char_data[0]):
        return 0
    if char_data[row][col].isnumeric():
        num = build_num(row, col)
        return num
    return 0
# finds a number from all 8 positions around symbol
def find_num_and_start(pos):
    row = pos[0]
    col = pos[1]
    nums = 0
    for j in range(col-1, col+2):
        nums += find_num(row-1, j)
    for j in range(col-1, col+2):
        if j == col:
            continue
        nums += find_num(row, j)
    for j in range(col-1, col+2):
        nums += find_num(row+1, j)

    return nums


ans = 0

for pos in sym_pos:
    ans += find_num_and_start(pos)
print(ans)
