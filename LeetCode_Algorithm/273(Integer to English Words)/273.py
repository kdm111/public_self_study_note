class Solution:
    def one(self, c):
        dic = {
            '1' : 'One',
            '2' : 'Two',
            '3' : 'Three',
            '4' : 'Four',
            '5' : 'Five',
            '6' : 'Six',
            '7' : 'Seven',
            '8' : 'Eight',
            '9' : 'Nine'
        }
        return dic[c]
    def under_twenty(self, c):
        dic = {
            '10' : 'Ten',
            '11' : 'Eleven',
            '12' : 'Twelve',
            '13' : 'Thirteen',
            '14' : 'Fourteen',
            '15' : 'Fifteen',
            '16' : 'Sixteen',
            '17' : 'Seventeen',
            '18' : 'Eighteen',
            '19' : 'Nineteen',
        }
        return dic[c]
    def ten(self, c):
        dic = {
            '20' : 'Twenty',
            '30' : 'Thirty',
            '40' : 'Fourty',
            '50' : 'Fifty',
            '60' : 'Sixty',
            '70' : 'Seventy',
            '80' : 'Eighty',
            '90' : 'Ninety'
        }
        return dic[c]
        
    def numberToWords(self, num: int) -> str:
        ans = ""
        for div in [1000000000, 1000000, 1000, 100, 10, 1]:
            d = num // div
            num %= div
            if d > 0:
                if d >= 100:
                    ans += self.one(str(d // 100)) + ' Hundred ' 
                    d %= 100
                if d >= 10:
                    if d < 20:
                        ans += self.under_twenty(str(d))
                    else:
                        ans += self.ten(str(d)[0] + '0')
                    d %= 10
                if d > 0:
                    ans += self.one(str(d))
        return ans

'''
hundred : 3
thousand : 4
million : 7
billion : 9

                if div == 1000000000:
                    ans += ' Billion'
                if div == 1000000:
                    ans += ' Million'
                if div == 1000:
                    ans += ' Thousand'
                if div == 100:
                    ans += ' Hundred'

'''
print(Solution().numberToWords(999))