var bitwiseComplement = function(n) {
// sol3 O(1), O(1) 74~126ms 48~5% 
  // bitmask
  if (n==0){return 1}
  l = parseInt(Math.log2(n)) + 1
  bitmask = (1 << l) - 1 
  return n ^ bitmask
};

console.log(bitwiseComplement(4))