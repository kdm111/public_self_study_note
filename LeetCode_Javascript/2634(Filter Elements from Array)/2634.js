var filter = function(arr, fn) {
  // sol1 56ms 69% 41.6MB 83%
  // return arr.reduce((ret, x, idx) => {
  //   if (fn(x, idx)) {
  //     ret.push(x)
  //   }
  //   return ret
  // }, [])

  // sol2 49ms 94% 42.4MB 15%
  return arr.filter(fn)
};

console.log(filter([0,10,20,30], function(x) {return x > 10}))