import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr]); ptr +=1
    X = int(input[ptr]); ptr +=1
    Y = int(input[ptr]); ptr +=1

    towns = []
    for _ in range(N):
        K = int(input[ptr]); ptr +=1
        sweets = []
        for __ in range(K):
            a = int(input[ptr]); ptr +=1
            b = int(input[ptr]); ptr +=1
            c = int(input[ptr]); ptr +=1
            sweets.append( (a, b, c) )
        town