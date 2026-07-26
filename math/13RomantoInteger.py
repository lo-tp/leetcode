class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"],
        ]
        res = 0
        for v_idx in range(2, -1, -1):
            if mapping[v_idx][-1] in s:
                base = 10**v_idx
                res += 9 * base
                s = s.replace(mapping[v_idx][-1], "")
        # print(res)

        for h_idx in range(2, 0, -1):
            if mapping[-1][h_idx] in s:
                s = s.replace(mapping[-1][h_idx], "")
                res += (h_idx) * 1000
        # print(res)

        for v_idx in range(2, -1, -1):
            for h_idx in range(8, 5, -1):
                if mapping[v_idx][h_idx] in s:
                    base = 10**v_idx
                    res += h_idx * base
                    s = s.replace(mapping[v_idx][h_idx], "")
            for h_idx in range(4, -1, -1):
                if mapping[v_idx][h_idx] in s:
                    base = 10**v_idx
                    res += h_idx * base
                    s = s.replace(mapping[v_idx][h_idx], "")
                if mapping[v_idx][5] in s:
                    base = 10**v_idx
                    res += 5 * base
                    s = s.replace(mapping[v_idx][5], "")
        return res
