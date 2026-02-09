# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read Ram's truth tasks
    tr = int(input())
    Tr = list(map(int, input().split()))
    tr_set = set(Tr)
    
    # Read Ram's dare tasks
    dr = int(input())
    Dr = list(map(int, input().split()))
    dr_set = set(Dr)
    
    # Read Shyam's truth tasks
    ts = int(input())
    Ts = list(map(int, input().split())) if ts > 0 else []
    
    # Read Shyam's dare tasks
    ds = int(input())
    Ds = list(map(int, input