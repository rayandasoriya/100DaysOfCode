class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.word = ''


class WordDictionary(object):
    
    def __init__(self):
        """
            Initialize your data structure here.
            """
        self.root = TrieNode()
    
    def addWord(self, word):
        """
            Adds a word into the data structure.
            :type word: str
            :rtype: void
            """
        node = self.root
        for char in word:
            if node.children[ord(char) - ord('a')] is None:
                node.children[ord(char) - ord('a')] = TrieNode()
            node = node.children[ord(char) - ord('a')]
        node.word = word
    
    def search(self, word):
        """
            Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
            :type word: str
            :rtype: bool
            """
        node = self.root
        return self.match(word, 0, node)
    
    def match(self, word, index, node):
        if index == len(word):
            return node.word != ''
        if word[index] != '.':
            if node.children[ord(word[index])-ord('a')] is not None:
                return self.match(word, index + 1, node.children[ord(word[index])-ord('a')])
        else:
            for i in range(26):
                if node.children[i] is not None:
                    if self.match(word, index + 1, node.children[i]):
                        return True
        return False
