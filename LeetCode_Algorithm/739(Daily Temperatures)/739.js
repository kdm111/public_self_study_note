var dailyTemperatures = function(temperatures) {
  // sol1 322ms 76% 71.8MB 19%
  let stack = []
  let ans = new Array(temperatures.length).fill(0)
  for (let i=0; i <temperatures.length; i++) {
    while (stack.length > 0 && stack[stack.length-1][1] < temperatures[i]) {
      temp = stack.pop()
      let day = temp[0];
      ans[day] = i - day
    }
    stack.push([i, temperatures[i]])
  }
  return ans
};