# open and split data by line
with open("day4.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
# split lines into card part and winning number part
for i in range(len(data)):
    line = data[i]
    line = line.split(":")
    line = line[1:]
    line = line[0].split("|")
    fin_line = []
    fin_line.append(line[0].split(" "))
    fin_line.append(line[1].split(" "))
    data[i] = fin_line[:]

total = 0
for card in data:
    cur = 0
    my_card = card[0]
    prize = card[1]
    winners = set()
    # create set of winning numbers
    for value in prize:
        if value.isnumeric():
            winners.add(value)
    # check if current number on card is a winning number
    for num in my_card:
        if num in winners:
            if cur:
                cur *= 2
            else:
                cur = 1
    total += cur
print(total)

