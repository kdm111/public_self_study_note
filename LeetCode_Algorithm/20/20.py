from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        # sol1 51ms 35.78% 빠름
        # stack = []
        # que = deque(s)

        # while que:
        #     que_char = que.popleft()
        #     if que_char == "(" or que_char == "[" or que_char == "{":
        #         stack.append(que_char)
        #     else:
        #         if stack:
        #             stack_char = stack.pop()
        #             if que_char == ")" and stack_char == "(":
        #                 continue
        #             elif que_char == "}" and stack_char == "{":
        #                 continue
        #             elif que_char == "]" and stack_char == "[":
        #                 continue
        #             else:
        #                 return False
        #         else:
        #             return False

        # if stack: return False
        # return True

        # sol2 편차가 들쭉날쭉함. 최소 39ms 최대 65ms 68%보다 빠름
        if len(s)%2 != 0: return False

        stack = []
        brackets = [char for char in s]
        bracket_map = {"(" : ")", "{" : "}", "[" : "]"}
        
        while brackets:
            bracket = brackets.pop(0)
            if bracket in bracket_map: stack.append(bracket)
            else:
                if not stack: return False
                stack_char = stack.pop() 

                if bracket_map[stack_char] == bracket: continue
                else: return False
        
        return not stack
        

        
                




print(Solution().isValid('()'))