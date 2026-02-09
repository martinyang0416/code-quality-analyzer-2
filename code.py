import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    w = int(data[idx+1])
    k = int(data[idx+2])
    idx +=3
    a = list(map(int, data[idx:idx+n]))
    idx +=n
    t = list(map(int, data[idx:idx+n]))
    saved = []
    for ti in t:
        saved_i = ti - (ti +1)//2
        saved.append(saved_i)
    
    max_pleasure = 0
    
    for x in range(n):
        current_sum_t = 0
        current_sum_a = 0
        heap =