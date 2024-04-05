#Input
rowIndex = 5

#Logic
def main(rowIndex):
    res = [[1]]
    for _ in range(rowIndex): # identify how much it cycles
        temp = [0]+res[-1]+[0]
        row = []
        for j in range(len(res[-1])+1): # identify next row's length
            row.append(temp[j]+temp[j+1])
        res.append(row)
    return res[-1]
    
#Output
print(main(rowIndex))
