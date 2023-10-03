var createCounter = function(init) {
  presentCnt = init
  function increment () {
    return ++presentCnt
  } 
  function decrement() {
    return --presentCnt
  }
  function reset() {
    presentCnt = init
    return presentCnt
  }
  return {
    increment, decrement, reset
  }
};