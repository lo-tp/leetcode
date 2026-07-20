from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        data=[1]
        should_reverse=False
        for v_idx in range(len(board)-1, -1, -1):
            if should_reverse:
                for h_idx in range(len(board[0])-1, -1, -1):
                    data.append(board[v_idx][h_idx])
            else:
                for h_idx in range(0, len(board[0])):
                    data.append(board[v_idx][h_idx])
            should_reverse=not should_reverse
        seen=set([1])
        q=deque([(1, 0)])
        target=len(board)**2
        while q:
            idx, step=q.popleft()
            if idx==target:
                return step
            for nxt_idx in range(idx+1, min(idx+7, target+1)):
                nxt_idx=nxt_idx if data[nxt_idx]==-1 else data[nxt_idx]
                if not nxt_idx in seen:
                    seen.add(nxt_idx)
                    q.append((nxt_idx, step+1))
        return -1

