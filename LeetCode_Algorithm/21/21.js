function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

var mergeTwoLists = function(list1, list2) {
  // var list1_idx = 0
  // var list2_idx = 0
  // var ans = []
  // let idx = 0
  // while (list1_idx < list1.length && list2_idx < list2.length)
  // {
  //   if (list1[list1_idx] < list2[list2_idx]){
  //     ans[idx] = list1[list1_idx]; list1_idx += 1
  //   }
  //   else{
  //     ans[idx] = list2[list2_idx]; list2_idx += 1
  //   }
  //   idx += 1
  // } 

  // while (list1_idx < list1.length)
  // {
  //   ans[idx] = list1[list1_idx]; list1_idx += 1
  //   idx += 1
  // }

  // while (list2_idx < list2.length)
  // {
  //   ans[idx] = list2[list2_idx]; list2_idx += 1
  //   idx += 1
  // }
  // return ans

  // 보기에는 문제없음
  // if (!list1) {return list2}
  // if (!list2) {return list1}

  // var ans = new ListNode()
  // curr = ans
  // let list1_idx = 0; 
  // let list2_idx = 0;

  // while (list1_idx < list1.length && list2_idx < list2.length){
  //   if (list1[list1_idx] < list2[list2_idx]){curr.next = new ListNode(list1[list1_idx]); list1_idx += 1}
  //   else {curr.next = new ListNode(list2[list2_idx]); list2_idx += 1}
  //   curr = curr.next
  // }
  // while(list1_idx < list1.length){curr.next = new ListNode(list1[list1_idx]); list1_idx += 1; curr = curr.next}
  // while(list2_idx < list2.length){curr.next = new ListNode(list2[list2_idx]); list2_idx += 1; curr = curr.next}


  // return ans.next

  // 101ms
  ans = new ListNode()
  curr = ans

  while (list1 && list2){
    if (list1.val < list2.val){
      curr.next = list1
      list1 = list1.next
    }
    else{
      curr.next = list2
      list2 = list2.next
    }
    curr = curr.next
  }
  while (list1 !== null){
    curr.next = list1
    list1 = list1.next
    curr = curr.next
  }
  while (list2 !== null){
    curr.next = list2
    list2 = list2.next
    curr = curr.next
  }

  return ans.next
  
};  
var ans = mergeTwoLists([1,2,4], [1,3,4])

while (true){
  if (ans == null){break;}
  console.log(ans.val)
  ans = ans.next
}

