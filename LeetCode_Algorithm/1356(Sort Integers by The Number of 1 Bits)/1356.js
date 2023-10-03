var sortByBits = function(arr) {
  // sol3 122ms 77% 43.8MB 98%
   arr.sort((a,b) => {
    return (cnt1Bits(a) - cnt1Bits(b) || a-b)
   })
   return arr
};

var cnt1Bits = function(num) {
  let cnt = 0
  while (num > 0) {
    if (num & 1) {
      cnt++
    }
    num >>= 1
  }
  return cnt
}
console.log(sortByBits([1111,7644,1107,6978,8742,1,7403,7694,9193,4401,377,8641,5311,624,3554,6631]))
