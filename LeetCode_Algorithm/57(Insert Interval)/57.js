var insert = function(intervals, newInterval) {
  // sol1 92ms 72%
  let newStart = newInterval[0]; let newEnd = newInterval[1]
  let idx = 0; let ans = []

  while (idx < intervals.length && newStart > intervals[idx][0]) {
    ans.push(intervals[idx])
    idx += 1
  }
  if (ans.length == 0 || ans[ans.length-1][1] < newStart) {
    ans.push(newInterval)
  } else {
    ans[ans.length-1][1] = Math.max(ans[ans.length-1][1], newEnd)
  }
  while (idx < intervals.length) {
    let start = intervals[idx][0]; let end = intervals[idx][1]
    if (ans[ans.length-1][1] < start) {
      ans.push([start, end])
    } else {
      ans[ans.length-1][1] = Math.max(ans[ans.length-1][1], end)
    }
    idx += 1
  }
  return ans
};

console.log(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))