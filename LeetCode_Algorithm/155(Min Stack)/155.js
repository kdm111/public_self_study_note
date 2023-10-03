var MinStack = function() {
  // sol2 129ms 80%
  this.arr = []    
};

MinStack.prototype.push = function(val) {
  if (this.arr.length == 0) {
    this.arr.push([val, val])
  } else{
    if (this.arr[this.arr.length-1][1] > val) {
      this.arr.push([val, val])
    } else {
      this.arr.push([val, this.arr[this.arr.length-1][1]])
    }
  }
};

MinStack.prototype.pop = function() {
  this.arr.pop()
};

MinStack.prototype.top = function() {
  return this.arr[this.arr.length-1][0]
};

MinStack.prototype.getMin = function() {
  return this.arr[this.arr.length-1][1]
};
