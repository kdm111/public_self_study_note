var map = function(arr, fn) {
  // sol1
  // return arr.map((el) => {return fn(el)})

  // sol2 69ms 6% 41.8MB 67%
  return arr.reduce((ret, el, idx) => {
    ret.push(fn(el, idx))
    return ret
  }, [])
};
console.log(map([1,2,3], function(x){return x+1}))