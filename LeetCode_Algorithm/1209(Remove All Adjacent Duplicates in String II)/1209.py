'''
LeetCode 1209 : Remove All Adjacent Duplicates in String II
문자열에서 주어진 k 만큼 삭제하여 리턴하라

# sol1
O(n) O(n)
스택에 넣어가면서 글자가 주어진 글자가 연속적이면 카운트를 더해간다.
연속적이지 않다면 1부터 다시 카운트를 시작한다.

'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []; cntArr = []
        for c in s:
            if stack and cntArr[-1][0] == c:
                cntArr[-1][1] += 1
                stack.append(c)
                if cntArr[-1][1] == k:
                    while cntArr[-1][1]:
                        cntArr[-1][1] -= 1
                        stack.pop()
                    cntArr.pop()
            else:
                cntArr.append([c, 1])
                stack.append(c)
        return "".join(stack)

print(Solution().removeDuplicates("xaax", 2))
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2))
print(Solution().removeDuplicates("dtpdtaaaaaaaaappppppppppppppppppppaaaaaaaaaaxxxxxxxxxxxxxxsssssssssjjjjjjjjjjjjjjjjjjjjxxxxxxxxxxxxxxxxxxxxsssssssjjjjjjjjjjjjjjjjjjjjssssxxxxxxatdwvvpctpggggggggggggggggggggajagglaaaaaaaaaaaaaaaaaaaa", 20))


