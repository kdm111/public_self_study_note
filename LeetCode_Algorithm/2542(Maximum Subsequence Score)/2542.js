class Heap {
  constructor() {
    this.heap = []
  }
  parent(idx) {
    return Math.floor((idx-1) / 2)
  }
  heappush(num) {
    this.heap.push(num)

    let idx = this.heap.length-1
    while (this.heap[this.parent(idx)] && this.heap[this.parent(idx)] > this.heap[idx]) {
      let temp = this.heap[this.parent(idx)]
      this.heap[this.parent(idx)] = this.heap[idx]
      this.heap[idx] = temp
      idx = this.parent(idx)
    }
  }
  remove() {
    const ret = this.heap.shift()
    let temp = this.heap[0]
    this.heap[0] = this.heap[this.heap.length-1]
    this.heap[this.length-1] = temp
    let idx = 0
    while (this.heap[2*idx+1]) {
      let small = 2*idx+1
      if (this.heap[2*idx+2] && this.heap[2*idx+2] < this.heap[2*idx+1]) {
        small = 2*idx+2
      }
      if (this.heap[idx] < this.heap[small]) {
        break ;
      } else {
        let temp = this.heap[idx]
        this.heap[idx] = this.heap[small]
        this.heap[small] = temp
      }
      idx = small
    }
    return ret
  }
  peek() {
    if (this.heap.length === 0) {
      return null
    }
    return this.heap[0]
  }
}
var maxScore = function(nums1, nums2, k) {
  // sol1
  let heap = new Heap(); let total = 0; let ans = 0
  const nums = []
  for (let i = 0; i < nums1.length; i++ ){
    nums.push([nums1[i], nums2[i]])
  }
  nums.sort((a,b) => b[1] - a[1])
  for (let i = 0; i < nums.length; i++) {
    heap.heappush(nums[i][0])
    total += nums[i][0]
    if (heap.heap.length > k) {
      total -= heap.remove()
    }
    if (heap.heap.length == k) {
      ans = Math.max(ans, total * nums[i][1])
    }
  }
  return ans
};
console.log(maxScore([1,3,3,2], [2,1,3,4], 3))
console.log(maxScore([4,2,3,1,1], [7,5,10,9,6], 1))
