class PalindromeCheck:

    def verifyPalindrome(self, st: str) -> bool:

        st = [i.lower() for i in st if i.isalnum()]
        st = ''.join(st)
        st = st.lower()
        left = 0
        right = len(st) - 1
        while left < right:
            if st[left] == st[right]:
                left += 1
                right -= 1
            else:
                return False
        return True