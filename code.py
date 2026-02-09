def canCross(stones):
    if len(stones) < 2 or stones[0] != 0 or stones[1] != 1:
        return False
    stones_set = set(stones)
    from collections import defaultdict
    dp = defaultdict(set)
    dp[0].add(0)
    last_stone = stones[-1]
    for s in stones:
        if s not in dp:
            continue
        for k in dp[s]:
            for delta in (k-1, k, k+1):
                if delta <= 0:
                    continue
                next_pos = s + delta
                if next_pos in