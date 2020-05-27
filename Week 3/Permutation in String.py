class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Converting to list and sorting so that it becomes easy to find a match regardless of order of characters.
        s1 = sorted(list(s1))

        # Storing length of s1 and s2 for further use.
        s2_length = len(s2)
        s1_length = len(s1)

        # Looping through indices of s2 such that substring of s1_length can be matched for every index.
        for i in range(s2_length - s1_length + 1):

        	# If the current substring of s2_length matches s1 then return True.
            # Here, a list is made and then it is sorted so that matching can be done regardless of order of words.
            if sorted(list(s2[i:i+s1_length])) == s1:
                return True

        # If no permutation is found then return False.        
        return False