def fuelToK(crabs, k, f):
    return sum( [ f(abs(crab-k)) for crab in crabs ] )

def lookForK(crabs, f):
    return min([ fuelToK(crabs, i, f) for i in range(len(crabs)) ])

def fst(crabs):
    return lookForK(crabs, lambda x : x)

def snd(crabs):
    return lookForK(crabs, lambda k : sum( [ i for i in range(k+1) ] ) )

def main():
    with open("input.txt", "r") as f:
        crabs = [ int(x) for x in f.readline().split(',') ]
    print(fst(crabs))
    print(snd(crabs))

if __name__=="__main__":
    main()