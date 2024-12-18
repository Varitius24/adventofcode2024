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

def parser2(file):
    with open(file) as f:
        txt = f.read()
    count = 0
    do = True
    x = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', txt)
    for operation in x:
        print(operation)
        if operation == "do()":
             do = True
        elif operation == "don't()":
            print(1212234)
            do = False
        elif do == True:
            a,b = re.findall(r'\d+', operation)
            count += int(a)*int(b)
    print(count)


parser2("input.txt")