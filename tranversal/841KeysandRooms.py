class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen, stack = set(), [0]
        while stack:
            k = stack.pop()
            if k not in seen:
                seen.add(k)
                stack.extend(rooms[k])
        return len(seen) == len(rooms)
