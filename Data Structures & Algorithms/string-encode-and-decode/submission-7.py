class Solution:
    delim = "#$%^|:;"
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(f"{len(i)}{self.delim}{i}{self.delim}")
        # print(encoded)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        if s == '':
            return []
        split_val = s.split(self.delim)
        for i in range(1, len(split_val), 2):
            decoded.append(split_val[i])
        print(decoded)
        return decoded