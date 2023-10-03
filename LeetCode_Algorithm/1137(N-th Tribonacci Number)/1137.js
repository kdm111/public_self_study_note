var tribonacci = function(n) {
  // sol1 59ms 44% 41.4MB 85%
  if (n == 0) {return 0}
  let a = 0; let b = 1; let c = 1
  for (let _ = 0; _ < n - 2; _++) {
      let temp = c
      c = a+b+c
      let temp2 = b
      b = temp
      a = temp2        
  }
  return c
};