class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for s in strs:
            encode_string += str(len(s)) + "#" + s
        return encode_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])
            i = j + 1
            j = i + str_len
            res.append(s[i:j])
            i = j
        return res
