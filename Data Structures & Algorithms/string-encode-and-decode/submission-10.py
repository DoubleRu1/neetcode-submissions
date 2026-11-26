class Solution:

    def encode(self, strs: List[str]) -> str:
        word_end = "<WORD_END>"
        s = ""
        for word in strs:
            s += word+word_end
        return s
    def decode(self, s: str) -> List[str]:

        word_end = "<WORD_END>"
        word_list = s.split("<WORD_END>")
        return word_list[:-1]
        
