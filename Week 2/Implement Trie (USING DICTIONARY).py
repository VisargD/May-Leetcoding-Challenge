# Dictionary is used in this solution. All the characters are stored as a key and a value which contains a dictionary.
# For example: "hey". Here h is stored as a key and its value is a dictionary. {'h':{}}
# Then "e" is stored as a key and its value is a dictionary. Same process is followed for all the characters.
# The last character of a word is indicated by #end.
# {'h':{'e':{'y':{'#end':'#'}}}} . This is how the word "hey" is stored.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initializing a dictionary.
        self.mydict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Initializing a variable "trie" to mydict.
        trie = self.mydict
        
        # Looping through each character of word.
        for alpha in word:

            # Checking if the character already exists. If yes, then set the level of trie to that character.
            if alpha in trie:
                trie = trie[alpha]
            
            # Else, add the new character as key with an empty dict as its value.
            # And then change the level to the newly added key.
            else:
                trie[alpha] = {}
                trie = trie[alpha]
                
        # This marks the end of the word. 
        trie['#end'] = '#'
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Initializing a variable "trie" to mydict.
        trie = self.mydict
        
        # Looping through each character of word.
        for alpha in word:

            # Checking if the character is in the trie. If yes, then change the level to that key.
            if alpha in trie:
                trie = trie[alpha]
            
            # If any of the character is not present then return False.
            else:
                return False
        
        # If all the character are present then check if end is present at current level.
        # This confirms that the word is not a part of any other word. And it confirms that it is the required word.
        if '#end' in trie:
            return True 

        # If there is no end then the word is a sub-part of another long word and it is not an independent word.
        # So return False.
        else:       
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Initializing the variable "trie" to mydict.
        trie = self.mydict

        # The same process that we did for "search" is followed for startsWith but,
        # The only difference is that we do not have to check for end as we only have to check for prefix.
        for alpha in prefix:

            if alpha in trie:
                trie = trie[alpha]
            
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)