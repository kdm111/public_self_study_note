from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # sol1 O(n), 48~68ms 77~36%
        # ans = []
        # for i in range(1, n+1):
        #     string = ""
        #     if i % 3 == 0 and i % 5 == 0:
        #         string = "FizzBuzz"
        #     elif i % 5 == 0:
        #         string = "Buzz"
        #     elif i % 3 == 0:
        #         string = "Fizz"
        #     else:
        #         string = str(i)
            
        #     ans.append(string)
        # return ans


        # sol2 47~83ms 78~13%

        ans = []
        hashMap = {
            3 : "Fizz",
            5 : "Buzz"
        }
        
        for num in range(1, n+1):
            num_ans_str = ""

            for key in hashMap.keys():
                if (num % key) == 0:
                    num_ans_str += hashMap[key]
            
            if num_ans_str == "":
                num_ans_str = str(num)

            ans.append(num_ans_str)

        return ans

print(Solution().fizzBuzz(4))