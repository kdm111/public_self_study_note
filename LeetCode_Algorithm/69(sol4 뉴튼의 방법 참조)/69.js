var mySqrt = function(x) {
  // sol1 O(1) O(1) 78~124ms 86~38%
  // return parseInt(x**0.5)

  // sol1-1 O(1) O(1) 64~80ms 98%
  // var left = parseInt(Math.E ** (0.5 * Math.log(x)))
  // var right = left + 1
  // return (right*right > x) ? left : right;

  // sol2 O(logn), O(1) 68~88ms 97~77%
  // var left = 1; var right = x
  // while (left <= right){
  //   let pivot = parseInt(left + (right-left)/2)
  //   let num = pivot*pivot
  //   if (num < x) { left = pivot+1 }
  //   else if (num > x) {right = pivot-1}
  //   else {return pivot}
  // }
  // return right


  // sol3 68~144ms 97~25%
  if (x < 2) { return x }
  var left = mySqrt(x >> 2) << 1
  var right = left+1
  console.log(left, right)
  return (right * right > x) ? left : right

};
console.log(mySqrt(10))