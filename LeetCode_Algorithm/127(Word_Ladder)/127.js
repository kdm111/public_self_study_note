var ladderLength = function(beginWord, endWord, wordList) {
  // sol1 2164ms 11.6%
  // let graph = new Map()
  // for (let word of wordList) {
  //   for (let idx in word) {
  //     let temp = [...word]; temp[idx] = '_';
  //     let key = temp.join('')
  //     if (graph[key] == undefined) {
  //       graph[key] = [word]
  //     } else {
  //       graph[key].push(word)
  //     }
  //   }
  // }
  // let queue = [[beginWord, 0]]; let visited = []
  // while (queue.length > 0) {
  //   let temp = queue.shift()
  //   let word = temp[0]; let cnt = temp[1]
  //   if (word == endWord) {
  //     return cnt+1
  //   }
  //   if (visited.indexOf(word) > -1) {
  //     continue
  //   }
  //   visited.push(word)
  //   for (let idx in word) {
  //     let lst_word = [...word]; lst_word[idx] = '_';
  //     let key_word = lst_word.join('')
  //     if (graph[key_word] != undefined) {
  //       for (let temp_word of graph[key_word]) {
  //         queue.push([temp_word, cnt+1])
  //       }
  //     }
  //   }
  // }
  // return 0

  // sol2 169ms 86% 63.5MB 9%
  let graph = new Map()
  for (let word of wordList) {
    for (let i = 0; i < word.length; i++) {
      let key = word.slice(0, i) + '*' + word.slice(i+1, )
      if (graph[key] == undefined)
        graph[key] = []
      graph[key].push(word)
    }
  }
  let queue = [[beginWord, 1]]; let seen = new Set([beginWord])
  while (queue.length) {
    let [word, cnt] = queue.shift()
    if (word == endWord)
      return cnt
    for (let i = 0; i < word.length; i++) {
      let key = word.slice(0, i) + '*' + word.slice(i+1, )
    if (graph[key] != undefined) {
        for (let w of graph[key]) {
            if (!seen.has(w)) {
              seen.add(w)
              queue.push([w, cnt+1])
            }
        }
      }
    }
 }
 return 0
};


console.log(ladderLength("hit", "dog", ["hot","dog","dot"]))