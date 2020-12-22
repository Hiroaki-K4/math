import numpy as np


def transpose(arr):
	col = len(arr[0]) # 3
	row = len(arr)  # 2
	ans_list = []
	i = 0
	while i < col:
		tmp_list = []
		j = 0
		while j < row:
			tmp_list.append(arr[j][i])
			j += 1
		ans_list.append(tmp_list)
		i += 1
	return ans_list


def matrix_mlp(list1, list2):
	ans_row = len(list1)
	ans_col = len(list2[0])
	ans_list = []
	for i in range(ans_row):
		tmp_list = []
		for j in range(ans_col):
			tmp = 0
			for k in range(ans_row):
				tmp += list1[i][k] * list2[k][j]
			tmp_list.append(tmp)
		ans_list.append(tmp_list)
	return ans_list


def main():
	l_2d = [[0, 1, 2, 2], [3, 4, 5, 5], [6, 7, 8, 8]]
	arr_t = np.array(l_2d).T.tolist()
	print("~~traspose_test~~")
	print("Before   : ", l_2d)
	print("correct  : ", arr_t)
	print("my_answer: ", transpose(l_2d))
	print("~~matrix_multiple_test~~")
	arr1 = np.arange(4).reshape((2, 2))
	arr2 = np.arange(6).reshape((2, 3))
	print("Before1  :", arr1.tolist())
	print("Before2  :", arr2.tolist())
	print("correct  :", np.dot(arr1, arr2).tolist())
	print("my_answer:", matrix_mlp(arr1.tolist(), arr2.tolist()))


if __name__ == '__main__':
	main()