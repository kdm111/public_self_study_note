function Node(val, next, random) {
  this.val = val;
  this.next = next;
  this.random = random; 
};

var getNode = (node) => {
 if (node) {
   if (!visited[node]) {
    //  visited[node] = new Node(node.val)
     visited.set(node, new Node(node.val))
   }
   return visited[node]
 }
 return null
}
var copyRandomList = function(head) {
   if (!head)
       return head
 let init = head
 let visited = new Map()
 newNode = new Node(head.val)
 while (init) {
  visited.set(init, new Node(init.val))
  init = init.next
 }
 init = head
 while (init) {
  visited.get(init).next = visited.get(init.next) || null
  visited.get(init).random = visited.get(init.random) || null
  init = init.next
 }
 return visited.get(head)
};