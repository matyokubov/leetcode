#Input
nums = [4,1,2,1,2]

#Logic
def main(nums):
    num = 0
    for x in nums: num^=x
    return num
    # return 2 * sum(set(nums)) - sum(nums)
    
#Output
print(main(nums))
