def fst(l):
    return len(
        [i for i in zip(l,l[1:]) if i[0]<i[1]]
    )

def snd(l):
    new_l = [sum(i) for i in zip(l,l[1:],l[2:])]
    return len(
            [k for k in zip(new_l,new_l[1:]) if k[0]<k[1]]
        )

def main():
    with open("input.txt", "r") as f:
        l = [int(x) for x in f.readlines()]
    print( fst(l) )
    print( snd(l) )

if __name__=='__main__':
    main()