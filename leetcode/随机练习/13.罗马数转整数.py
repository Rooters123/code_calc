class Solution:
    def romanToInt(self, s: str) -> int:
        tmp = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        total = 0
        for i in range(len(s) - 1):
            if tmp[s[i]] < tmp[s[i + 1]]:
                total -= tmp[s[i]]
            else:
                total += tmp[s[i]]
        total += tmp[s[-1]]
        return total
