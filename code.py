def main():
    s = input().strip()
    s_list = list(s)
    n = len(s)
    res = []
    for i in range(1, n + 1):
        prefix = s_list[:i]
        reversed_p = prefix[::-1]
        if reversed_p < prefix:
            res.append(1)
            s_list[:i] = reversed_p
        else:
            res.append(0)
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()