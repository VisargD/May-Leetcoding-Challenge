# To solve this, I initialized the minimum and maximum to first element.
# Then I looped through the remaining elements of the list.
# On every step, calculate maximum sum sequence and find the maximum total. 
# The main idea behind this code is to find and subtract the minimum sum sequence from the total sum.

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        # Store the first element as maximum.
        maximum = A[0]
        maximum_total = A[0]
        
        # Store first element as minimum.
        minimum  = A[0]
        minimum_total = A[0]
        
        # Loop through list.
        for i in range(1, len(A)):
            
            # Check the max between current element and (max + current element) and store it.
            maximum = max(A[i], maximum + A[i])

            # Check the max between max and max_total
            maximum_total = max(maximum, maximum_total)
            
            # Check the min between current element and (min + current element) and store it.
            minimum = min(A[i], minimum + A[i])

            # Check the min between min and min_total
            minimum_total = min(minimum, minimum_total)
            
        # Check if the minimum total is equal to sum of list. This means that all the numbers are negative.
        # If yes, then return the maximum number from the list. (It will be available in max_total)
        if minimum_total == sum(A):
            return maximum_total

        # Else return the maximum from max_total or sum - min_total.
        else:
            return max(maximum_total, sum(A) - minimum_total)
            