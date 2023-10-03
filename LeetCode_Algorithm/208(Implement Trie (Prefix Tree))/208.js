var TrieNode = function() {
  this.word = false
  this.children = {}
}

var Trie = function() {
  // 314ms 40%
  this.root = new TrieNode()
};

Trie.prototype.insert = function(word) {
  let node = this.root
  for (let w of word) {
    if (node.children[w] == undefined) {
      node.children[w] = new TrieNode()
    }
    node = node.children[w]
  }
  node.word = true
};

Trie.prototype.search = function(word) {
  let node = this.root
  for (let w of word) {
    if (node.children[w] == undefined) {
      return false
    }
    node = node.children[w]
  }
  return node.word
};

Trie.prototype.startsWith = function(prefix) {
  let node = this.root
  for (let p of prefix) {
    if (node.children[p] == undefined) {
      return false
    }
    node = node.children[p]
  }
  return true
};
