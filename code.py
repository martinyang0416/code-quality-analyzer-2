def main():
    import sys
    f0_str = "What are you doing at the end of the world? Are you busy? Will you save us?"
    prefix_str = "What are you doing while sending \""
    s1_str = "\"? Are you busy? Will you send \""
    s2_str = "\"?"
    
    q = int(sys.stdin.readline())
    res = []
    
    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        if n == 0:
            if k > len(f0_str):
                res.append('.')
            else:
                res.app