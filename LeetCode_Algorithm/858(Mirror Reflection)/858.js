var mirrorReflection = function(p, q) {
  // sol1 65ms 90% 41.9Mb 58%
  if (q == 0)
    return 0
  let m = 1; let n = 1
  while (m * p != n * q) {
    n += 1
    m = parseInt(n * q / p)
  }
  if (n % 2 == 0) {
    return 2
  }
  if (m % 2 == 1) {
    return 1
  }
  return 0
};