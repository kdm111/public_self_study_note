var MovingAverage = function(size) {
  // sol1 153~197ms 48~19%
  this.queue = new Array(size)
  this.head = 0
  this.size = size
  this.length = 0
  this.totalSum = 0
};

MovingAverage.prototype.next = function(val) {
  if (this.queue[this.head] != undefined){
    this.totalSum -= this.queue[this.head]
    this.length -= 1
    this.queue[this.head] = undefined
  }
  this.queue[this.head] = val
  this.head = (this.head + 1) % this.size
  this.length += 1
  this.totalSum += val
  return this.totalSum / this.length

};

obj = new MovingAverage(3)
console.log(obj.next(1))
console.log(obj.next(2))
console.log(obj.next(3))
console.log(obj.next(4))



console.log(obj.queue)