var maxProfit = function(prices) {

  // sol1 O^2 시간 초과
  // var ans = 0
  // for (let buyDay in prices){
  //   for (let sellDay in prices){ // sellDay는 string
  //     if (Number(buyDay) < Number(sellDay)){ 
  //       // for in으로 인덱스를 뽑을 때 문자열로 뽑아져 나온다.
  //       // 따라서 9와 10의 비교는 9>10이 된다. console.log("10"<"9") console.log("10"<"3")
  //       // 따라서 Number로 형 변환을 해줌.
  //       let profit = prices[sellDay]- prices[buyDay]
  //       if (profit > ans){ans = profit}
  //     }
  //   }
  // }
  // return ans

  // sol2 92ms 82%보다 빠름
  var minPrice = 99999999999
  var ans = 0
  prices.forEach(function(price){
    if (price < minPrice){minPrice = price}
    else{
      let profit = price-minPrice
      if(profit>ans){ans = profit}
    }
  })
  return ans
};

console.log(maxProfit([1,2,4,2,5,7,2,4,9,0,9]))

