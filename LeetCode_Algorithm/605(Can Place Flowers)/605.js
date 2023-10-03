var canPlaceFlowers = function(flowerbed, n) {
  // sol1  O(n) 64~95ms 98~67%
  for (let i=0; i < flowerbed.length; i++){
    if (flowerbed[i] == 1){ continue }
    let emptyLeftPlot = (i==0) || (flowerbed[i-1] == 0)
    let emptyRightPlot = (i==flowerbed.length-1) || (flowerbed[i+1] == 0)

    if (emptyLeftPlot && emptyRightPlot){
      flowerbed[i] = 1
      n -= 1
    }  
  }
  // console.log(flowerbed, n)
  // return (n <= 0) ? true : false
  return (n <= 0) && true || false
};
console.log(canPlaceFlowers([1,0,0,0,1],2))