'''
LeetCode 705 : Design HashSet
해쉬셋 만들기

# sol1 139ms 99% 18.8MB 62%
내장 해쉬셋 사용

# sol2
내장 해쉬셋을 이용하지 않고 해쉬셋에 대한 자료구조에 대한 이해를 돕는 문제
두 가지가 필요하다. 해쉬함수와 충돌처리
해쉬 함수는 주어진 값을 저장할 주소를 할당한다. 각각의 고유값이 고유한 해쉬값을 가진다.
충돌 처리 : 해쉬함수는 공간 A에 해당 여러 값이 공간의 동일한 값으로 매핑될 수 있다.이것을 충돌이라 한다.
충돌 발생 시 
sol1 동일한 해쉬 키에 대해 버킷에 보관한다.
sol2 충돌이 있을 때마다 빈 슬롯을 찾을 때까지 공간을 계속 탐색한다.
sol3 두 개의 해쉬함수를 사용하고 충돌이 적은 주소를 선택한다.
여기서는 sol1을 따른다.
기본 저장소는 array이고 각 요소 bucket은 실제 값을 저장한다.
키가 주어지면 해쉬 함수를 통해 value를 통해 값에 대한 키를 생성한다. 생성된 키는 버킷을 찾기 위한 인덱스에 사용된다.

해쉬함수의 기본은 modulo 연산자이다. hashval = key % base여기서 base는 해쉬셋 끝에 있는 버킷 수를 결정한다.
버킷이 많을 수록 충돌이 일어날 확률이 낮다.
일반적으로 나눗셈을 사용하므로 소수를 base의 길이를 구하겠다.
필요한 공간이 커지기에 잘 선택해야 한다.
linked list를 활용해서 자료구조를 만든다.
100000까지 값이 들어올 수 있으므로 100000 sqrt의 값인 316.2이므로 317로 base의 길이를 구함

'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyHashSet:

    def __init__(self):
        # sol1
        # self.map = {}
        # sol2
        self.base = 317
        self.bucket = [None] * self.base

    def add(self, key: int) -> None:
        # sol1
        # self.map[key] = True
        
        # sol2
        head = self.bucket[key % self.base]
        while head and head.val != key:
            head = head.next
        head = Node(key)

    def remove(self, key: int) -> None:
        # sol1
        # if key in self.map:
        #     del self.map[key]
        
        # sol2
        curr = self.bucket[key % self.base]
        curr_next = curr.next
        while curr_next and curr_next.val != key:
            curr = curr.next
            curr_next = curr.next
        curr_next = curr_next.next
        curr.next = curr_next
            
    def contains(self, key: int) -> bool:
        # sol1
        # return key in self.map

        # sol2
        curr = self.bucket[key % self.base]
        while curr and curr.val != key:
            curr = curr.next
        return not curr or curr.val == key



    