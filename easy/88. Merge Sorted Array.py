#Input
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

#Logic
def main(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m]+nums2[:n])
    print(nums1) # Just to see the result
    
#Output
main(nums1, m, nums2, n)
