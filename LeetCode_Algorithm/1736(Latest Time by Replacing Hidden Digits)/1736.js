var maximumTime = (time) => {
  // sol1 97ms 48% 41.8MB 79%
  let t = time.split("")
  hour(t)
  minute(t)
  return t.join("")
};
var hour = (time) => {
  if (time[0] == '?') {
    if (time[1] == '?' || time[1] < '4') {
      time[0] = '2'
    } else {
      time[0] = '1'
    }
  }
  if (time[1] == '?') {
      if (time[0] < '2') {
          time[1] = '9'
      } else {
          time[1] = '3'
      }
  }
}
var minute = (time) => {
  if (time[3] == '?') {
    time[3] = '5'
  }
  if (time[4] == '?') {
    time[4] = '9'
  }
}