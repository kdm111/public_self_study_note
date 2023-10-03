var minMutation = function(startGene, endGene, bank) {
  // sol1 53ms 96% 42.2MB 25%
  if (bank.indexOf(endGene) < 0)
    return -1
  let graph = new Map()
  graph.set('A', ['C', 'G', 'T'])  
  graph.set('C', ['A', 'G', 'T'])
  graph.set('G', ['A', 'C', 'T'])
  graph.set('T', ['A', 'C', 'G'])
  let seen = new Set(); seen.add(startGene)
  let queue = [[startGene, 0]]
  while (queue.length) {
    [gene, cnt] = queue.shift()
    if (gene == endGene)
      return cnt
    for (let i = 0; i < 8; i++) {
      for (let c of graph[gene[i]]) {
        let newGene = gene.slice(0, i) + c + gene.slice(i+1, )
        if (!seen.has(newGene) && bank.indexOf(newGene) >= 0) {
          seen.add(newGene)
          queue.append([newGene, cnt+1])
        }
      }
    }
  }
  return -1
};