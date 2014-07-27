def break_test():
	for n in range(2, 10):
		for x in range(2, n):
			if n % x == 0:
				print(n, 'equals', x, '*', n//x)
				break
		else:
			print(n, 'is a prime number')
	
	print("hello world")
	
import math
def compare_func(a, b):
	return a > b

def compare_speed(compare_func):
	for n in range(1, 100):
		a = int(8 * math.pow(n, 2))
		b = int(64 * n * math.log(n, 10))

		if compare_func(a, b):
			print("n=", n, ";a=", a, ";b=", b)
		#else:
		#	print("n=", n, ";a=", a, ";b=", b)

def insert_sort(A, compare_func):
	""" 插入排序，和归并排序两个都是比较常用的排序算法


	"""
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and compare_func(A[i], key):
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
			
	return A

arr = [5, 2, 4, 6, 1, 3, 10, 2345, 234, 12, 324, 7, 78234]

print(insert_sort(arr, compare_func))

#compare_speed(compare_func)