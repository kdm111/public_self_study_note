# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
LeetCode 236 : Lowest Common Ancestor of a Binary Tree
LCA 구하기

# sol1
postorder 순회를 하여 현재 값이 p나 q와 일치하면 일치한다는 시그널을 보낸다.
여기서 left는 왼쪽 노드에서 올라온 매칭값이고 right는 오른쪽에서 올라온 매칭값
mid는 현재 노드와 일치하는 값이 있는 지 매칭하는 값이다.
left + right + mid가 2이상일 경우 현재 노드가 LCA가 된다.


# sol2
똑같은 postorder로 순회하되 현재 노드가 둘 중 하나와 만이라도 같다면 그 노드를 리턴한다.
left는 왼쪽 하위 트리 right는 오른쪽 하위 트리에서 나오는 값으로 
그 둘이 참이라면 현재 노드를 리턴하고
아니면 그 둘 중 참인 값을 리턴한다.

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # sol1
        # self.p_val = p.val
        # self.q_val = q.val
        # self.ans = root
        # self.solve(root)
        return self.solve2(root, p, q)

    def solve2(self, node, p, q):
        if not node:
            return False
        if node == p or node == q:
            return node
        left = self.solve2(node.left, p, q)
        right = self.solve2(node.right, p, q)
        if left and right:
            return node
        if left:
            return left
        return right
    def solve(self, node):
        if not node:
            return False
        left = self.solve(node.left)
        right = self.solve(node.right)
        mid = (node.val == self.p_val) or (node.val == self.q_val)
        if mid + left + right >= 2:
            self.ans = node
        return mid or left or right
            
print(Solution().lowestCommonAncestor())