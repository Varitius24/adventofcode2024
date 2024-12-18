import re
def order(file):
    instructions = []
    prod = []
    instruct = True
    with open(file) as f:
        for line in f:
            line = line.strip()
            if re.match(r'^\s*$', line):
                instruct = False
            elif instruct:
                line = line.split("|")
                instructions.append(line)
            else:
                line = line.split(",")
                prod.append(line)
    correct = []
    count = 0
    for line in prod:
        if check_stack(line,instructions[:]):
            correct.append(line)
            mid_index = len(line) // 2
            count += int(line[mid_index])
    print(count)

            

def check_stack(line, instructions):
    # for page in line:
    #     for instruct in instructions:
    #         if instruct != []:
    #             if page == instruct[0]:
    #                 del instruct[0]
    # for elt in instructions:
    #     if elt != []:
    #         return False
    # return True
            
            
    

order("input.txt")