import re

def parser(file):
    with open(file) as f:
        txt = f.read()
    count = 0
    print(txt)
    x = re.findall(r'mul\(\d+,\d+\)', txt)
    for operation in x:
        print(operation)
        a,b = re.findall(r'\d+', operation)
        count += int(a)*int(b)
    print(count)



parser("input.txt")