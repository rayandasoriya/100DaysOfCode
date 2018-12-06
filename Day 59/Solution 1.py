class Solution:
    def findWords(self, words):
        values = (
                  set("qwertyuiop"),
                  set("asdfghjkl"),
                  set("zxcvbnm")
                  )
            
            
                  result = []
                  for word in words:
                      for row in values:
                          if not set(word.lower()).difference(row):
                              result.append(word)
                      return result
