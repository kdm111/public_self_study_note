/*

Promise 객체
비동기 작업이 맞이할 완료 또는 실패와 값을 나타낸다.
Promise.all : 메서드는 모든 프로미스가 이행 된 뒤 이행하는 프로미스를 반환한다.
프로미스 결과값이 숫자로 이행되므로 더하여 반환한다.
*/
var addTwoPromises = async function(promise1, promise2) {
  // sol1 55ms 96% 42.08MB 46%
  const [val1, val2] = await Promise.all([promise1, promise2])
  return val1 + val2
};

console.log(addTwoPromises(Promise.resolve(2), Promise.resolve(2)))