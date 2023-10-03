class Heap {
  constructor() {
    this.heap = []
  }
  parent(idx) {
    return Math.floor((idx - 1) / 2)
  }
  leftChild(idx) {
    return (2 * idx + 1)
  }
  rightChild(idx) {
    return (2 * idx + 2)
  }
  hasleftChild(idx) {
    return (2 * idx + 1) < this.heap.length
  }
  hasrightChild(idx) {
    return (2 * idx + 2) < this.heap.length
  }
  heappush(num) {
    this.heap.push(num)
    let idx = this.heap.length-1
    let par = this.parent(idx)
    while (par >= 0 && this.heap[par] > this.heap[idx]) {
      this.swap(par, idx)
      idx = par
      par = this.parent(idx)
    }
  }
  heappop() {
    const ret= this.heap[0]
    this.heap[0] =  this.heap[this.heap.length-1]
    this.heap.pop()
    let idx = 0
    while (this.hasleftChild(idx)) {
      let small = this.leftChild(idx)
      if (this.hasrightChild(idx) && this.heap[small] >= this.heap[this.rightChild(idx)]) {
        small = this.rightChild(idx)
      }
      if (this.heap[idx] >= this.heap[small]) {
        this.swap(idx, small)
      } 
      idx = small
    }
    return ret
  }
  swap(par, idx) {
    let temp = this.heap[par]
    this.heap[par] = this.heap[idx]
    this.heap[idx] = temp
  }
}

var findKthLargest = function(nums, k) {
  // sol2 runtime error 5000개중 첫번째로 큰 수 찾기
  // let pivot = nums[Math.floor(Math.random()) * nums.length()]
  // let left = []; let mid = []; let right = []
  // for (let num of nums) {
  //   if (num < pivot) {
  //     left.push(num)
  //   } else if (num == pivot) {
  //     mid.push(num)
  //   } else {
  //     right.push(num)
  //   }
  // }
  // if (k < left.length()) {
  //   return findKthLargest(left, k)
  // } else if (k > mid.length()+right.length()) {
  //   return findKthLargest(right, k-mid.length()-right.length())
  // } else {
  //   return mid[0]
  // }

  // sol1 time limit exceeded 63565번째 큰 수 찾기
  //  let heap = new Heap(nums)
  //   for (let idx=1; idx < k; idx++) {
  //     heap.items.pop()
  //   } return heap.items[0]

  // 98ms 87% 50.8MB 71%
  let heap = new Heap()
  for (let num of nums) {
      heap.heappush(num)
      if (heap.heap.length > k) 
        heap.heappop()
  }
  return heap.heap[0]
};

// console.log(findKthLargest([4,2,3,5,1], 2))
console.log(findKthLargest([7,6,5,4,3,2,1]  ,5))
