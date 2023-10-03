'''
LeetCode 146 : LRU Cache
least recently used cache를 만들어라
만약 정해진 캐시 크기를 넘어선다면 lru를 삭제해야 한다.

# sol1
# O(1) O(n)
OrderedDict ordereddict라는 자료구조가 있다고 한다.
자바에서는 linkedhashmap이라고 한다.
이 구조를 사용해서 문제를 얼마나 간단히 풀 수 있는 지 알아보자.

# sol2 2099ms 36% 76.7MB 10%
O(1) O(n)
이제 더블 링크드 리스트를 통해 문제를 해결해보자. 
put과 get에 O(1)의 복잡도를 가진다.
한 가지 장점은 노드가 스스로 삭제될 수 있을 뿐만 아니라 add와 remove에 상수의 시간이 소모된다는 점이다.

'''
# sol1
# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity
        
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)

# sol2 2099ms 
class Node():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self._move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = Node()
            new_node.key = key; new_node.value = value
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    def _add_node(self, node):
        # head다음에 항상 새로운 node를 위치시킴
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
