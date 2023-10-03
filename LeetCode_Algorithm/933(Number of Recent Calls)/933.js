var RecentCounter = function() {
  // sol1 191ms 95% 57% 35%
  this.queue = []  
};
RecentCounter.prototype.ping = function(t) {
  this.queue.push(t)
  while (this.queue.length && this.queue[0] < t-3000) {
    this.queue.shift()
  }
  return this.queue.length
};