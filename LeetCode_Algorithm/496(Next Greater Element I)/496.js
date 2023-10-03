class Stack {
  constructor() {
    this._arr = []
  }
  push(item) {
    this._arr.push(item)
  }
  pop() {
    return this._arr.pop();
  }
  peek(){
    return this._arr[this._arr.length-1]
  }
}
var nextGreaterElement = function(nums1, nums2) {
  // sol1 O(mn), O(n) 94~125ms 47~13%
  // hashMap을 사용해서 처음부터 끝까지 더 서치 안해도 됨
  // hashMap = new Map()
  // for (let i=0; i < nums2.length; i++){
  //   hashMap.set(nums2[i], i)
  // }
  // var ans = new Array()
  // for (let num1 of nums1){
  //   var temp = -1
  //   for (let idx=hashMap.get(num1)+1; idx<nums2.length; idx++){
  //     if (num1 < nums2[idx]) {temp = nums2[idx]; break;}
  //   }
  //   ans.push(temp)
  // }
  // return ans

  // sol2 87~92ms 59~50%

  var stack = new Stack()
  var hashMap = new Map()
  for (let idx=0; idx < nums2.length; idx++){
    if (stack.length == 0 || nums2[idx] < stack.peek()){
      stack.push(nums2[idx]); continue
    }
    else if (stack.peek() == nums2[idx]){
      continue
    }
    else {
      while (stack.length != 0){
        if (stack.peek() < nums2[idx]){
          hashMap.set(stack.pop(), nums2[idx])
        }
        else{
          break
        }
      }
      stack.push(nums2[idx])
    }
  }

  while (stack._arr.length > 0){
    hashMap.set(stack.pop(), -1)
  }

  for (let idx=0; idx<nums1.length; idx++){
    nums1[idx] = hashMap.get(nums1[idx]) 
  }
  return nums1
};

console.log(nextGreaterElement([4,1,2], [1,3,4,2]))