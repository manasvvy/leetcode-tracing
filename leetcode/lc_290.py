class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in charToWord:
                if charToWord[char] != word:
                    return False
            else:
                charToWord[char] = word

            if word in wordToChar:
                if wordToChar[word] != char:
                    return False
            else:
                wordToChar[word] = char
        return True
           
