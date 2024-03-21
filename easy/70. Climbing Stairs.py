#Input
n = 6

#Logic
def main(n):
    def factr(x):
        res = 1
        for i in range(1, x+1):
          res*=i
        return res
    c = lambda l,i: factr(l)/(factr(i)*factr(l-i))
    res,i = 1,1
    it = list(range(1,n))[::-1]
    print(it)
    for l in it:
        res+=c(l, i)
        i+=1
    return int(res)
    
#Output
print(main(n))
