function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}
var makeTree = function (lst, idx) {
  if (idx > lst.length - 1) {
    return null;
  }
  let root = new TreeNode(lst[idx]);
  root.left = makeTree(lst, 2 * idx + 1);
  root.right = makeTree(lst, 2 * idx + 2);
  return root;
};
var makeGraph = function (node, graph) {
  // js의 key값은 스트링이다.
  // https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Keyed_collection
  // Object는 문자열을 값에 매핑하는 데 사용되고 Map은 모든 값을 가질 수 있다.
  // Map에 node를 매핑하려고 했는데 [Object Object]라는 결과값이 나왔음
  // Object를 Map의 key로 매핑할 경우 [object Object]라는 스트링으로 매핑이 되기 때문에 사용할 수 없음
  // graph의 key 값을 node의 val 값으로 사용
  if (graph[node.val] == undefined) {
    graph[node.val] = [];
  }
  if (node.left && node.left.val) {
    graph[node.val].push(node.left);
    if (graph[node.left.val] == undefined) {
      graph[node.left.val] = [node];
    }
    makeGraph(node.left, graph);
  }
  if (node.right && node.right.val) {
    graph[node.val].push(node.right);
    if (graph[node.right.val] == undefined) {
      graph[node.right.val] = [node];
    }
    makeGraph(node.right, graph);
  }
};
var solve = function (target, graph, k) {
  console.log(target);
  if (target == null || visited.indexOf(target.val) > -1 || k < 0) {
    return;
  }
  if (k == 0) {
    ans.push(target.val);
    return;
  }
  visited.push(target.val);
  for (let idx in graph[target.val]) {
    solve(graph[target.val][idx], graph, k - 1);
  }
};
var par = function (node, par) {
  if (node) {
    node.par = par;
    par(node.left, node);
    par(node.right, node);
  }
};
var distanceK = function (root, target, k) {
  // sol1 190ms 5%
  // if (!root) {
  //   return []
  // }
  // let graph = new Map(); visited = []; ans = []
  // makeGraph(root, graph)
  // solve(target, graph, k)
  // return ans

  // sol2 98ms 62%
  // par 속성을 추가한 뒤 queue로 나눔
  TreeNode.prototype.par = null;
  if (!root) {
    return [];
  }
  makepar(root, null);

  let queue = [[target, k]];
  let visited = new Set().add(target);

  while (queue.length) {
    [node, k] = queue.shift();
    if (k == 0) {
      ans = [];
      if (node) {
        ans.push(node.val);
      }
      for (let [node, k] of queue) {
        if (node && k == 0) {
          ans.push(node.val);
        }
      }
      return ans;
    }
    for (let [temp, cnt] of [
      [node.left, k - 1],
      [node.right, k - 1],
      [node.par, k - 1],
    ]) {
      if (temp && !visited.has(temp)) {
        visited.add(temp);
        queue.push([temp, cnt]);
      }
    }
  }
  return [];
};

let root = makeTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], 0);
let target = root.left;
console.log(distanceK(root, target, 2));
