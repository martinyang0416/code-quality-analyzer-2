def main():
    s = input().strip()
    vowels = {'A', 'E', 'I', 'O', 'U'}
    pattern = []
    for c in s:
        if c in vowels:
            pattern.append('V')
        else:
            pattern.append('C')
    
    # Check if the pattern is a palindrome
    if pattern == pattern[::-1]:
        vowel_count = sum(1 for c in s if c in vowels)
        if vowel_count % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
