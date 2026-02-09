import sys

def main():
    n = int(sys.stdin.readline())
    dp = [[-float('inf')] * 26 for _ in range(26)]
    
    for _ in range(n):
        name = sys.stdin.readline().strip()
        if not name:
            continue  # handle empty lines if any
        s = ord(name[0]) - ord('a')
        e = ord(name[-1]) - ord('a')
        l = len(name)
        
        new_trans = {}
        
        # Standalone case
        key = (s, e)
        if key in new_trans:
            if l > new_trans[key]:
 