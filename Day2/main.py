import re
# 12 red cubes, 13 green cubes, and 14 blue cubes p1
with open("input.txt") as f:
    data = f.read().strip()
color_count = {'red':12, 'green':13, 'blue':14}
def check_lines(line):
    # divide line into day/data
    day_data = line.split(":")
    # get the data
    guesses = day_data[1]
    # split the data into each particular guess
    guesses = guesses.split(";")
    possible = True
    # walk through each guess
    for guess in guesses:
        # split each guess into the color
        guess = guess.split(',')
        # work on each guess
        for entry in guess:
            # get the count for the color
            count = (re.findall("\d+", entry))
            # convert it to int
            count = int(count[0])
            i = 0
            color = ''
            # find which color the count is for
            while i < len(entry):
                if entry[i] == 'r':
                    color = "red"
                elif entry[i] == 'g':
                    color = 'green'
                elif entry[i] == 'b':
                    color = 'blue'
                if color:
                    # if we found a color, see if we get a match
                    i = len(entry)
                    if count > color_count[color]:
                        print(color, color_count[color])
                        # flag, not possible
                        possible = False
                        return [possible, int(day_data[0].split()[1])]
                i += 1
    return[possible, int(day_data[0].split()[1])]

def clean_up(data):
    lines = data.split("\n")
    total = 0
    for line in lines:
        day = check_lines(line)
        if day[0]:
            total += day[1]
    return total

print(clean_up(data))


