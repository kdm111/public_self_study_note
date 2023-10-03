function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

var addTwoNumbers = function(l1, l2) {
  // sol1 114ms 30% 48MB 13%
  let stack1 = makeStack(l1); let stack2 = makeStack(l2)
  let stack = []; let endNode = null
  while(stack1.length || stack2.length) {
    let val = 0
    if (stack1.length) {
      val += stack1.pop().val
    }
    if (stack2.length) {
      val += stack2.pop().val
    }
    if (endNode) {
      val += endNode.val
    }
    let m = parseInt(val / 10); let n = parseInt(val % 10)
    stack.push(new ListNode(n))
    endNode = new ListNode(m)
  }
  if (endNode && endNode.val > 0)
    stack.push(endNode)
  let ans = stack[stack.length-1]
  let temp = stack[stack.length-1]
  for (let i = stack.length-2; i >= 0; i--) {
    temp.next = stack[i]
    temp = stack[i]
  }
  return ans
};
var makeStack = (l) => {
  let stack = []
  // js에서는 0은 false
  while (l && l.val >= 0) {
    stack.push(l)
    l = l.next
  }
  return stack
}