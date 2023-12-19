# open and split data by line
with open("input.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
    label = 1
    for i in range(len(data)):
        new = []
        # label all galaxies
        for j in range(len(data[i])):
            item = data[i][j]
            if item == '#':
                new.append(label)
                label += 1
            else:
                new.append(item)
        data[i] = new


def no_galaxy_row(row):
    # check if a row contains galxies
    for elem in row:
        if type(elem) == int:
            return False
    return True


def no_galaxy_col(col):
    # check if a column contains galaxies
    for i in range(len(data)):
        if type(data[i][col]) == int:
            return False
    return True


def row_adjust(data=data):
    count = 0
    empty = [['.' for _ in range(len(data[0]))]]
    while count < len(data):
        # check each row
        if no_galaxy_row(data[count]):
            # if row is empty we insert an extra empty row before it
            data = data[:count] + empty[:] + data[count:]
            count += 2
        else:
            count += 1
    # return altered data
    return data


def col_adjust():
    count = 0
    while count < len(data[0]):
        # check each column
        if no_galaxy_col(count):
            for i in range(len(data)):
                # if column is empty we insert an extra empty column before it
                data[i] = data[i][:count] + ['.'] + data[i][count:]
            count += 2
        else:
            count += 1

# adjust data
data = row_adjust()
col_adjust()


def shortest_path(gala1, gala2):
    # find distance between 2 galaxies
    x_coord = abs(gala1[0]-gala2[0])
    y_coord = abs(gala1[1]-gala2[1])
    return x_coord+y_coord


def get_locations():
    ans = []
    # get all locations of galaxies
    for i in range(len(data)):
        for j in range(len(data[0])):
            if type(data[i][j]) is int:
                ans.append((i,j))
    return ans

# get positions
positions = get_locations()


def total_distance():
    total = 0
    # sum distances between all pairs of galaxies
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            total += shortest_path(positions[i], positions[j])
    print(total)
total_distance()


