# open and split data by line
with open("day5.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
# get seed data from first line
seeds = data[0].split()[1:]
for i in range(len(seeds)):
    # convert all seed numbers to int
    seeds[i] = int(seeds[i])
# get rest of data
data = data[2:]
# create map that matches an array of
# matching info for each stage
main_map = {0:[],
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[]}

def count(rows):
    ans = []
    cur = []
    # go through the data and put all
    # related lines into a single array
    # then add that array to a final answer array
    # that has the data split by stage
    for line in rows:
        if not line:
            ans.append(cur)
            cur = []
        elif line[0].isalpha():
             cur = []
        else:
            cur.append(line)
    ans.append(cur)
    return ans
# get the data split into sections
all_maps = count(data)
# assigns each section to its respective place in the process
def assign():
    for i in range(len(main_map)):
        main_map[i] += all_maps[i]
        for j in range(len(main_map[i])):
            main_map[i][j] = main_map[i][j].split()
assign()

# given an array with (dest-start, source-start, range) info
# and a source we find the matching destination and return it
def get_dest(start, maps):
    # goes through all the given mappings
    # in that stage until solution is found
    for mapping in maps:
        origin = int(mapping[1])
        end = origin + int(mapping[2])
        if origin <= start <= end:
            dest = int(mapping[0]) + start-origin
            return dest
    # if no match found then source is destination
    return start

ans = []
for seed in seeds:
    cur = seed
    # for all seeds find the matching location
    for place in range(len(main_map)):
        cur = get_dest(cur, main_map[place])
    ans.append(cur)
# print lowest matching location
print(min(ans))
