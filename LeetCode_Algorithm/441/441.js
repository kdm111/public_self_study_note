var arrangeCoins = function(n) {
  
  // sol1 O(1), O(1) 85~113ms 85~55%
  // return parseInt(Math.sqrt(2*n+0.25) - 0.5)

  // sol2 O(logn), O(1) 113~134ms 55~30%
  var left = 0; var right = n;
  while (left <= right){
    const mid = parseInt((left+right)/2)
    const k = parseInt(mid*(mid+1) / 2)

    if (k == n) {
      return mid
    }
    if (k < n){
      left = mid+1
    }
    else{
      right = mid-1
    }
  }
  return right
};

console.log(arrangeCoins(3))