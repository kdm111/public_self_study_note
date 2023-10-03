var Logger = function() {
  // sol1 217ms 70% 52MB 38%
  this.hashMap = {}    
};

Logger.prototype.shouldPrintMessage = function(timestamp, message) {
  if (this.hashMap[message]) {
    if (timestamp < this.hashMap[message]) {
      return false
    } else {
      this.hashMap[message] = timestamp + 10
      return true
    }
  } else {
    this.hashMap[message] = timestamp + 10
    return true
  }
};
