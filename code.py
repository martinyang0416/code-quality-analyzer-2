def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    K = int(input[idx])
    idx += 1
    D = int(input[idx])
    idx += 1

    times = []
    for _ in range(N):
        time_str = input[idx]
        idx += 1
        hh, mm, ss = map(int, time_str.split(':'))
        t = hh * 3600 + mm * 60 + ss
        times.append(t)

    events = []
    for t in times:
        start = t
        end = t + D
        events.append((start, 1))
      