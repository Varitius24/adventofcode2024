import numpy as np

def crossword(file):
    word = list("XMAS")
    contents = []
    counter = 0
    with open(file) as f:
        for line in f:
            contents.append(np.array(list(line.strip())))
    contents = np.array(contents)
    
    pos = np.where(contents[:,]=="X")
    pos = list(zip(pos[0], pos[1]))
    rows, cols = contents.shape
    for x,y in pos:
        right = contents[x, y:y+len(word)]
        right = np.array([right if right.shape[0] == 4 else np.array(list("XXXX"))])[0]
        counter += (word == right).sum()

        left = contents[x, y-len(word):y]
        left = np.array([left if left.shape[0] == 4 else np.array(list("XXXX"))])[0]
        counter += (word == left).sum()

        up = contents[x - len(word):x, y]
        up = np.array([up if up.shape[0] == 4 else np.array(list("XXXX"))])[0]
        counter += (word == up).sum()

        down = contents[x:x+len(word), y]
        down = np.array([down if down.shape[0] == 4 else np.array(list("XXXX"))])[0]
        counter += (word == down).sum()

        print(counter)
        # right_up =
        # right_down =
        # left_up = 
        # left_down = 

crossword("input.txt")