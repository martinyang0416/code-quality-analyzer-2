n, d = map(int, input().split())
values = list(map(int, input().split()))
times = list(map(int, input().split()))
tasks = list(zip(values, times))

def calculate_score(sorted_tasks, d):
    total = 0
    current_time = 0
    for v, t in sorted_tasks:
        finish_time = current_time + t
        total += v - d * finish_time
        current_time = finish_time
    return total

alice_sorted = sorted(tasks, key=lambda x: x[0])
bob_sorted = sorted(tasks, key=lambda x: -x[0])

alice_score = calculat