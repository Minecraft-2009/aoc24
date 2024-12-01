##########   PART I   ##########

# Get distance between inputs

# get lists from txt
text = open("src/roth/December1/input.txt", "r")
lines = text.readlines()

group1str = []#left
group2str = []#right

# separate columns
for line_num in range(0, 1000):
    that_line = lines[line_num]
    group1str.append(that_line[:5])
    group2str.append(that_line[8:13])
# print(group1str)
# print(group2str)

# make it integers, not strings 
group1int = []
group2int = []

for num in group1str:
    group1int.append(int(num))
for num in group2str:
    group2int.append(int(num))
# print(group1int)
# print(group2int)

# sort numerically lowest to highest
group1int.sort()
group2int.sort()
# print("1",group1int)
# print("2",group2int)
# print(len(group1int))
# print(len(group2int))

# get difference between each int
differences = []
for num in range(0, 1000):
    differences.append(abs(group1int[num]-group2int[num]))
# print(differences)

# add up differences
total_difference = sum(differences)
# print(total_difference) = 2344935



##########   PART II   ##########

similarity = 0#to begin with

for left_num in group1int:
    # print(left_num, ":", (left_num * group2int.count(left_num)))
    similarity += (left_num * group2int.count(left_num))
# print(similarity) = 27647262