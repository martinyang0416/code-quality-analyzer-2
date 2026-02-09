T = int(input())
for _ in range(T):
    n_activities, origin = input().split()
    n_activities = int(n_activities)
    total = 0
    for _ in range(n_activities):
        activity = input().split()
        if activity[0] == 'CONTEST_WON':
            rank = int(activity[1])
            bonus = max(0, 20 - rank)
            total += 300 + bonus
        elif activity[0] == 'TOP_CONTRIBUTOR':
            total += 300
        elif activity[0] == 'BUG_FOUND':
            severity = int(activity[1])
