def lookForRows(boards):
    index = boards.index([-1,-1,-1,-1,-1])
    return index-index%5

def lookForColumns(boards):
    for row in range(0,len(boards)-1,5):
        for j in range(0,len(boards[row])):
            if [boards[row+k][j] for k in range(0,5)] == [-1,-1,-1,-1,-1]:
                return row

def fst(num,boards):
    for i in range(5,len(num)):
        boards = [ [ -1 if k in num[:i] else k for k in x ] for x in boards ]
        try:
            start = lookForRows(boards)
            boards_tmp = [ [ x for x in l if x!=-1 ] for l in boards[start : start + 5] ]
            return sum( [ sum(l) for l in boards_tmp ] )*num[i-1]
        except ValueError as v:
            pass
        start = lookForColumns(boards)
        if start is not None:
            boards_tmp = [ [ x for x in l if x!=-1 ] for l in boards[start : start + 5] ]
            return sum( [ sum(l) for l in boards_tmp ] )*num[i-1]

def snd(num, boards):
    for i in range(5,len(num)):
        boards = [ [ -1 if k in num[:i] else k for k in x ] for x in boards ]
        w1=w2=True
        while w1 or w2: # For each winning board -> remove board
            try:
                start = lookForRows(boards)
                if len(boards)==5: # if is the last board -> return res
                    boards_tmp = [ [ x for x in l if x!=-1 ] for l in boards ]
                    return sum( [ sum(l) for l in boards_tmp ] )*num[i-1]
                boards[start : start + 5] = []
            except ValueError as v:
                w1 = False
            start = lookForColumns(boards)
            if start is not None:
                if len(boards)==5: # if is the last board -> return res
                    boards_tmp = [ [ x for x in l if x!=-1 ] for l in boards ]
                    return sum( [ sum(l) for l in boards_tmp ] )*num[i-1]
                boards[start : start + 5] = []
            else:
                w2 = False

def main():
    with open("input.txt", "r") as f:
        numbers = [ int(n) for n in f.readline().split(',') ]
        boards = [ [int(num) for num in line.split()] for line in f.readlines() if line != "\n"]
    print( fst(numbers,boards) )
    print( snd(numbers,boards) )

if __name__=="__main__":
    main()