# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root) ->  List[List[int]]:
        # O(n)(tree traversal) O(nlogn)(sort), O(n) 55ms 30%
        if root == []:
            return []
        rootNode = self.makeTree(root, 0)
        queue = []
        hashMap = {}
        queue.append([rootNode, 0])
        while queue:
            root = queue.pop(0)
            rootNode = root[0]
            key = root[1]
            if key not in hashMap:
                hashMap[key] = [rootNode.val]
            else:
                hashMap[key].append(rootNode.val)
            if rootNode.left:
                queue.append([rootNode.left, key-1])
            if rootNode.right:
                queue.append([rootNode.right, key+1])

        sorted_hashMap = sorted(hashMap.items(), key = lambda hashMap : hashMap[0])
        ans = []
        for values in sorted_hashMap:
            temp  = []
            for value in values[1]:
                if value != None:
                    temp.append(value)
            if len(temp) != 0:
                ans.append(temp)
        
        return ans
            




            
        return [1]

    def makeTree(self, root, idx):
        rootNode = TreeNode(root[idx])
        if 2*idx + 1 < len(root):
            rootNode.left = self.makeTree(root, 2*idx + 1)
        if 2*idx + 2 < len(root):
            rootNode.right = self.makeTree(root, 2*idx + 2)
        return rootNode
        



print(Solution().verticalOrder([3,9,20,None,None,15,7]))