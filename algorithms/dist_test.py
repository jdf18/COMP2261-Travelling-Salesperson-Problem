import random
random.seed(41)

from bisect import bisect_left
s, N = 0, 100
# s=0 - linear, s=1 - uniform
linear_selection = lambda x : (2-s)/N + 2*(x-1)*(s-1)/N/(N-1)
PROBABILITY_DIST = [sum(map(linear_selection, range(1, i+1))) for i in range(1, N+1)]

def test(n):
    for _ in range(n):
        x = random.random()
        i = bisect_left(PROBABILITY_DIST, x)
        yield (i)

x = list(test(20))
print(PROBABILITY_DIST)
for i in range(len(PROBABILITY_DIST)-2):
    print((PROBABILITY_DIST[i+1] - PROBABILITY_DIST[i]))
    # print((PROBABILITY_DIST[i+2] - PROBABILITY_DIST[i+1]) - (PROBABILITY_DIST[i+1] - PROBABILITY_DIST[i]))
print(x)
