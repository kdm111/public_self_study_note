var validMountainArray = function(arr) {
  // sol1 83ms 43% 44.9MB 30%
  let i = 0
  while (i < arr.length-1 && arr[i] < arr[i+1])  
    i++;
  if (i ==0 || i == arr.length-1)
    return false
  while (i < arr.length-1 && arr[i] > arr[i+1])
    i++;
  return i == arr.length-1
};