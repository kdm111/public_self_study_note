/*
함수, 배열, t가 주어진다. 캔슬 함수를 리턴하라.
tms의 시간이 흐른 뒤에 fn은 args를 활용한 값을 리턴한다.

여기에서 특별한 조건이 하나 붙는다.
함수 바깥에서 함수는 다음과 같이 호출된다.
const cancelTime = 50
const cancel = cancellable((x) => x * 5, [2], 20); // fn(2) called at t=20ms
setTimeout(cancel, cancelTime);
cancelTime이 t를 초과하였을 경우 함수는 아무것도 리턴해서는 안된다.


// 
우리는 함수가 setTimeout(함수, cancelTime) cancelTime이후에 함수가 취소되기를 원한다.


//
*/

var cancellable = function(fn, args, t) {
  // sol1

};

function foo(message) {
  console.log('1 wasn\'t cancelled')
  console.log('2 wasn\'t cancelled')
  console.log(message)
}

console.log(foo("bar"))