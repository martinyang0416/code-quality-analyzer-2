import sys
from collections import deque

def rotate_right(s, N):
    return ((s >> 1) | ((s & 1) << (N-1))) & ((1 << N) - 1)

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        lights_str = input[idx]
        switches_str = input[idx+1]
        idx +=2

        initial_lights = int(lights_str, 2)
        initial_switches = int(switches_str, 2)
        target = initial_lights

    