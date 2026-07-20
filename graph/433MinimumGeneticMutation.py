from collections import deque

class Solution:
    def havePath(a,b):
        sz=len(a)
        if sz!=len(b):
            return False
        dif=0
        for idx in range(0,sz):
            if a[idx]!=b[idx]:
                if dif:
                    return False
                dif+=1
        return True


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q=deque((startGene,0))
        seen=set()
        while q:
            gene, step=q.popleft()
            if gene==endGene:
                return step
            seen.add(gene)
            for b in bank:
                if b not in seen and havePath(gene, b):
                    q.append((b, step+1))
        return -1
