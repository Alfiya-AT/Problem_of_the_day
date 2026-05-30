class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split(" ")

        # Length should match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            # Check char -> word mapping
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word

            # Check word -> char mapping
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch

        return True


obj = Solution()

pattern = "abba"
s = "dog cat cat dog"

print(obj.wordPattern(pattern, s))