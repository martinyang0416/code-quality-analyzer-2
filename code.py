import sys

def decode_caesar(line):
    result = []
    n = 0
    for c in line:
        if c.isalpha():
            encrypted_pos = ord(c) - ord('a')
            shift = (n + 1) % 26
            original_pos = (encrypted_pos - shift) % 26
            result.append(chr(original_pos + ord('a')))
        else:
            result.append(c)
        n += 1
    return ''.join(result)

def main():
    for line in sys.stdin:
        line = line.rstrip('\n')
        decoded_line = decode_caesar(line)
  