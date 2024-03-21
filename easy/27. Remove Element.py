#Input
nums, val = [0,1,2,2,3,0,4,2], 2

#Logic
def main(nums, val):
    nums[:] = list(filter(lambda i: i!=val, nums))
    return len(nums)
    
#Output
print(main(nums, val))
