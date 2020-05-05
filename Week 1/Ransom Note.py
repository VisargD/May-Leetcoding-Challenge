class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Initializing answer to True. (By default answer will be True)
        answer = True

        # Converting the magazine string to list to make it easy to check.
        magazine_list = list(magazine)

        # Looping through each character of ransomNote.
        for char in ransomNote:

            # Checking if the char is present in the magazine_list.
            if char in magazine_list:

                # If the char is present in the list then don't change the answer and remove the char from list.
                # So next time it does not consider the same char. 
                magazine_list.remove(char)

            # Else condition:- If char not present in list then change answer to False and return answer   
            else:
                answer = False
                return answer

        # Return True as answer (Occurs when the else condition is never triggered).
        return answer
                
