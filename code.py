L, m = map(int, input().split())
# Discard the list of checkpoints as they are not needed
input()
s, t = map(int, input().split())
distance = abs(t - s)
min_distance = min(distance, L - distance)
print(min_distance)