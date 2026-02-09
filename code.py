from math import ceil, log, floor, sqrt
import math	
	
	
k = 1	
def mod_expo(n, p, m):
	"""find (n^p)%m"""
	result = 1
	while p != 0:
		if p%2 == 1:
			result = (result * n)%m
		p //= 2
		n = (n * n)%m
	return result
	
def is_prime(n):
	m = 2
	while m*m <= n:
		if n%m == 0:
			return False
		m += 1
	return True
	
def find_sum(n, a):
	a.insert(0, 0)
	for i in range(1, n+1):
		prev = a[i] & a[i-1]
		cur = a[i] | a[i-1]
		a[i-1] = prev
		a[i] = cur
	return sum(m*m for m in a)

def prin_abc(x, y, z)