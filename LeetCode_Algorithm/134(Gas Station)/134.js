var canCompleteCircuit = function(gas, cost) {
  // sol2 83ms 79% 50.2MB 84%
  let totalGas = 0; let currGas = 0; let ans = 0
  for (let i=0; i < gas.length; i++) {
    totalGas += (gas[i] - cost[i])
    currGas += (gas[i] - cost[i])
    if (currGas < 0) {
      currGas = 0;
      ans += 1
    }
  }
  if (totalGas < 0)
    return -1
  return ans
};