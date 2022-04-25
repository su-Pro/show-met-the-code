import collections

N, n = int(1e3 + 5), int(input())
# pre_state 存储的是右哪个状态转移过来的
g, pre_state = [list(input().split())
                for x in range(n)], [[-1] * N for x in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def isok(
    x, y): return 0 <= x < n and 0 <= y < n and pre_state[x][y] == -1 and g[x][y] == '0'


def bfs():
    que = collections.deque()
    que.append((0, 0))
    pre_state[0][0] = (-1, -1)

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if not isok(nx, ny):
                continue
            pre_state[nx][ny] = (x, y)
            que.append((nx, ny))


bfs()


def custom_print():
    path = []
    x, y = n - 1, n - 1
    while x != -1 and y != -1:
        path.append((x, y))
        x, y = pre_state[x][y]
    for pos in path[::-1]:
        print(*pos)


custom_print()
