var countSegments = function(s) {
  // sol1 T : 83ms 68% S : 41.9MB 51%
  return s.split(" ").filter(function(n) {return n}).length
};

console.log(countSegments("abb aa"))