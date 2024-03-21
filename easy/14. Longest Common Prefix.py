#Input
strs = ["flower", "flow", "flight"]

def main(strs):
    string = ""
    newlist = sorted(strs)
    firstword = newlist[0]
    lastword = newlist[-1]
    for i in range (len(firstword)):
        if(firstword[i] == lastword[i]):
            string = string + firstword[i]
        else: break
    return string

#Output
print(main(strs))
