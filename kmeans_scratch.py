#Making a kmeans classifier from scratch

import numpy as np
from sympy.utilities.iterables import ibin

arr = np.array([
	[1, 2],
	[2, 2],
	[3, 3],
	[2.5, 2],
	[2.2, 1],
	[1.5, 3],
	[2.8, 4],
	[7, 10],
	[8, 9],
	[7.5, 8.5],
	[10,10]])

def create_indices(arr):
	indices = list(ibin(len(arr), 'all'))
	return indices

indices = create_indices(arr)

def calc_loss(arr2d, index_set):
	sum_x1, sum_x2 = 0,0
	sum_y1, sum_y2 = 0,0
	n1, n2 = 0,0
	euclidean_distance1, euclidean_distance2 = 0, 0
	set1 = []
	set2 = []

	for i in range(len(arr2d[:,0])):
		if index_set[i] == 0:
			sum_x1 += arr2d[i, 0]
			sum_y1 += arr2d[i, 1]
			n1 += 1
			set1.append(arr2d[i, :])
		else:
			sum_x2 += arr2d[i, 0]
			sum_y2 += arr2d[i, 1]
			n2 += 1
			set2.append(arr2d[i, :])

	if n1 != 0 and n2 != 0:
		set1_centroid = [sum_x1/n1, sum_y1/n1]
		set2_centroid = [sum_x2/n2, sum_y2/n2]
		for i in range(len(set1)):
			euclidean_distance1 += ((set1[i][0]-set1_centroid[0])**2)+((set1[i][1]-set1_centroid[1])**2)**0.5
		for i in range(len(set2)):
			euclidean_distance2 += ((set2[i][0]-set2_centroid[0])**2)+((set2[i][1]-set2_centroid[1])**2)**0.5
		return euclidean_distance1 + euclidean_distance2
	else:
		return 99*99


def calc_losses(arr, index_set):
	losses = []
	for i in range(len(index_set)):
		losses.append(calc_loss(arr, index_set[i]))
	return losses

def find_min_loss(losses):
	min_loss = losses[0]
	for j in losses:
		if j < min_loss:
			min_loss = j
	return min_loss

def min_loss_index(arr2d, index_set):
	for i in range(len(indices)):
		if calc_loss(arr2d, indices[i]) == find_min_loss(calc_losses(arr2d, index_set)):
			return i
			break

print(indices[min_loss_index(arr, indices)])