var toHex = function(num) {
  // sol1 66ms 48% 41.9MB 52%
  if (num == 0) {return "0"}
  let hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
  let ans = ""
  while (num != 0) {
    ans = hex[num & 15] + ans
    num = num >>> 4
  }
  return ans
};

console.log(toHex(-1))