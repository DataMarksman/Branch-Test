dr = [-1, 0, 1, 0]  # 북 동 남 서
dc = [0, 1, 0, -1]

r, c = map(int, input().split())
start, end, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
# print(room)
visited = set()
d = 0
while True:
    if room[start][end] == 0:
        room[start][end] = 7
        visited.add((start, end))

    for k in range(1, 5):
        if room[start+dr[(d+3*k)%4]][end+dc[(d+3*k)%4]] == 0:
            start = start+dr[(d+3*k)%4]
            end = end+dc[(d+3*k)%4]
            d = (d+3*k)%4
            break
    else:
        start = start + dr[(d + 2) % 4]
        end = end + dc[(d + 2) % 4]
        if 0 < start < r-1 and 0 < end < c-1 and room[start][end] != 1:
            pass
        else:
            break
print(len(visited))