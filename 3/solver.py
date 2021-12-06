def fst(l):
    mcb = [ sum(int(seq[i]) for seq in l) for i in range(0, len(l[0])) ]
    mcb = [ '1' if mcb[i] > len(l)/2 else '0' for i in range(0, len(mcb)) ]
    mcb = int(''.join(mcb),2)
    ones = int('1'*len(l[0]),2)
    lcb = mcb^ones
    return (mcb*lcb)

def snd(l):
    mcb = f(l.copy(),True)
    lcb = f(l,False)
    return mcb*lcb

def f(l,truth):
    nLines = len(l)/2
    i=0
    while len(l)>1:
        l=list(filter(lambda x : (
            truth if (x[i]=='1' and sum(int(seq[i]) for seq in l) >= nLines) 
                 or (x[i]=='0' and sum(int(seq[i]) for seq in l) < nLines) 
            else not(truth)), l))
        i+=1
        nLines = len(l)/2
    return int(l[0],2)

def main():
    with open("input.txt", "r") as f:
        l = f.read().split('\n')
    print( fst(l) )
    print( snd(l) )

if __name__=="__main__":
    main()