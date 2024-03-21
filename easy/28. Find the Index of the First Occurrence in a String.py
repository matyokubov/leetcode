#Input
haystack = "mississippi"
needle = "issipi"

#Logic
def main(haystack, needle):
    if needle in haystack:
        r = haystack.index(needle)
    else: r = -1
    return r
        
#Output
print(main(haystack, needle))
