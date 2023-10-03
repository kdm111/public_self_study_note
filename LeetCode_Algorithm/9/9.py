class Solution:
    
    def isPalindrome(self, x: int) -> bool:       
        # 문자열 변환 시 74ms 
        num_to_string = str(x)
        for i in range(len(num_to_string)//2):
            if num_to_string[i] != num_to_string[len(num_to_string) -1 -i]:
                return False
                
        # 리스트로 변환시 148ms
        # num_to_list = list(map(str, str(x)))
        # for i in range(len(num_to_list)//2):
        #     if num_to_list[i] != num_to_list[len(num_to_list) -1 -i]:
        #         return False
        # return True

print(Solution().isPalindrome(-121))
