# get lists from txt
text = open("src/roth/December3/input.txt", "r").read().rstrip()

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
print(mul_locations)
# n = 554 # test
# print(text[mul_locations[n]:mul_locations[n]+4])
# weed out unfinished parenthesis