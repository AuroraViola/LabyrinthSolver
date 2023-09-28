import sys

import images

def _resolve(labirinth, x, y, endx, endy, values):
    if x == endx and y == endy:
        values.append((x, y))
        for value in values:
            labirinth[value[1]][value[0]] = (255, 0, 0)

    if 0 <= x < len(labirinth[0]) and 0 <= y < len(labirinth):
        if labirinth[y][x] == (255, 255, 255):
            values.append((x, y))
            labirinth[y][x] = (255, 255, 170)
            _resolve(labirinth, x+1, y, endx, endy, values.copy())
            _resolve(labirinth, x-1, y, endx, endy, values.copy())
            _resolve(labirinth, x, y+1, endx, endy, values.copy())
            _resolve(labirinth, x, y-1, endx, endy, values.copy())

def resolve(labirinth):
    resolved = labirinth.copy()
    _resolve(resolved, 188, 0, 244, 395, [])
    return resolved

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    labirinth = images.load("Labirinto2.png")
    labirinth = resolve(labirinth)
    images.save(labirinth, "result.png")
