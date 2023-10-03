import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # sol1 hashMap O(n) 109ms 29%
        if len(ransomNote) > len(magazine): return False

        def makeMap(string):
            temp = {}
            for char in string:
                if char in temp:
                    temp[char] += 1
                else:
                    temp[char] = 1
            return temp

        ransomNote_map = makeMap(ransomNote)
        magazine_map = makeMap(magazine)

        for char in ransomNote_map:
            if char in magazine_map: 
                if magazine_map[char] < ransomNote_map[char]:
                    return False
            else:
                return False
        return True


        
        pass

print(Solution().canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
print(Solution().canConstruct("a", "b"))
