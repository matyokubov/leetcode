#Input
s = "   fly me   to   the moon  "

#Logic
def main(s):
    lastword = ""
    for i in list(range(len(s)))[::-1]:
        if s[i]!=' ':
            while s[i]!=' ':
                lastword+=s[i]
                if i==0: break
                i-=1
            return len(lastword)
    
#Output
print(main(s))
