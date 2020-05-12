# I used binary search for this problem. There is a pattern that every even index should have first occurence of a number.
# And the odd index should have the second occurence of a number.
# So every time the mid index is even, then mid + 1 index should have the same element. Otherwise the single element is in left half.
# And everytime the mid index is odd, then mid - 1 index should have the same element. Otherwise the single element is in right half.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # Initializing low and high for binary search.
        low = 0
        high = len(nums) - 1

        # Starting the while loop.
        while low <= high:
            
            # Calculating mid everytime.
            mid = (low + high) // 2
            
            # If the mid index element count is 1 then it is the single element. Return that element.
            if nums.count(nums[mid]) == 1:
                return nums[mid]
            
            # Check if the mid is even.
            if mid % 2 == 0:
                
                # If it is even and mid + 1 is "not equal" to the mid element then single element is in left half. 
                if nums[mid] != nums[mid + 1]:
                    high = mid - 1 

                # Else Single element is in the right half.                    
                else : 
                    low = mid + 1
                    
            # Check if the mid is odd.        
            elif mid % 2 != 0:

                # If it is odd and mid - 1 is "not equal" to the mid element then single elemtent is in the left half.
                if nums[mid] != nums[mid - 1]:
                    high = mid - 1
                    
                # Else the single element is in the right half.
                else:
                    low = mid + 1
                    