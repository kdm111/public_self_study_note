// map오브젝트 사용 안할 시 70ms 절약
// const romanToIntMap = new Map()
// romanToIntMap.set('I', 1)
// romanToIntMap.set('V', 5)
// romanToIntMap.set('X', 10)
// romanToIntMap.set('L', 50)
// romanToIntMap.set('C', 100)
// romanToIntMap.set('D', 500)
// romanToIntMap.set('M', 1000)

const romanToIntMap = {
  "I" : 1,
  "V" : 5,
  "X" : 10,
  "L" : 50,
  "C" : 100,
  "D" : 500,
  "M" : 1000
}

var romanToInt = function(s) {
  // 186ms  
  // var len = s.length
  // var ans = romanToIntMap.get(s[len-1])

  // for (let i = len-2 ;i >= 0;i--){
  //   let num = romanToIntMap.get(s[i])
  //   let prevNum = romanToIntMap.get(s[i+1])
  //   num < prevNum ? ans -= num : ans += num
  // }

  // 124ms 93.7% 보다 빠름 아마도 js 보다 파이썬이 더 빨리 풀리는 문제인듯
  var strArr = s.split('')
  var ans = 0
  for (let i = 0; i < strArr.length; i++){
    const curr = romanToIntMap[strArr[i]]
    const next = romanToIntMap[strArr[i+1]]
    curr < next ? ans -= curr : ans += curr
  }

  return ans
};

console.log(romanToInt("III"))