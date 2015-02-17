from math import sqrt

__author__ = 'suzy'


def readfile(path):
	f = open(path)
	n = 0
	cities = []
	while 1:
		lines = f.readlines(100)
		if not lines:
			break
		for line in lines:
			cities = cities + [[int(i) for i in line.split()]]
			n = n + 1
	return cities, n


def merge(left, right, k):  # k->index in array that is used as reference for sorting
	length = len(left) + len(right)
	i = j = 0
	combine = []
	while len(combine) < length:
		if left[i][k] < right[j][k]:
			combine.append(left[i])
			if i == len(left) - 1:
				combine.extend(right[j:])
				break
			else:
				i = i + 1
		else:
			combine.append(right[j])
			if j == len(right) - 1:
				combine.extend(left[i:])
				break
			else:
				j = j + 1
	return combine


def mergeSort(array, k):
	length = len(array)
	if length == 1 or length == 0:
		return array
	else:
		mid = int(length / 2)
		left = array[:mid]
		right = array[mid:]
		leftOrd = mergeSort(left, k)
		rightOrd = mergeSort(right, k)
		return merge(leftOrd, rightOrd, k)


def rebuildTour(dstSelected, tour):
    dstSelected = mergeSort(dstSelected, 2)
    cityA = dstSelected[0][0]
    cityB = dstSelected[0][1]
    a = tour.index(cityA)
    b = tour.index(cityB)
    if a > b:
        a, b = b, a
    tour1 = tour[:a + 1]
    tour2 = tour[b:]
    tour2.extend(tour1)
    return tour2


def calDistance(cityA, cityB):
	"""cityA (index,x,y)"""
	d = int(round(sqrt(pow((cityA[1] - cityB[1]), 2) + pow((cityA[2] - cityB[2]), 2))))
	return d


def addPathToTour(city1, city2, visited, tour, dstSelected, route):
	"""Add path city1<->city2 to tour
       city1(index,x,y)
    """
	cityA = city1[0]
	cityB = city2[0]

	if cityB<cityA:
		cityA,cityB=cityB,cityA

	if visited[cityA] < 2 and visited[cityB] < 2:
		isFound = 0
		isCircle = 0
		for subtour in tour:
			lg = len(subtour)
			if subtour[0] == cityA:
				isFound = 1
				if subtour[lg - 1] != cityB:
					subtour.insert(0, cityB)
				else:
					isCircle = 1
				break
			elif subtour[0] == cityB:
				isFound = 1
				if subtour[lg - 1] != cityA:
					subtour.insert(0, cityA)
				else:
					isCircle = 1
				break
			elif subtour[lg - 1] == cityA:
				isFound = 1
				if subtour[0] != cityB:
					subtour.insert(lg, cityB)
				else:
					isCircle = 1
				break
			elif subtour[lg - 1] == cityB:
				isFound = 1
				if subtour[0] != cityA:
					subtour.insert(lg, cityA)
				else:
					isCircle = 1
				break

		if isFound == 0:
			tour.insert(0, [cityA, cityB])
		if isCircle == 0:
			d = calDistance(city1, city2)
			dstSelected.append([cityA, cityB, d])
			route = route + d
			visited[cityA] = visited[cityA] + 1
			visited[cityB] = visited[cityB] + 1
	return visited, tour, dstSelected, route


def combineSubtours(route, tour, visited, dstOrdered):
	i = len(tour) - 1
	while i > 0:
		isInsert = 0
		for subtour in tour[:i]:
			lg = len(subtour)
			t = len(tour[i])
			if tour[i][0] == subtour[0]:
				j = 1
				while j < t:
					subtour.insert(0, tour[i][j])
					j = j + 1
				isInsert = 1
			elif tour[i][0] == subtour[lg - 1]:
				j = 1
				while j < t:
					subtour.insert(lg, tour[i][j])
					lg = lg + 1
					j = j + 1
				isInsert = 1
			elif tour[i][t - 1] == subtour[0]:
				j = t - 2
				while j >= 0:
					subtour.insert(0, tour[i][j])
					j = j - 1
				isInsert = 1
			elif tour[i][t - 1] == subtour[lg - 1]:
				j = t - 2
				while j >= 0:
					subtour.insert(lg, tour[i][j])
					lg = lg + 1
					j = j - 1
				isInsert = 1
			if isInsert == 1:
				if subtour[0] == subtour[len(subtour) - 1] and len(subtour) > 1:
					# break circle by removing first path--------------------->other choice?
					visited[subtour[0]] = visited[subtour[0]] - 1
					visited[subtour[1]] = visited[subtour[1]] - 1
					for item in dstOrdered:
						if (item[0] == subtour[0] and item[1] == subtour[1]) or (
										item[0] == subtour[1] and item[1] == subtour[0]):
							dstOrdered.remove(item)
							route = route - item[2]
					del subtour[0]
				# route=route-dst[subtour[0]][subtour[1]]
				del tour[i]
				break
		i = i - 1
	return route, tour, visited, dstOrdered


