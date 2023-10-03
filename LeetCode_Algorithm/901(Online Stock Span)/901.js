var StockSpanner = function() {
  // sol1 290ms 56% 54.7MB 29%
  this.stack = []
};

StockSpanner.prototype.next = function(price) {
  let ans = 1
  while (this.stack.length > 0 && this.stack[this.stack.length-1][0] <= price) {
    ans += this.stack.pop()[1]
  }
  this.stack.push([price, ans])
  return ans
};