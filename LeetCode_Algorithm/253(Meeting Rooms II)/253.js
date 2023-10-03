var minMeetingRooms = function(intervals) {
 // sol3 132ms 37% 44.7MB 47%2

    let startTime = []; let endTime = []
    for (let interval of intervals) {
      startTime.push(interval[0])
      endTime.push(interval[1])
    }
    startTime.sort((a,b) => {return a-b})
    endTime.sort((a,b) => {return a-b})
    let startPtr = 0; let endPtr = 0; let ans = 0
    while (startPtr < startTime.length) {
      if (startTime[startPtr] >= endTime[endPtr]) {
        ans -= 1
        endPtr += 1
      }
      ans += 1
      startPtr += 1
    }
    return ans
};