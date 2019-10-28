def cumsum(list):
	cumsum = 0
	newList = list[:]
	for item in list:
		cumsum += item
		newList.append(cumsum)
	return newList