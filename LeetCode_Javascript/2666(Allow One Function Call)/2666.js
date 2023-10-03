/*
  55ms 77% 41.9MB 45%
  미리 값을 생성한 뒤 함수를 리턴하여 원하는 값을 리턴하고 값을 수정
*/
var once = function(fn) {
  let notOpen = true
  return function(...args){
    if (notOpen) {
      notOpen = false
      return fn(...args)
    } else {
      return
    }
  }
};

let fn = (a, b, c) => (a + b + c)
let onceFn = once(fn)
console.log(onceFn(1,2,3))
console.log(onceFn(1,2,3))

