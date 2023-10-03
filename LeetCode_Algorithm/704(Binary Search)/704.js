var search = function(nums, target) {
    // sol 78ms 73%보다 빠름
  var left = 0
  var right = nums.length-1

  while(left<=right){
    console.log((right-left)/2) // 실수형으로 표현
    let mid = left + parseInt((right-left)/2) // 몫을 구할 때는 parseInt()를 사용하여 정수로 변경
    console.log(mid)
    if (nums[mid]== target) {
      return mid 
    }
    if (nums[mid] < target){
      left = mid+1
    }else{
      right = mid-1
    }
  }
  return -1

};

console.log(search([-1,0,3,5,9,12], 9))