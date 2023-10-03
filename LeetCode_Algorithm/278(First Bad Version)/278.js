var solution = function(isBadVersion) {
  function isBadVersion(n){
    let badVersion = 3
    return (n < badVersion) ? false : true
  }
  return function(n) {
    // sol1 O(n), O(1) 시간초과
    // for (let i=1; i < n+1; i++){
    //   if (isBadVersion(i) == true){
    //     return i
    //   }
    // }
    // return n
    // sol2 O(logn) O(1) 65~81ms 78~54%
    var left = 0
    var right = n
    while (left <= right) {
      
      let mid = parseInt((left+right)/2)
      console.log(mid)
      if (isBadVersion(mid) == false){ left = mid+1 }
      else{
        if (isBadVersion(mid-1) == false){ return mid }
        right = mid-1
      }
    }
  };
};

console.log(solution()(5))