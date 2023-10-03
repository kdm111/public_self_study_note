// sol1 
// 716ms 27%
var TimeMap = function() {
  this.hashMap = new Map()    
};

TimeMap.prototype.set = function(key, value, timestamp) {
  if (!this.hashMap[key]) {
    this.hashMap[key] = new Map()
    this.hashMap[key].set(value, timestamp)
  } else {
    this.hashMap[key].set(value, timestamp)
  }
  return null
};

TimeMap.prototype.get = function(key, timestamp) {
  let time = 0; let ret = ""; timestamp = parseInt(timestamp)
  if (this.hashMap[key] != null) {
    this.hashMap[key].forEach((v, k) => {
      if (v < timestamp+1 && time < v) {
        ret = k; time = v
      }
    })
  }
  return ret
};

var timeMap = new TimeMap()
console.log(timeMap.set("key", "value", 1))
console.log(timeMap.get("key", 1))
console.log(timeMap.get("key", 3))
console.log(timeMap.set("key", "value2", 3))
console.log(timeMap.get("key", 4))




// console.log(timeMap)