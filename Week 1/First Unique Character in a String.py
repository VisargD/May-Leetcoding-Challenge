class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Initialize a default value to -1 so that it can be used if every word is a repeating word.
        default = -1
        
        # Looping through all the index of string s.
        for index in range(len(s)):

            # Checking if character at index has count equal to 1.
            # If count == 1 then it will return index of the first character having count == 1.
            if s.count(s[index]) == 1:
                return index

        # If no character has count == 1 then it will return the default value -1    
        return default
        