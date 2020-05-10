# When I first saw this problem I wrote this code. This is not at all an efficient solution.
# But somehow, it got excepted without TLE.
# I also solved this problem with a more efficient code.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # Checking if there is only one person
        if N == 1:
            return 1

        # Creating a list of all the people who trust somebody.    
        trustee = [x[0] for x in trust]

        # Creating a list of all the people who are trusted by somebody.
        trusted = [x[1] for x in trust]

        # Looping through the trusted list.
        for x in trusted:

            # Checking if an element has a count N - 1 and it is not present in trustee.
            # If such element exist then it will be the judge as it is trusted by all other (N - 1) and trusts noone (not present in trustee)
            if (trusted.count(x) == N - 1) and x not in trustee:
                return x

        # Return -1 if judge not found.        
        return -1