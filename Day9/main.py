# open and split data by line
with open("input.txt") as f:
    data = f.read().strip()
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split()

# function to find next_num in given sequence
def next_val(nums):
    diff = []
    non_zero = False
    for i in range(len(nums)-1):
        cur = int(nums[i+1])-int(nums[i])
        if cur:
            non_zero = True
        diff.append(cur)
    if non_zero:
        return int(nums[-1])+next_val(diff)
    return nums[-1]

total = 0
# sum all next nums
for line in data:
   total += next_val(line)

print(total)


