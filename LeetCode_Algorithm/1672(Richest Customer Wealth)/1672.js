var maximumWealth = function(accounts) {
  // 72ms 87%
  let maxWealth = 0
  for (let account of accounts) {
    let tempSum = account.reduce((acc, curr) => acc+curr, 0)
    if (maxWealth < tempSum) {
      maxWealth = tempSum
    }
  }  
  return maxWealth 
};