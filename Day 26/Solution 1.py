class Solution(object):
    def __init__(self):
        self.digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
    }

def letterCombinations(self, digits):
    """
        :type digits: str
        :rtype: List[str]
        """
            if len(digits) == 0:
                return []
                    results = []
                    
                    def dfs(digits, i, word):
                        if i == len(digits):
                            results.append(word)
                            return
                                for comb in self.digit_map[digits[i]]:
                                    word += comb
                                        dfs(digits, i+1, word)
                                        word = word[:-1]
                                            dfs(digits, 0, "")
                                            return results
