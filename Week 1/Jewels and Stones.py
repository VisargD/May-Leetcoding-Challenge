class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        # Initializing the counter.
        total_count = 0

        # Looping through each character in string J.
        for char in J:

            # Adding the counts of char in J to the counter
            total_count += S.count(char)

        # Returning the counter value.
        return total_count
