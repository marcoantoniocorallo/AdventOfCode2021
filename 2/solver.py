from functools import reduce

def fst(list):
    h = sum( [ int(x[1]) if x[0]=="forward" else 0 for x in list ]  )
    v = sum( [ int(x[1]) if x[0]=="down" else -int(x[1]) for x in list if x[0]!="forward" ] )
    return h*v

def snd(list):
    h,v,_=reduce(f,list,[0,0,0])
    return (h*v)

def f(tot,command):
    tot[0] += int(command[1]) if command[0]=="forward" else 0
    tot[1] += int(command[1])*tot[2] if command[0]=="forward" else 0
    tot[2] += int(command[1]) if command[0]=="down" else -int(command[1]) if command[0]=="up" else 0
    return tot

def main():
    with open("input.txt", "r") as f:
        l = [x.split(" ") for x in f.readlines()]
    print( fst(l) )
    print( snd(l) )
    
if __name__=='__main__':
    main()