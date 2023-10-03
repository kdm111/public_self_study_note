class Solution:
    def intToRoman(self, num: int) -> str:
        # greedy 68ms 53%
        # hashMap = {
        #     1000 : 'M',
        #     500 : 'D',
        #     100 : 'C',
        #     50 : 'L',
        #     10 : 'X',
        #     5 : 'V',
        #     1 : 'I',
        # }
        # ans = ""
        # while 0 < num:
        #     if 1000 <= num:
        #         num -= 1000
        #         ans += hashMap[1000]
        #     elif 900 <= num:
        #         num += 100
        #         ans += hashMap[100]
        #     elif 500 <= num:
        #         num -= 500
        #         ans += hashMap[500]
        #     elif 400 <= num:
        #         num += 100
        #         ans += hashMap[100]
        #     elif 100 <= num:
        #         num -= 100
        #         ans += hashMap[100]
        #     elif 90 <= num:
        #         num += 10
        #         ans += hashMap[10]
        #     elif 50 <= num:
        #         num -= 50
        #         ans += hashMap[50]
        #     elif 40 <= num:
        #         num += 10
        #         ans += hashMap[10]
        #     elif 10 <= num:
        #         num -= 10
        #         ans += hashMap[10]
        #     elif 9 <= num:
        #         num += 1
        #         ans += hashMap[1]
        #     elif 5 <= num:
        #         num -= 5
        #         ans += hashMap[5]
        #     elif 4 <= num:
        #         num += 1
        #         ans += hashMap[1]
        #     elif 1 <= num:
        #         num -= 1
        #         ans += hashMap[1]
        # return ans


        # sol2 80ms 34%
        # thousands = ['', 'M', "MM", "MMM"]
        # hundreds = ['', 'C', "CC", "CCC", "CD", 'D', "DC", "DCC", "DCCC", "CM"]
        # tens = ['', 'X', "XX", "XXX", "XL", 'L', "LX", "LXX", "LXXX", "XC"]
        # ones = ['', 'I', "II", "III", "IV", 'V', "VI", "VII", "VIII", "IX"]

        # ans = ""
        # x = num // 1000; num %= 1000
        # ans += thousands[x]
        # x = num // 100; num %= 100
        # ans += hundreds[x]
        # x = num // 10; num %= 10
        # ans += tens[x]
        # x = num // 1; num %= 1
        # ans += ones[x]
        # return ans


        # sol3 T : 55ms 89% S : 13.9MB 35%
        ans = ""
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        valIdx = len(value) - 1
        symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        while valIdx > -1:
            cnt = 0
            while cnt < num // value[valIdx]:
                ans += symbol[valIdx]
                cnt += 1 
            num %= value[valIdx]
            valIdx -= 1
        return ans

        


print(Solution().intToRoman(2222))