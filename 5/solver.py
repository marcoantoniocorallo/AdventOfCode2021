from numpy import zeros

def fst(lines,M):
    for line in lines:
        x1,y1,x2,y2=line[0][0],line[0][1],line[1][0],line[1][1]
        x1,x2=min(x1,x2),max(x1,x2)
        y1,y2=min(y1,y2),max(y1,y2)
        if x1==x2 or y1==y2:
            M[y1:y2+1,x1:x2+1]+=1
    return sum([ sum(x) for x in [ [ 1 for x in row if x > 1] for row in M ] ])

def snd(lines,M):
    for line in lines:
        x1,y1,x2,y2=line[0][0],line[0][1],line[1][0],line[1][1]
        if x1==x2 or y1==y2:
            x1,x2=min(x1,x2),max(x1,x2)
            y1,y2=min(y1,y2),max(y1,y2)
            M[y1:y2+1,x1:x2+1]+=1
        else:
            j = x1
            n = 1 if y2>y1 else -1
            for i in range(y1, y2+n, n):
                M[i][j]+=1
                j += 1 if x2>x1 else -1
    return sum([ sum(x) for x in [ [ 1 for x in row if x > 1] for row in M ] ])

def main():
    with open("input.txt", "r") as f:
        coordinates = [ [ [ int(p) for p in points.split(',') ] for points in line.strip('\n').split(' -> ') ] for line in f.readlines()]
    maxY = max([line[0][0] for line in coordinates]+[line[1][0] for line in coordinates])
    maxX = max([line[0][1] for line in coordinates]+[line[1][1] for line in coordinates])
    print(fst(coordinates, zeros((maxX+1,maxY+1))))
    print(snd(coordinates, zeros((maxX+1,maxY+1))))

if __name__=="__main__":
    main()