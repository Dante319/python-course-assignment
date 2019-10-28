def nested_sum(list):
	sum = 0
	for i in list:
		for j in i:
			sum += j
	return sum