def countAvg(array, k):
	i = 0
	s = 0
	for item in array:
		s = s + item[k]
		i = i + 1
	return int(s / i)


def updateTour(tour, a, b, c, d):  # a<b<c<d
    tour1 = tour[:a + 1]
    tour2 = tour[b:c + 1]
    tour3 = tour[d:]
	# tour=tour1+tour2[::-1]+tour3
    tour1.extend(tour2[::-1])
    tour1.extend(tour3)
    return tour1


def calPathAB(cities, cityA1, cityA2, cityB1, cityB2):
    d11 = calDistance(cities[cityA1], cities[cityB1])
    d12 = calDistance(cities[cityA1], cities[cityB2])
    d21 = calDistance(cities[cityA2], cities[cityB1])
    d22 = calDistance(cities[cityA2], cities[cityB2])

    pathA = d12 + d21
    pathB = d11 + d22
    return pathA, pathB, d11, d12, d21, d22


def selectPathA(tour, a1, a2, b1, b2):
    if a1 < a2 < b2 < b1:
        tour = updateTour(tour, a1, a2, b2, b1)
    elif b2 < b1 < a1 < a2:
        tour = updateTour(tour, b2, b1, a1, a2)
    elif a2 < a1 < b1 < b2:
        tour = updateTour(tour, a2, a1, b1, b2)
    elif b1 < b2 < a2 < a1:
        tour = updateTour(tour, b1, b2, a2, a1)
    return tour


def selectPathB(tour, a1, a2, b1, b2):
    if a1 < a2 < b1 < b2:
        tour = updateTour(tour, a1, a2, b1, b2)
    elif b1 < b2 < a1 < a2:
        tour = updateTour(tour, b1, b2, a1, a2)
    elif a2 < a1 < b2 < b1:
        tour = updateTour(tour, a2, a1, b2, b1)
    elif b2 < b1 < a2 < a1:
        tour = updateTour(tour, b2, b1, a2, a1)
    return tour


def swapPath(cities, route, dstSelected, tour, dst1, dst2):
	cityA1 = dst1[0]
	cityA2 = dst1[1]
	cityB1 = dst2[0]
	cityB2 = dst2[1]

	path = dst1[2] + dst2[2]
	pathA, pathB, d11, d12, d21, d22 = calPathAB(cities, cityA1, cityA2, cityB1, cityB2)
	a1 = tour.index(cityA1)
	a2 = tour.index(cityA2)
	b1 = tour.index(cityB1)
	b2 = tour.index(cityB2)
	if pathA< path and ((a1 < a2 and b2 < b1) or (a1 > a2 and b1 < b2)):
		dstSelected.remove(dst1)
		dstSelected.remove(dst2)
		if cityA1>cityB2:
			cityA1,cityB2=cityB2,cityA1
		if cityA2>cityB1:
			cityA2,cityB1=cityB1,cityA2
		dstSelected.extend([[cityA1, cityB2, d12], [cityA2, cityB1, d21]])
		route = route - path + pathA
		# print route
		tour = selectPathA(tour, a1, a2, b1, b2)
	elif pathB < path and ((a1 < a2 and b1 < b2) or (a1 > a2 and b1 > b2)):
		dstSelected.remove(dst1)
		dstSelected.remove(dst2)
		if cityA1>cityB1:
			cityA1,cityB1=cityB1,cityA1
		if cityA2>cityB2:
			cityA2,cityB2=cityB2,cityA2
		dstSelected.extend([[cityA1, cityB1, d11], [cityA2, cityB2, d22]])
		route = route - path + pathB
		# print route
		tour = selectPathB(tour, a1, a2, b1, b2)

	return route, dstSelected, tour