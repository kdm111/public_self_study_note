var busyStudent = function(startTime, endTime, queryTime) {
  // sol1 95ms 45% 42.4MB 14%
  // O(n) O(1)
  let ans = 0
  for (let i=0; i < startTime.length; i++) {
    if (endTime[i]>= queryTime && queryTime >= startTime[i]) {
      ans += 1
    }
  }  
  return ans
};