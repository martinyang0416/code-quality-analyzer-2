import heapq
import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1
    L = int(input[ptr]); ptr +=1
    s = int(input[ptr]); ptr +=1
    t = int(input[ptr]); ptr +=1

    edges = []
    adj_fixed = [[] for _ in range(n)]
    adj_S = [[] for _ in range(n)]
    original_edges = []
    for _ in range(m):
        u = int(input[ptr]); ptr +=1
        v = int(input[ptr]); ptr +=1
  