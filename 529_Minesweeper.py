class Solution:
    def updateBoard(self, board, click):
        m = len(board)
        n = len(board[0])

        def deal_w_edge_cases(ne, m, n):
            return (min(max(0, ne[0]), m - 1), min(max(0, ne[1]), n - 1))

        def get_neighbors(cell_r, cell_c, m, n):
            right = (cell_r, cell_c + 1)
            left = (cell_r, cell_c - 1)
            up = (cell_r - 1, cell_c)
            down = (cell_r + 1, cell_c)
            up_right = (cell_r - 1, cell_c + 1)
            up_left = (cell_r - 1, cell_c - 1)
            down_right = (cell_r + 1, cell_c + 1)
            down_left = (cell_r + 1, cell_c - 1)
            all_neighbors = [right, left, up, down, up_right, up_left, down_right, down_left]
            neighbors_edge_cases = [deal_w_edge_cases(ne, m, n) for ne in all_neighbors]
            distinct_neighbors = set(neighbors_edge_cases) - {(cell_r, cell_c)}
            return list(distinct_neighbors)

        def get_nb_bombs(board, neighbors):
            n = 0
            for ne in neighbors:
                if board[ne[0]][ne[1]] == 'M':
                    n += 1
            return n

        def reveal(cell_r, cell_c, m, n, visited):
            # need a visited set. if already visited on se fait pas chier. sinn on
            # continue
            if (cell_r, cell_c) in visited:
                return
            else:
                # Base case
                if board[cell_r][cell_c] == 'M':
                    board[cell_r][cell_c] = 'X'
                    return
                if board[cell_r][cell_c] == 'E':
                    neighbors = get_neighbors(cell_r, cell_c, m, n)
                    nb_bombs_surrounding = get_nb_bombs(board, neighbors)
                    visited.add((cell_r, cell_c))

                    if nb_bombs_surrounding == 0:
                        board[cell_r][cell_c] = 'B'
                        for ne in neighbors:
                            reveal(ne[0], ne[1], m, n, visited)
                    else:
                        board[cell_r][cell_c] = str(nb_bombs_surrounding)
                        return

        visited = set()
        reveal(click[0], click[1], m, n, visited)
        return board