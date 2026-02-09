def getHappyString(n: int, k: int) -> str:
    happy = []
    
    def backtrack(s):
        if len(s) == n:
            happy.append(s)
            return
        last_char = s[-1] if s else ''
        for c in ['a', 'b', 'c']:
            if c != last_char:
                backtrack(s + c)
    
    backtrack('')
    return happy[k-1] if k <= len(happy) else ''