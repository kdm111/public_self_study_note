var daysBetweenDates = function(date1, date2) {
  //sol1 78ms 79%
  // Date 모듈 사용
  // Date.prototype.getTime()은 1970년 1월 1일 00:00:00으로 부터 경과 시간을 밀리초 단위로 보여준다.

  // let arr1 = date1.split('-')
  // let arr2 = date2.split('-')  
  // let time1 = new Date(arr1[0], arr1[1], arr1[2])
  // let time2 = new Date(arr2[0], arr2[1], arr2[2])
  let mSec1 = new Date(date1).getTime()
  let mSec2 = new Date(date2).getTime()

  // 밀리초 단위로 반환하므로
  // 하루를 밀리초 단위로 나타내야 한다.
  let daySec = 1000 * 60 * 60 * 24
  let ans = Math.abs(mSec1-mSec2) / daySec
  return ans
};

console.log(daysBetweenDates("2020-01-15", "2020-01-16"))