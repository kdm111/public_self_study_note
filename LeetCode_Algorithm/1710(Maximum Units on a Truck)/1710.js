var maximumUnits = function(boxTypes, truckSize) {
  // sol1 O(nlong), O(1) 72~125ms 97~40%
  boxTypes.sort(function(a,b){
    return b[1]-a[1]
  })

  var units = 0
  for (let box of boxTypes){
    let boxNum = Math.min(box[0], truckSize)
    units += (boxNum * box[1])
    truckSize -= boxNum
    if (truckSize == 0) {break}
  }
  return units

};

console.log(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))