var solve = (lo, hashMap) => {
  if (lo == 1) {
    return 0;
  }  
  if (hashMap[lo]) {
    return hashMap[lo]
  }
  let res = 0
  if (lo % 2 == 0) {
    res = solve(parseInt(lo/2), hashMap)+1
  } else {
    res = solve(3*lo+1, hashMap)+1
  }
  hashMap[lo] = res
  return hashMap[lo]
}

var getKth = function(lo, hi, k) {
  // sol1 352ms 30% 48.7MB 33%
  let hashMap = {}; let ans = []
  while (lo <= hi) {
    ans.push([lo, solve(lo, hashMap)])
    lo += 1
  }
  ans.sort((a,b) => {return a[1] - b[1]})
  return ans[k-1][0]  
};