Example 1:

Input:
n = 5, k = 4
tree[] = {2, 3, 6, 2, 4}
Output: 3
Explanation: Wood collected by cutting trees
at height 3 = 0 + 0 + (6-3) + 0 + (4-3) = 4
hence 3 is to be subtracted from all numbers.
Since 2 is lesser than 3, nothing gets
subtracted from it.
Example 2:

Input:
n = 6, k = 8
tree[] = {1, 7, 6, 3, 4, 7}
Output: 4
Explanation: Wood collected by cutting trees
at height 4 = 0+(7-4)+(6-4)+0+0+(7-4) = 8



class Solution:
    def find_height(self,tree,n,k):
        i=0
        j=max(tree)
        
        while i<=j:
            mid=(i+j)//2
            wood=self.p(tree,mid)
            
            if wood==k:
                return mid
            elif wood>k:
                i=mid+1
            else:
                j=mid-1
        return -1
    def p(self,tree,mid):
        wood=0
        for i in range(0,len(tree)):
            if tree[i]>mid:
                wood=wood+(tree[i]-mid)
        return wood
