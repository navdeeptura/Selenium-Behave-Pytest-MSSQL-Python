class ReverseString:

    def reverseUsingStringReverse(self, n: str) -> str:
        return n[::-1]


    def reverseUsingCharLoop(self, n: str) -> str:
        str_arr = []
        for i in range(len(n)-1, -1, -1):
            str_arr.append(n[i])
        print(str_arr)
        return "".join(str_arr)
