class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def visit(node, edges, path, not_visited_):
            if node in path:
                return len(path) - path[:-1].index(node)
            else:
                try:
                    not_visited_.remove(node)
                    if edges[node] == -1:
                        return -1
                    else:
                        return visit(edges[node], edges, path + [node], not_visited_)
                except:
                    return -1

        n = len(edges)
        # Only visit nodes that could be part of a cycle !
        to_visit = [n for n in range(n) if edges[n] != -1]
        not_visited = {e for e in to_visit}
        max_cycle_len = -1
        keep_going = True
        while keep_going and max_cycle_len < len(to_visit):
            if len(not_visited) != 0:
                start_point = max(not_visited)
                len_cycle = visit(start_point, edges, [], not_visited)
                max_cycle_len = max(max_cycle_len, len_cycle)
            else:
                keep_going = False

        return max_cycle_len