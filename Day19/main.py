import re


def get_conditions(info):
    # split data by comma to get separate conditions
    info = info.split(',')
    conditions = []
    for i in range(len(info)-1):
        # for each condition, append
        # the attibute, comparator, rating, and result
        cond = info[i]
        res = []
        res.append(cond[0]) # attribute
        res.append(cond[1]) # comparator
        res.append(int(re.findall("\d+", cond)[0])) # rating
        cond = cond.split(':')
        res.append(cond[-1]) # result
        conditions.append(res[:])
    conditions.append(info[-1][:-1]) # if all else fails option
    return conditions


# split data
with open("input.txt") as f:
    data = f.read().strip()
    data = data.split("\n")


def clean_data(my_data):
    # parse data and split into usable chunks
    workflows = {}
    parts = []
    for i in range(len(my_data)):
        # split data into workstation and requirements
        my_data[i] = my_data[i].split('{')
        if my_data[i][0]:
            # if its a workstation we split map the station
            # to the requiremnts
            process = get_conditions(my_data[i][1])
            workflows[my_data[i][0]] = process
        else:
            # if its a part we clean it up into integers
            if len(my_data[i]) < 2:
                continue
            parts.append(my_data[i][1].split(','))
            for j in range(len(parts[-1])):
                parts[-1][j] = int(re.findall("\d+", parts[-1][j])[0])

    return workflows, parts


stations, products = clean_data(data)


def check(ratings, station):
    # depending on the station we end our search or continue it
    if station == 'R':
        return False
    if station == 'A':
        return True
    return accept(ratings, station)


# give the corresponding index of the attribute
types = {'x':0,'m':1,'a':2,'s':3}


def accept(ratings, station='in'):
    conds = stations[station]
    # get our conditions
    for cond in conds:
        # check if it's the else portion
        if type(cond) is str:
            return check(ratings, cond)
        rating = ratings[types[cond[0]]]
        # get the rating of the condition
        if cond[1] == '>':
            # do the comparison based on the comparison sign
            if rating > cond[2]:
                return check(ratings, cond[3])
            else:
                continue
        else:
            if rating < cond[2]:
                return check(ratings, cond[3])
            else:
                continue
total = 0
for product in products:
    # cycle through all products and add
    # ratings of accepted products
    if accept(product):
        total += sum(product)
print(total)