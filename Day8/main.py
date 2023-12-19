with open("input.txt") as f:
    # get the data and split it by row
    data = f.read().strip()
    data = data.split("\n")
# instructions on where to turn
instructs = data[0]
# the mappings
data = data[2:]
map = {}
for line in data:
    info = line.split()
    # split data into souce and destinations
    source = info[0]
    dest = [info[2][1:-1], info[3][:-1]]
    map[source] = dest
# initialize start and number of steps
steps = 0
cur = 'AAA'
pointer = 0
# set map for L/R distinction
directions = {'L': 0, 'R': 1}
while cur != 'ZZZ': # we stop when we get ZZZ
    # get the direction
    direction = instructs[pointer]
    direction = directions[direction]
    # get the next position
    cur = map[cur][direction]
    # increment steps taken and current instruction to follow
    steps += 1
    pointer += 1
    # keep instruction within bounds
    pointer = pointer % len(instructs)
print(steps)
# for dat in data:
#     print(dat)