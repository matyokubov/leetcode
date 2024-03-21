#Input
a, b = "1010", "1011"

#Logic
def main(a,b):
    def bin2dec(x):
        res = 0
        for i,v in enumerate(x[::-1]): res+=int(v)*2**i
        return res
    return str(bin(bin2dec(a)+bin2dec(b)))[2:]

#Output
print(main(a,b))
