var eraseOverlapIntervals = function(intervals) {
  // sol1 176ms 99% 73MB 98%
  if (!intervals || intervals.length == 0) {return 0} 
  intervals.sort((a,b) => {
    return a[1] - b[1]
  })
  let cnt = 1; let end = intervals[0][1] 
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] >= end) {
      end = intervals[i][1]
      cnt += 1
    }
  }
  return intervals.length - cnt
};

console.log(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))