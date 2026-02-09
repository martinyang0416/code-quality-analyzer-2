def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    W = int(input[ptr])
    ptr +=1
    H = int(input[ptr])
    ptr +=1
    v = list(map(int, input[ptr:ptr+W-1]))
    ptr += W-1
    h = list(map(int, input[ptr:ptr+H-1]))
    ptr += H-1
    
    # Calculate the position to split vertically
    split_v = (W // 2) -1
    sum_v = sum(v[:split_v +1])
    
    # Calculate the position to split horizontally
    split_h = (H // 2) -1
    sum_h = sum(h[:split_h +1])
    
    t