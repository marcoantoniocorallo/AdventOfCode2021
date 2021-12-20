def fst(fishes,n): # Inefficient !!!
    for i in range(n):
        zeros = len(list(filter(lambda x : x==0,fishes)))
        fishes = [ (x-1 if x>0 else 6) for x in fishes ]
        fishes.extend([8]*zeros)
    return len(fishes)

def snd(fishes,n):
    nFishes = [ fishes.count(x) for x in range(0,9) ]
    for i in range(n):
        zeros = nFishes[0]
        nFishes = [ nFishes[(j+1)%9] for j in range(0,9) ]
        nFishes[6] += zeros
    return sum(nFishes)

def main():
    with open("input.txt", "r") as f:
        fishes = [ int(x) for x in f.readline().split(',') ]
    print(snd(fishes,80))
    print(snd(fishes,256))

if __name__=="__main__":
    main()