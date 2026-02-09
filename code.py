n = int(input())
t = input().strip()

s = []
index = 0
group_size = 1

while index < len(t):
    # Extract the group of current group_size
    group = t[index:index + group_size]
    # Append the first character of the group to s
    s.append(group[0])
    # Move to the next group
    index += group_size
    group_size += 1

print(''.join(s))