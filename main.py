import bisect
import sys

p = sorted(map(int, input().split()))
t = sorted(map(int, input().split()))
c = int(input())
r = 250
n = len(p)
m = len(t)

if n == 0:
    print(0)
    sys.exit()
if m == 0:
    print("-1")
    sys.exit()
if c <= 2 * r:
    print(t[0])
    sys.exit()


def coverage(c: int, l: list[int], s: int, e: int) -> tuple[int, int]:
    if s >= 0:
        start = bisect.bisect_left(l, s)
    else:
        start = bisect.bisect_left(l, s % c)
    if e < c:
        end = bisect.bisect_right(l, e)
    else:
        end = bisect.bisect_right(l, e % c)
    if s >= 0 and e < c:
        return start % len(l), end - start
    n = len(l)
    return start % n, (n - start) + end


t1 = dict()
for ti in t:
    s, l = coverage(c, p, ti - 250, ti + 250)
    if t1.get(s) is None:
        t1[s] = []
    t1[s].append((l, ti))
a = 0  # anchor: index of the first check post
INF = float("inf")
best = (INF, [])

for s0 in t1:
    for l0, t0 in t1[s0]:
        end = s0 + l0
        if end < n:
            covered = s0 <= a < end
        else:
            covered = a >= s0 or a < end - n
        if not covered:
            continue

        # dp[q] = fewest transmitters covering the q posts following s0
        dp = [INF] * (n + 1)
        parent: list = [None] * (n + 1)
        dp[0] = 0
        for q in range(n):
            if dp[q] == INF:
                continue
            for l2, t2 in t1.get((s0 + q) % n, []):
                if q + l2 <= n and dp[q] + 1 < dp[q + l2]:
                    dp[q + l2] = dp[q] + 1
                    parent[q + l2] = (q, t2)
        if dp[n] < INF and dp[n] < best[0]:
            path = []
            pos = n
            while pos > 0:
                pos, t = parent[pos]
                path.append(t)
            best = (dp[n], path[::-1])

if best[1] == []:
    print("-1")
else:
    print(len(best[1]))
    print(" ".join(map(str, best[1])))
