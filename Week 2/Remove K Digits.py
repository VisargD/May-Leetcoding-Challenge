# The concept for number of high value is that higher place values should hold higher digit.
# So if we have to make a highest number from 1, 2, 3, 4, 5 (no repetition) then 5 (highest number) should be at highest place value.
# So, descending order gives highest number possible (54321).
# And ascending order gives the lowest number (12345).
# I used this to solve the problem by deleting k number that were not in ascending order.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # Checking condition if k = length of num. If yes then remove all digit and return 0
        if k == len(num):
            return "0"
        
        # Setting outer_count to zero. Every time we iterate, it is incremented by 1.
        outer_count = 0
        
        # We only need to remove k digits. So iterate only k times (0,1,2......,k - 1).
        while outer_count != k:
            
            # Setting inner counter to zero. This counter is used to iterate over the whole string.
            inner_count = 0
            
            # inner_count < len(num) - 1 to iterate over whole string.
            while inner_count < len(num) - 1:

                # Checking if the digit is in ascending order. If yes, then go to next digit.
                if  num[inner_count] <= num[inner_count + 1]:
                    inner_count += 1

                # Else break from the while loop.    
                else:
                    break

            # Remove the value at index inner_count.
            # NOTE: If the while loop is not breaked explicitly then inner_count will have last index.(It means All digits are in ascending order so remove last)        
            num = num[:inner_count] + num[inner_count + 1:]
            
            # Increment the outer_count.
            outer_count += 1

        # If after stripping the leading zeros the string becomes empty then return 0. This happens if only zeros are remaining.    
        if len(num.lstrip('0')) == 0:
            return "0"
        
        # Else return the num with no leading zeros.
        else:
            return num.lstrip('0')
                    
            

# For example: num="1432219" and k = 3.
# Start from left, 4 and 3 are not in order so remove 4.
# 3 and 2 are not in order so remove 3.
# 2 and 1 are not in order so remove 2.
# Final num is "1219".