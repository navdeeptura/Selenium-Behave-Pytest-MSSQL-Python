class Solution:
    """
    Initialize pointers i = 0, j = 0
    Initialize an empty final string RESULT
    While loop: i < len(word1) and j < len(word2)
        add word[i] to RESULT
        add word[j] to RESULT
        increment i and j
    Append remaining letters from word1
    Append remaining letters from word2
    return RESULT
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        final_string = ""
        print(word1, word2, len(word1), len(word2))
        len_word1 = len(word1)
        len_word2 = len(word2)
        while i < len_word1 and j < len_word2:
            final_string += word1[i]
            final_string += word2[j]
            i += 1
            j += 1

        # string_to_add = word2[j:] if len_word2 > len_word1 else word1[i:]
        # final_string += string_to_add
        final_string += word1[i:]
        final_string += word2[j:]

        return final_string


word1 = "ab"
word2 = "pqrs"
c = Solution()
v = c.mergeAlternately(word1, word2)
print (v)