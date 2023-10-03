 function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function solve1(nums, left, right) {
  // O(n), O(logn) 104ms 59%
  if (left > right){return null}
  let mid = left + parseInt((right-left)/2)
  const root = new TreeNode(nums[mid])
  root.left = solve1(nums, left, mid-1)
  root.right = solve1(nums, mid+1, right)
  return root
}
var sortedArrayToBST = function(nums) {
  return solve1(nums, 0, nums.length-1)  
};

console.log(sortedArrayToBST([1,2,3,4,5]))