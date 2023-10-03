var lastStoneWeight = function(stones) {
  // sol1 O(mnlogn), O(n) 77~102ms 67~27%
  // while (stones.length > 1){
  //   stones.sort(function(a,b){return a-b})
  //   const heavyStone = stones.pop()
  //   const lightStone = stones.pop()
  //   if (heavyStone-lightStone != 0){
  //     stones.push(heavyStone-lightStone)
  //   }
  // }
  // return stones.length > 0 ? stones[0] : 0

  // console.log(stones)

  // sol2
  // heap

  // sol3 O(n), O(n) 68~111ms 82~15%
  // counts

  // counts = new Array(Math.max(...stones)+1)
  counts = new Array(stones.reduce(function(a,b){
    return Math.max(a,b)
  })+1).fill(0)
  // counts = new Array(Math.max(...stones)+1)

  for (let weight of stones){
    counts[weight] += 1
  }
  var currWeight = 0
  for (let weight=counts.length-1; weight > 0; weight--)
  {
    if (currWeight == 0) 
    {
      if (counts[weight] % 2 == 1)
      {
        currWeight = weight
        counts[weight] = 0
      }
    }
    else {
      while (counts[weight] > 0) {
        counts[weight] -= 1
        if (currWeight-weight <= weight)
        {
          counts[currWeight-weight] += 1
          if (counts[weight] % 2 == 0)
          {
            currWeight = 0
          }
          else
          {
            currWeight = weight
          }
          counts[weight] = 0
          break;
        }
        else
        {
          currWeight -= weight
        }
        if (currWeight == 0)
        {
          currWeight = weight
        }
      }
    }
  }
  return currWeight
};

console.log(lastStoneWeight([1,3]))