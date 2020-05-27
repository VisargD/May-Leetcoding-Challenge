class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # Sorting the pattern so that it can be matched in any order.
        p = sorted(list(p))
        
        # Empty list to store index.
        newlist = []

        # Storing the length of pattern.
        length = len(p)

        # Looping through the string such that the we can check substring of length equal to pattern length.
        for i in range(len(s) - length + 1):
            
            # Checking the sorted substring of length equal to pattern length.
            # sorted is used so that order of characters match the sorted pattern.    
            list1 = sorted(list(s[i:i + length]))
            
            # If the all the characters match then it is an anagram of pattern.
            # Append the index to newlist.
            if list1 == p:
                newlist.append(i)

        # Return the newlist.
        return newlist