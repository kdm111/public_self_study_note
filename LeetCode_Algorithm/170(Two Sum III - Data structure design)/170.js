var TwoSum = function() {
  // sol2 1284ms 55% 93.5MB 32%
  this.hashMap = {}
};

TwoSum.prototype.add = function(number) {
  if (this.hashMap[number] == undefined){
    this.hashMap[number] = 1
  } else {
    this.hashMap[number] += 1
  }
};

TwoSum.prototype.find = function(value) {
  for (let k in this.hashMap) {
    let c = value - k
    if (c != k) {
      if (this.hashMap[c] != undefined)
        return true
    } 
    if(this.hashMap[c] > 1) {
      return true
    }
  }
  return false
};
