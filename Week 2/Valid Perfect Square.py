class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Initializing low and high to implement binary search algorithm for the range 1 ... num .
        low = 1
        high = num
        
        # 1 is a perfect square.
        # Checking explicitly if the number is 1. And returning True.
        if num == 1:
            return True
        
        # Beginning the binary search.
        while low <= high:
            
            # Calculating mid 
            mid = (low + high) // 2
            
            # Checking if the square of mid is equal to number.
            # If yes, then num is a perfect square. So, return True.
            if mid ** 2 == num:
                return True

            # Else if the square of mid is less than num then check in the right half. Set low = mid + 1 for this.    
            elif mid ** 2  < num:
                low = mid + 1
                
            # Else if the square of mid is greater than num then check in the left half. Set high = mid - 1 for this.    
            else:
                high = mid - 1

        # If during the search no such element is found then return False        
        return False
                
        
