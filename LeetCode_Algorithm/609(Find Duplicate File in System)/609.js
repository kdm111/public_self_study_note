var findDuplicate = function(paths) {
  // sol1 129ms 91% 57.4MB 80%
  let hashMap = new Map()
  for (let path of paths) {
    path = path.split(" ")
    let addr = path[0]
    for (let i =1 ;i < path.length; i++) {
      let content = path[i].slice(path[i].lastIndexOf('(')+1, path[i].lastIndexOf(')'))
      let dir = addr + '/' + path[i].slice(0, path[i].lastIndexOf('('))
      if (hashMap[content]) {
        hashMap[content].push(dir)
      } else {
        hashMap[content] = [dir]
      }
    }
  }
  let ans = []
  for (let [k,v] of Object.entries(hashMap)) {
    if (v.length > 1) {
      ans.push(v)
    }
  }
  return ans
};

console.log(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))