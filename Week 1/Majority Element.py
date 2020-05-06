class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Sorting the list so that same numbers get together in sequence.
        sorted_list = sorted(nums)

        # Initializing element to the first element of the  sorted_list to compare during for loop.
        element = sorted_list[0]

        # Initializing counter to store occurence of elements.
        count = 0

        # Length to compare if count is greater than (n / 2).
        length = len(sorted_list) // 2

        # Looping through element of sorted_list.
        for x in sorted_list:

            # Checking if x is same as element. If yes, then increment count. 
            if x == element:
                count += 1

                # Check if count is greater than n // 2. If yes, then return x
                if count > length:
                    return x

            # Else if x is not equal to element that mean it is a new element. So make element = x and reset the counter to 1.
            else:
                element = x
                count = 1 


# I tried solving this problem by taking a for loop and checking if count of element on the list is greater than (size of list) // 2.
# If yes, then return that element.
# But it resulted in TLE. So, I came up with this alternate approach.