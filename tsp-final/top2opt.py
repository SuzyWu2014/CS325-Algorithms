from tspFuns import swapPath, mergeSort, rebuildTour


def do2opt(cities,route, dstSelected, tour,p):
    i = len(dstSelected) - 1
    while i > max(len(dstSelected) * p,len(dstSelected)-1000):
        j = i - 1
        while j >max(len(dstSelected) * p,len(dstSelected)-1000):
            dst1=dstSelected[i]
            dst2=dstSelected[j]
            route,dstSelected,tour=swapPath(cities,route,dstSelected,tour,dst1,dst2)
            j = j - 1
        i = i - 1

    return route, tour, dstSelected


def doTop2opt(cities,route, dstSelected, tour):
    dstSelected = mergeSort(dstSelected, 2)
    t = 0
    while t<30:
        temp = route
        route, tour, dstSelected = do2opt(cities,route, dstSelected, tour, 0.9)
        dstSelected = mergeSort(dstSelected, 2)
        print t, route
        if temp == route:
            break
        t = t + 1

    return tour, route,dstSelected
