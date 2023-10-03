/*
1. 함수가 만들어 질 때 함수를 선언하여 리턴할 수 있다.
2. error를 발생시킬 때 error 객체를 사용하여 안에 메시지를 담아 리턴할 수 있다.
throw new Error("message")
3. 

*/
var expect = function(val) {
  // sol1 51ms 90% 41.4MB 92%
  function toBe(val2) {
    if (val === val2) {
      return true
    } else {
      throw new Error("Not Equal");
    }
  }
  function notToBe(val2) {
    if (val !== val2) {
      return true;
    } else {
      throw new Error("Equal");
    }
  }
  return {
    toBe, notToBe
  }
};

// console.log(expect(5).toBe(null))
console.log(expect(5).toBe(5))
// console.log(expect(5).toBe('5'))
console.log(expect(5).notToBe('5'))
console.log(expect(5))