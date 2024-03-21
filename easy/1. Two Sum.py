# Input
nums = [2, 3, 3, 4]
target = 6

# Logic (brick-push method)
def main(nums,target):
    l = len(nums)
    for ix1 in range(l-1):
        for ix2 in range(ix1+1,l):
            if nums[ix1]+nums[ix2]==target: return [ix1,ix2]

# Output
print(main(nums,target))
