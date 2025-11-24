ANAGRAM

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 


class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        
        a=[0]*256
        
        for i in s1:
            a[ord(i)]=a[ord(i)]+1
        
        for i in s2:
            a[ord(i)]=a[ord(i)]-1
        
        for i in a:
            if i!=0:
                return False
        return True
       
