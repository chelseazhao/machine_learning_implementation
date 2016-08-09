import os
import numpy as np
#form: label data
def load_train_data_label(filename):
	fw = open(filename, 'r')
	lines = fw.readlines()
	labels = []
	data = []
	for line in lines:
		labels.append(float(line.split()[0]))
		sub = []
		for i in range(1, len(line.split())):
			sub.append(float(line.split()[i]))
		data.append(sub)
	return labels, data

y, x = load_train_data_label("train.txt")
a = np.zeros(len(x), np.float)
b = 0.0
Gram_Matrix = None 

def cal_gram_matrix():
	data_len = len(x)
	gram = np.empty((data_len, data_len), np.int)
	for i in range(data_len):
		for j in range(data_len):
			gram[i][j] = np.dot(x[i], x[j])
	return gram

def cal(i):
	global a, b, x, y
	res = np.dot(a * y, Gram_Matrix[i])
	res = y[i] * (res + b)
	return res

def update(i):
	global a, b
	a[i] = a[i] + 1
	b = b + y[i]

def check():
	global a, b, x, y
	flag = 0
	for i in range(len(x)):
		if cal(i) <= 0:
			flag = 1
			update(i)
	if flag == 0:
		w = np.dot(a*y, x)
		print "Result is w: " + str(w) + " b: " + str(b)
		return True
	return False


if __name__ == "__main__":
	Gram_Matrix = cal_gram_matrix()
	flag = 1
	for i in range(1000):
		if check():
			flag = 0
			break
	if flag == 1:
		print "Unsolved"
