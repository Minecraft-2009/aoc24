# get lists from txt
text = open("src/roth/December3/input.txt", "r").read().rstrip()
# print(len(text))
# quit()
# scan for "mul("
# text = "23456mm7890madfcgf"
m_locations = []
start = 0
while True:
    start = text.find("m", start)
    if start == -1:
        break
    m_locations.append(start)
    start += 1
# print(m_locations)
mul_locations = []
for m in m_locations:
    if text[m:m+4] == "mul(":
        mul_locations.append(m)
# print(mul_locations)
# n = 554 # test
# print(text[mul_locations[n]:mul_locations[n]+4])
# weed out unfinished parenthesis
muls = []
for mul_location in mul_locations:
    for end in range(3, 13):
        if text[mul_location+end] == ")":
            muls.append([mul_location, mul_location+end+1])
            break
# print("muls",muls, "muls")
# for mul in muls:
    # print(text[mul[0]:mul[1]])
# print("----------")

# find locations of do's and don't's
d_locations = []
dstart = 0
done=False
while dstart <= len(text) and not done:
    do_start = text.find("do()", dstart)
    dont_start = text.find("don't()", dstart)
    print(dstart)
    if dstart == -1:
        break
    if do_start < dont_start: 
        d_locations.append([do_start, True])
        dstart = do_start +1
    else:
        d_locations.append([dont_start, False])
        dstart = dont_start +1
    if dstart==0:
        done=True
d_locations.pop()
# print(d_locations)
# quit()

# list of do runs 
dos = []
# donts = []
past_d = 0
for d in d_locations:
    if d[1]:
        dos.append([past_d, d[0]])
    # else:
    #     donts.append([past_d,d[0]])
    past_d = d[0]

print("dos\n", dos)
# print(donts)
# for index, nums in enumerate(muls):

quit()
# get the numbers themselves
good_nums = []
nums_to_mul = []
for mul in muls:
    nums = text[mul[0]:mul[1]][4:-1]
    # print(mul,nums)
    if "," not in nums:
        continue
    split_num = nums.split(",")
    if (not split_num[0].isnumeric()) or (not split_num[1].isnumeric()):
        continue
    for stretch in dos:
        ran = range(stretch[0], stretch[1])
        # if #FIX THIS IT IS UNFINISHED
    good_nums.append(split_num)

# puts the ones to multiply into list
for num in good_nums:
    nums_to_mul.append(num)
# print(nums_to_mul)

# specific purges bc time-pressed
# nums_to_mul.remove("504who(")
# nums_to_mul.remove("")

total = 0
for factors in nums_to_mul:
    total += int(factors[0])*int(factors[1])
print(total)