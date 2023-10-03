var RandomizedSet = function() {
  // sol1 417ms 90% 94.3MB 84%
  this.arr = []
  this.hashMap = new Map()
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
  if (this.hashMap.has(val)) {
    return false
  }  
  this.hashMap.set(val, this.arr.length)
  this.arr.push(val)
  return true
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
  if (!this.hashMap.has(val)) {
    return false
  }
  let last = this.arr[this.arr.length-1]; let idx = this.hashMap.get(val)
  this.arr[idx] = last; this.hashMap.set(last, idx)
  this.arr.pop()
  this.hashMap.delete(val)
  return true
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
  return this.arr[Math.floor(Math.random() * this.arr.length)]
};
