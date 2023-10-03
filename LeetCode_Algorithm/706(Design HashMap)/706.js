var MyHashMap = function() {
  // 415ms 16%
  this.hashMap = {}
};

MyHashMap.prototype.put = function(key, value) {
this.hashMap[key] = value
};

MyHashMap.prototype.get = function(key) {
if (this.hashMap[key] != undefined) {
    return this.hashMap[key]
} else {
    return -1
}
};

MyHashMap.prototype.remove = function(key) {
  this.hashMap[key] = undefined
};
let map = new MyHashMap()
map.put(1,1)
map.put(1,2)
map.remove(1)
console.log(map.get(1))
