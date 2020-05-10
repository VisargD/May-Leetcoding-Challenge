# The idea behind this code is that we first make a list that contains zero for all the N people.
# For a person to be judge, during the "for" loop no value should be decremented as judge trusts no one.
# And for judge the value should be incremented exact N - 1 times during the for loop as the judge is trusted by all the N - 1 other people.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # Creating a list containing 0 for all indices.
        # Here our indices represent 1....N people.
        newlist = [0 for x in range(1, N + 1)]
        
        # Looping through the trust list. Here x will also be a list.
        for x in trust:
            
            # Increasing value by 1 at index x[1]. (The person x[1] is trusted by someone)
            # Decreasing value by 1 at index x[0]. (The person x[0] trusts someone)
            newlist[x[1]] += 1
            newlist[x[0]] -= 1
        
        # Checking the edge case
        if N == 1:
            return 1
        
        # Checking if maximum of newlist is equal to N - 1.
        # If yes then it means that the index with max value is the judge.
        elif max(newlist) == N - 1:
            return newlist.index(max(newlist))

        # Return -1. No judge possible.
        else:
            return -1
            