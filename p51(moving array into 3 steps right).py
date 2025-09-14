Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]



class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        for j in range(1,k+1):
            temp=nums[n-1]
            for i in range(n-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=temp
        return nums

        
