class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        sz = len(grid)

        def generate(v, h, size):
            is_leaf = True
            for v_idx in range(v, v + size):
                for h_idx in range(h, h + size):
                    if grid[v_idx][h_idx] != grid[v][h]:
                        is_leaf = Fales
                        break
                if not is_leaf:
                    break
            if is_leaf:
                return Node(val=grid[v][h], isLeaf=True)
            size //= 2
            top_left = generate(v, h, size)
            top_right = generate(v, h + size, size)
            bottom_left = generate(v + size, h, size)
            bottom_right = generate(v + size, h + size, size)
            return Node(
                val=grid[v][h],
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right,
            )

        return generate(0, 0, sz)
