class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
class Trie:
    # Trie 자료구조
    # prefix tree data structure
    # 문자열 세트에서 키 검색에 사용된다.
    # 자동 완성, 맞춤법 체크, ip routing 등등에 사용된다.
    # 밸런스드 트리 해쉬 테이블 같은 자료구조가 있어 문자열 세트에서 단어를 검색할 수 있다.
    # 해쉬 테이블이 O(1)으로 찾지만 Trie가 필요한 이유는
    # 접두사에 맞는 모든 키를 찾아낸다.
    # 사전 순으로 문자열 세트를 나열하는 데 사용한다.
    # 또한 해쉬 테이블의 크기가 커질 수록 해쉬 충돌이 발생하고 검색 시간 복잡성이 O(n)으로 증가하기 때문이다.
    # trie는 해쉬 테이블보다 더 적은 공간을 사용할 수 있다.
    # 265ms 55%
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 루트를 가져옴
        node = self.root
        # 글자를 돌면서 키가 존재하는 지 확인
        for w in word:
            # 키 존재하지 않다면 
            if w not in node.children:
                # 글자로 키를 넣고 노드를 값으로 넣어줌 
                node.children[w] = TrieNode()
            # 노드를 그 키값으로 이동
            node = node.children[w]
        # 노드의 단어를 True값으로 변경
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.word


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
        
