#Input
digits = [1,2,3]

#Logic
def main(digits):
    digits_ = ""
    for d in digits: digits_+=str(d)
    return list(map(int,list(str(int(digits_)+1))))

#Output
print(main(digits))
