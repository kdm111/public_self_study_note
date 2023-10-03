var SmallestInfiniteSet = function() {
  // sol1 126ms 87% 50% 40%
  this.curr = 1
  this.s = new Set()    
};

SmallestInfiniteSet.prototype.popSmallest = function() {
  if (this.s.size) {
    let ret = Math.min(...this.s)
    this.s.delete(ret)
    return ret
  } else {
    this.curr += 1
    return this.curr - 1
  }
};


SmallestInfiniteSet.prototype.addBack = function(num) {
  if (this.curr > num) {
    this.s.add(num)
  }
};