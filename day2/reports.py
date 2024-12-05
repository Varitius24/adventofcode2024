def check_reports(report):
    ascending = None
    for count in range(len(report)-1):
        current = report[count]
        new = report[count+1]
        if ascending == None:
            if current > new :
                ascending = False
            elif current < new:
                ascending = True
        elif ascending:
            if current > new :
                return False
        else:
            if current < new :
                return False
        difference = abs(current-new)
        if difference < 1 or difference > 3:
            return False
    return True

 #  attempt without brute force
# def check_reports_damper(report):
#     ordered, damper = check_order(report)
#     print(ordered, report,damper)
#     if orderged ==False:
#         return False 
#     for count in range(len(report)-1):
#         current = report[count]
#         new = report[count+1]
#         difference = abs(current-new)
#         if difference < 1 or difference > 3:
#             if damper:
#                 if count+2 == len(report):
#                     return True
#                 difference = abs(report[count]-report[count+2])
#                 if difference < 1 or difference > 3:
#                     return False
#                 damper = False
#     return True
       
# def check_order(report):
#     ascending = sorted(report,reverse=False)
#     could_still_ascend = True
#     is_ascending = True
#     descending = sorted(report)
#     could_still_descend = True
#     is_descending = True

#     for count in range(len(report)-1):
#         curr,nxt = report[count], report[count+1] 

#         if curr>nxt:
#             # if report ==[78, 75, 74, 73, 71, 70, 68]:
#             #     print(could_still_descend)
#             if not could_still_ascend:
#                 is_ascending = False
#             could_still_ascend = False
#         if curr<nxt:
#             if not could_still_descend:
#                 is_descending = False
#             could_still_descend = False
#         if not(is_ascending or is_descending):
#             return False, False

    # if report ==[78, 75, 74, 73, 71, 70, 68]:
    #     print(is_ascending,is_descending,could_still_ascend,could_still_descend)

    # if is_ascending:
    #     if not is_descending:
    #         return True, could_still_ascend
    #     else:
    #         if could_still_ascend and not could_still_descend:
    #             return True, could_still_ascend
    # if is_descending:
    #     if not is_ascending:
    #         return True, could_still_descend
    #     else: 
    #         if could_still_ascend and not could_still_descend:
    #             return True, could_still_ascend
    # elif is_descending and is_ascending:
    #     return True, (could_still_ascend and could_still_descend)
    # return False, (could_still_ascend and could_still_descend)
        
            ######################################################   


def part1(file):
    with open(file) as f:
        count = 0
        for line in f:
            report = [int(elt) for elt in line.split(" ")]
            if check_reports(report):
                count +=1
                if [1, 1, 2, 3, 4] == report:
                    print("AAAA")
    print(count)


# brute force approach
def part2(file):
    with open(file) as f:
        counter = 0
        for line in f:
            report = [int(elt) for elt in line.split(" ")]
            if check_reports(report):
                counter +=1
    
            else:
                for count in range(0, len(report)):
                    new_list = report.copy()
                    del new_list[count]
                    if check_reports(new_list):
                        counter += 1
                        break

    print(counter)


# check_reports_damper([1,2, 6, 5, 7])
part2("input.txt") 