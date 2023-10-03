/*
  LeetCode 12 : Integer to Roman
  들어온 num을 로마 숫자 문자열러 바꾸는 함수 구현
  정해진 숫자 범위와 글자를 모두 배열로 구현
  가장 큰 숫자 부터 하나씩 비교해가며 num에서 제거한 뒤 해당하는 로마 글자를 하나씩 더해감
  sol1 : 딕셔너리 
  sol2 : 딕셔너리 제거
  sol3 : 나누기로 변경
*/
var intToRomanDict = function() {
  let hashMap = new Map()
  let symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
  let value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  for (let i=0; i < symbol.length; i++) {
    hashMap[value[i]] = symbol[i]
  }
  return hashMap
}

var intToRoman = function(num) {
  // sol1 T : 129ms 93% S : 49.6MB 28%
  // this.hashMap = intToRomanDict() 
  // let ans = ""
  // let value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  // let symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
  // let valIdx = value.length-1
  // while (num > 0) {
  //   if (value[valIdx] <= num) {
  //     num -= value[valIdx]
  //     ans += symbol[valIdx]
  //     valIdx++;
  //   }
  //   valIdx--;
  // }  
  // return ans

  // sol2 T : 175ms 81% S : 46.8MB 85%
  // 다시 생각해보니 굳이 맵을 사용할 필요가 없다.
  // let ans = ""
  // let value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  // let valIdx = value.length - 1
  // let symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
  // while (num > 0) {
  //   if (value[valIdx] <= num) {
  //     num -= value[valIdx]
  //     ans += symbol[valIdx]
  //     valIdx++;
  //   }
  //   valIdx--;
  // }
  // return ans


  // sol3 T : 122ms 96% S : 46.9MB 85%
  let ans = ""
  let value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  let valIdx = value.length
  let symbol = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
  while (--valIdx > -1) {
    let cnt = -1
    while (++cnt < parseInt(num / value[valIdx])) {
      ans += symbol[valIdx]
    }
    num %= value[valIdx]
  }
  return ans
};
intToRoman.prototype.hashMap = new Map()
console.log(intToRoman(1994))


