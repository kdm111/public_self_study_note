var MyQueue = function() { 
  // 139ms 5%
  this.lst = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
  this.lst.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
  return this.lst.shift()
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
  return this.lst[0]
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
  return this.lst.length == 0
};