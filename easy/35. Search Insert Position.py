#Input
nums, target = [1,3,5,6], 3

#Logic
def main(nums, target):
    nums.append(None)
    for i, e in enumerate(nums):
        if target<=e: return i
        if nums[i+1]==None: return i+1

#Output
print(main(nums, target))
