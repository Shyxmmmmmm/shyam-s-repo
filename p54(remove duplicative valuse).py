Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.



class Solution:
    def removeDuplicates(self, arr):
        a=set()
        r=[]
        for i in arr:
            if i not in a:
                a.add(i)
                r.append(i)
        return r


ALTERNATIVE:

class Solution:
    def removeDuplicates(self, arr):
        a=sorted(set(arr))
        return a
        
                
