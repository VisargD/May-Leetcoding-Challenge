# This is my solution using list. It is pretty much easy.
# But it is also not an efficient solution as every word is inserted as a new word. 
# The same thing can be done using dictionary and it is much more efficient.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initializing an empty list.
        self.mylist = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Inserting element into the list using append().
        self.mylist.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Checking if the word is present in the list.
        return word in self.mylist

    def startsWith(self, prefix: str) -> bool:
        
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Looping through the list.
        for x in self.mylist:
            
            # Checking if the current element starts with the prefix.
            if x.startswith(prefix):
                return True
        # If no element start with prefix then return False.
        return False     

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)