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


def main():
	l_2d = [[0, 1, 2, 2], [3, 4, 5, 5], [6, 7, 8, 8]]
	arr_t = np.array(l_2d).T.tolist()
	print(l_2d)
	print(arr_t)
	print(transpose(l_2d))


if __name__ == '__main__':
	main()