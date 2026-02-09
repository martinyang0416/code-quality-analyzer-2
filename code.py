import bisect

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    end_times = []
    dp = []
    for s, e, p in jobs:
        idx = bisect.bisect_right(end_times, s) - 1
        current = p
        if idx >= 0:
            current += dp[idx]
        if dp:
            current = max(current, dp[-1])
        dp.append(current)
        end_times.append(e)
    return dp[-1] if dp else 0