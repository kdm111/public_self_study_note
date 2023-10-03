var merge = function(intervals) {
  // sol1 O(nlogn) 177ms 37%
  if (intervals.length == 0) {return []}
  intervals.sort((a,b)=>{
    if(a[0] == b[0]) {
      return a[1]-b[1]
    } else {
      return a[0]-b[0]
    }
  })
  
  let i = 0; let ans = []
  while (i < intervals.length) {
    if (ans.length == 0 || intervals[i][0] > ans[ans.length-1][1]) {
      ans.push(intervals[i])
    } else {
      ans[ans.length-1][1] = Math.max(ans[ans.length-1][1], intervals[i][1])
    }
    i += 1
  }
  return ans
};

console.log(merge([[1,13],[2,6],[1,10],[15,18]]))