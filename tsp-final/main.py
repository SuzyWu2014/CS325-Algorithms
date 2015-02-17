
from Initialization import doTourInitialization
from merge2opt import merge2opt, getDstOrderByPath
from top2opt import doTop2opt
from tspFuns import readfile, calDistance

cities, n = readfile("input-test3.txt")
print "number of cities: " + str(n)



dstSelected, route, tour = doTourInitialization(cities)
print "Initialized tour :", route


tour, route,dstSelected =doTop2opt(cities,route, dstSelected, tour)
print "top 2-opt tour :", route


f=open("output-test3.txt","w")
f.write(str(route))
for city in tour:
    f.write('\n'+str(city))
f.close()


t=0
while t<4:
    temp=route
    tour=merge2opt(cities,tour)

    k = 0
    d = 0
    while k < n - 1:
        d = d + calDistance(cities[tour[k]], cities[tour[k + 1]])
        k = k + 1
    route=d + calDistance(cities[tour[0]], cities[tour[n - 1]])
    print "merge 2 opt", route

    f=open(str(t)+"-output-test3.txt","w")
    f.write(str(route))
    for city in tour:
        f.write('\n'+str(city))
    f.close()
    if temp==route:
        break
    t=t+1
    print t
#
# k = 0
# d = 0
# while k < n - 1:
#     d = d + calDistance(cities[tour[k]], cities[tour[k + 1]])
#     k = k + 1
# route=d + calDistance(cities[tour[0]], cities[tour[n - 1]])
# print "merge 2 opt", route
#
#
# f=open("output_example-input-1.txt","w")
# f.write(str(route))
# for city in tour:
#     f.write('\n'+str(city))
# f.close()