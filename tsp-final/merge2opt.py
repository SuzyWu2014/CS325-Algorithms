from tspFuns import swapPath, calDistance, mergeSort


def getDstOrderByPath(tour,cities,start,end):
    dstOrdByPath=[]
    n=len(tour)
    i=start
    while i<end-1:
        dstOrdByPath.append([tour[i],tour[i+1],calDistance(cities[tour[i]],cities[tour[i+1]])])
        i=i+1
    return dstOrdByPath


def tourMerge(cities,leftTour, rightTour):
    dst=getDstOrderByPath(leftTour,cities,1,len(leftTour))
    dst.extend(getDstOrderByPath(rightTour,cities,0,len(rightTour)-1))
    cityA=leftTour[len(leftTour)-1]
    cityB=rightTour[0]
    dst.append([cityA,cityB,calDistance(cities[cityA],cities[cityB])])
    dst=mergeSort(dst,2)
    tour=leftTour
    tour.extend(rightTour)

    t=i=n=len(dst)-1

    if t>1000:
        t=n*0.5
    else:
        t=2

    while i>t:
        j=i-1
        while j>t:
            dst1=dst[i]
            dst2=dst[j]
            route,dst,tour=swapPath(cities,0,dst,tour,dst1,dst2)
            j = j - 1
        i=i-1

    return tour


def merge2opt(cities,tour):
    n=len(tour)
    if n<5:
        return tour
    else:
        mid=int(n/2)
        leftTour=tour[:mid]
        rightTour=tour[mid:]
        leftTour=merge2opt(cities,leftTour)
        rightTour=merge2opt(cities,rightTour)
        return tourMerge(cities,leftTour,rightTour)
