var mergeTrees = function(root1, root2) {
    // sol1 88ms 99%
    return dfs(root1, root2)
};
var dfs = function(root1, root2) {
    if (!root1) {
        return root2
    }
    if (!root2) {
        return root1
    }
    root1.val += root2.val
    root1.left = dfs(root1.left, root2.left)
    root1.right = dfs(root1.right, root2.right)
    return root1
}