/*
 sol1 map, sol2 object
 object의 성능이 더 좋다.
 JSON.stringify()는 JS값이나 객체를 JSON 문자열로 변환한다.
 object는 JS에서 가장 기본 개념이다.
 const a = {}
 console.log(a instanceof Object) // true
 console.log(a instanceof Map) // false
 console.log(b instanceof Object) // true
 console.log(b instanceof Map) // true

 https://stackoverflow.com/questions/18541940/map-vs-object-in-javascript
 Map은 삽입 순서로 요소를 반복할 수 있다.
 Object는 킬 설정, 값 검색, 키 삭제 등을 할 수 있다는 점에서 Map과 유사하지만 객체는 프로토타입이 존재한다.
 따라서 기본키값이 맵에 저장되어 있다. 

 가장 다른 점은 오브젝트의 키는 문자열이지만 map에서는 어떠한 값이라도 될 수 있다.
 
*/
// function memoize(fn) {
//   // sol1 395ms 17% 108.9MB 9%
//   let d = new Map()
//   return function(...args) {
//     if (d.has(String(args))) {
//       return d.get(String(args))
//     } else {
//       d.set(String(args), fn(...args))
//       return d.get(String(args))
//     }
//   }
// }

function memoize(fn) {
  // sol2 327ms 88% 108.72MB 11%
  let d = {}
  return function(...args) {
    const key = JSON.stringify(args)
    if (key in d) {
      return d[key]
    } else {
      d[key] = fn(...args)
      return d[key]
    }
  }
}

// const sum = (a,b) => a+b
// const memoizedSum = memoize(sum)

// console.log(memoizedSum([2,2]))



// let c = new Map()
// c.set({a : 1}, 1)
// console.log(c.get({a : 1}))

// let o = {}
// o[{a : 1}] = {b : 1}
// console.log(o[{a : 1}])

let o = {}
let m = new Map()
console.log(o)
console.log(m)


