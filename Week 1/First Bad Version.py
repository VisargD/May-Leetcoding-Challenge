# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# I have solved this problem using iterative Binary Search.
# Here low <= high is used to consider the case when n = 1.

class Solution:
    def firstBadVersion(self, n):
        
        low = 1
        high = n

        # low <= high to consider the case when n = 1.
        while low <= high:

            # Calculating the mid value
            mid = (low + high) // 2

            # If middle version number is faulty then check if the mid - 1 is fault.
            if isBadVersion(mid) == True:

                # If mid - 1 is not faulty then mid should be the faulty one.
                if isBadVersion(mid - 1) == False:
                    return mid

                # Else mid - 1 is faulty, then continue the search in the lower half
                else:
                    high = mid - 1

            # If middle version is not faulty then try looking in the upper half.
            else:
                low = mid + 1
                

# I first used a simple for loop to use linear search. But it was not an efficient solution.