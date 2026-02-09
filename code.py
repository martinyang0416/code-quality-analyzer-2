def main():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    variables = []
    name_to_index = {}

    for idx in range(n):
        line = sys.stdin.readline().strip()
        parts = line.split()
        name = parts[0]
        expr = ' '.join(parts[2:])  # everything after ":", excluding :=

        if expr[0] in '01':
            # constant case
            const_str = expr
            assert len(const_str) == m
            variables.append(('const', const_str))
        e