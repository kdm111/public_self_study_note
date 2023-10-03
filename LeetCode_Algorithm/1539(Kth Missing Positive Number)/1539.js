var findKthPositive = function(arr, k) {
  // sol1 O(n), O(1) 79~87ms 66~54%

  if (k < arr[0]){
    return k
  }
  else{
    k -= arr[0]-1
  }
  for (let i=0; i < arr.length-1; i++){

    let diff = arr[i+1]-arr[i]-1

    if (k <= diff){
      return arr[i]+k
    }
    
    k -= diff
  }
  return arr[arr.length-1]+k
};

console.log(findKthPositive([2,3,4,7,11],5))