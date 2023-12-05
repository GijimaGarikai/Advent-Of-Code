import re
with open("input.txt") as f:
    data = f.read().strip()

def check_lines(line):
    # divide line into day/data
    day_data = line.split(":")
    # get the data
    guesses = day_data[1]
    # split the data into each particular guess
    guesses = guesses.split(";")
    # walk through each guess
    color_count = {'red': 1, 'green': 1, 'blue': 1}
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
                    color_count[color] = max(color_count[color], count)
                    i = len(entry)
                i += 1
    return color_count['red']*color_count['blue']*color_count['green']

def clean_up(data):
    lines = data.split("\n")
    total = 0
    for line in lines:
        total += check_lines(line)
    return total

print(clean_up(data))


