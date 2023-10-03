/*
  2621 : sleep
  시간을 입력받아 기다리는 sleep 함수를 만들어라

  // sol1 55ms 50% 41.3MB 100%
  setTimeout 함수를 사용하여 밀리초 이후 해결되는 promise를 생성한뒤
  promise 함수가 만들어 질 때까지 기다리는 await를 사용
*/
async function sleep(millis) {
  // sol1
  await new Promise(resolve => setTimeout(resolve, millis))

  // sol2 awync await 사용하지 않고 하기
  return new Promise(resolve => {setTimeout(resolve, millis)})
}
