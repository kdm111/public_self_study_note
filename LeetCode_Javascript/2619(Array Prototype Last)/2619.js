Array.prototype.last = function() {
  // 50ms 88% 41.6MB 86%
  let len = this.length
  return len == 0 ? -1 : this[len-1]
};
