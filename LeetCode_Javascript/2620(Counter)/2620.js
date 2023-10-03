var createCounter = (n) => () => {
  // 52ms 82%
  return n++;
};

var createCounter = function(n) {
  let cnt = n - 1
  return function() {
    cnt++;
    return cnt;
  }
}

var createCounter = function(n) {
  return function() {
    return n++;
  }
}