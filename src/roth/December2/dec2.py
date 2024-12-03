# get lists from txt
text = open("src/roth/December2/input.txt", "r")
lines = text.readlines()

reports = []

for reportstr in lines:
    report = reportstr[:-1].split(" ")
    reports.append(report)

safe_num = 0

for report in reports:
    increacing = None
    past_num = None
    good = True
    print("##########\n", report)
    # checks if good
    for num in report:
        num = int(num)
        print(past_num, num)
        if past_num != None and num - past_num >= 1:
            if num - past_num <= 3:
                if increacing == None:
                    print("started increacing")
                    increacing = True
                if increacing == False:
                    print("increaced but past was decreacing")
                    good = False
            if num - past_num > 3:
                print("incraced too much")
                good = False
        if past_num != None and num - past_num <= -1:
            if num - past_num >= -3:
                if increacing == None:
                    print("started decreaced")
                    increacing = False
                if increacing == True:
                    print("decreaced when past was increacing")
                    good = False
            if num - past_num < -3:
                good = False
                print("decreaced too much")
        if past_num != None and past_num == num:
            good = False
            print("same")
        past_num = num
    if good == True:
        safe_num += 1
    # if bad, see if dampener works
    else:
        dampened_good = False
        for location, removed_num in enumerate(report):
            dampened_report = report[:location] + report[location+1:]
            specific_dampened_good = True
            damp_past_num = None
            increacing = None  # Reset increacing for dampened report
            for num in dampened_report:
                num = int(num)
                print(damp_past_num, num)
                if damp_past_num != None and num - damp_past_num >= 1:
                    if num - damp_past_num <= 3:
                        if increacing == None:
                            print("started damp_increacing")
                            increacing = True
                        elif increacing == False:
                            print("increaced but past was decreacing")
                            specific_dampened_good = False
                            break
                    if num - damp_past_num > 3:
                        print("incraced too much")
                        specific_dampened_good = False
                        break
                elif damp_past_num != None and num - damp_past_num <= -1:
                    if num - damp_past_num >= -3:
                        if increacing == None:
                            print("started decreaced")
                            increacing = False
                        elif increacing == True:
                            print("decreaced when past was damp_increacing")
                            specific_dampened_good = False
                            break
                    if num - damp_past_num < -3:
                        specific_dampened_good = False
                        break
                if damp_past_num != None and damp_past_num == num:
                    specific_dampened_good = False
                    break
                damp_past_num = num
            if specific_dampened_good:
                dampened_good = True
                break  # Exit the loop once a dampened good report is found
        if dampened_good:
            safe_num += 1

print("TOTAL SAFE NUMBER:", safe_num)
