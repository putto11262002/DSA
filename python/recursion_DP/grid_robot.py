def get_path(grid: 'list[list[bool]]') -> 'list[tuple[int, int]]':
    if (grid is None or len(grid) < 1):
        return []
    path = list()
    failed_points = set()
    _get_path(len(grid) - 1, len(grid[0]) - 1, path, grid, failed_points)
    return path


def _get_path(r: int, c: int, path: 'list[tuple[int, int]]', grid, failed_points = set()):
    if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) or not grid[r][c]: 
        return False
    if (r, c) in failed_points: 
        return False
    
    if (r == 0 and c == 0) or _get_path(r - 1, c, path, grid, failed_points) or _get_path(r, c - 1, path, grid, failed_points): 
        path.append((r, c)) 
        return True
    failed_points.add((r, c))
    return False


grid = [
    [True, True, True, True],
    [False, False, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
]
path = get_path(grid)
print(path)

