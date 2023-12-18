
with open("day6.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
    # splitting data into times and distances
    for i in range(len(data)):
        data[i] = data[i].split(":")
    for i in range(len(data)):
        data[i] = data[i][1]
        data[i] = data[i].split(" ")

def ways(time, distance):
    # finds number of ways we can charge and
    # still beat the record
    print(time, distance)
    options = 0
    for i in range(time+1):
        if (time-i)*i > distance:
            options += 1
    return options
total = 0
product = 1
i = 0
j = 0
while i < len(data[0]) and j < len(data[1]):
    time = None
    distance = None
    # find time
    while not data[0][i] and i < len(data[0]):
        i += 1
    time = int(data[0][i])
    i += 1
    # find distance
    while not data[1][j] and j < len(data[1]):
        j += 1
    distance = int(data[1][j])
    j += 1
    if time and distance:
        # get total and product
        amt = ways(time, distance)
        total += amt
        product *= amt
print(total, product)

