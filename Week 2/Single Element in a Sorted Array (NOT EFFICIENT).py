# At first I solved this problem using this code.
# It got accepted but was not an efficient solution as the runtime for this solution is 6592 ms.
# I came up with a binary search approach. It is more efficient. The runtime for binary approach is 76 ms. 

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        for x in nums:
            
            if nums.count(x) == 1:
                
                return x
            
