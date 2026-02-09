import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    for _ in range(t):
        n = int(data[ptr])
        m = int(data[ptr+1])
        ptr +=2
        tourist_nodes = []
        if m > 0:
            tourist_nodes = list(map(int, data[ptr:ptr+m]))
            ptr += m
        adj = [[] for _ in range(n+1)]
        for __ in range(n-1):
            u = int(data[ptr])
            v = int(dat