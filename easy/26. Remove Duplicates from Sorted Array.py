#Input
nums = [0,0,1,1,1,2,2,3,3,4]

#Logic
def main(nums):
    nums[:] = sorted(set(nums))
    return len(nums)
    
#Output
print(main(nums))
