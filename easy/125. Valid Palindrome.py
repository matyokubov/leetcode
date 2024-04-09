#Input
s = "A man, a plan, a canal: Panama"

#Logic
def main(s):
    def c(s):
        r = ''
        for i in s.lower(): r+=i if i.isalnum() else ''
        return r
    s = c(s)
    return s == s[::-1]
    
#Output
print(main(s))
