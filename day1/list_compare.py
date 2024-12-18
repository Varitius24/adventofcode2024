import numpy as np
import bisect 
# def day1(a,b):
#     a = np.sort(np.array(a))
#     b = np.sort(np.array(b))
#     return np.sum(abs(a-b))
    
def part1(text):
    list1 = []
    list2 = []
    with open(text) as f:
        for line in f:
            line = line.strip()
            a,b = line.split(sep = "   ") 
            a = int(a)
            b = int(b)
            bisect.insort_left(list1, a) 
            bisect.insort_left(list2, b)
    print(len(list1) == len(list2))
    a = np.array(list1)
    b = np.array(list2)
    return list1,list2,np.sum(abs(a-b))
    # return [abs(a-b) for a,b in zip(list1,list2)]

def part2(a,b):
    counter = {elt:0 for elt in a}
    for elt in b:
        if counter.get(elt,None) != None:
            counter[elt] += 1
    product = [a* counter[a] for a in counter]
    print(sum(product))



a,b,c = part1("input.txt")
part1(a,b)
