def fillcell(i,j,A,t): #calculate each cell in the table
    tMax=aij=A[i][j]
    t[i][j]=(tMax,i,j)
    if i-1 >=0 :
        aij_up=t[i-1][j][0]+A[i][j]
        if tMax<aij_up:
            tMax=aij_up
            t[i][j]=(tMax,i-1,j)
    if j-1>=0:
        aij_left=t[i][j-1][0]+A[i][j]
        if tMax< aij_left:
            tMax=aij_left
            t[i][j]=(tMax,i,j-1)
    return t

def fillTable(rows,cols,A):
  t=[([0]*cols) for i in range(rows)]
  t[0][0]=(A[0][0],0,0)
  aij=aij_up=aij_left=tMax=-9999# without assignment?

  for i in range(0,rows):
    for j in range(cols):
        t=fillcell(i,j,A,t)
  return t

def findBest(rows,cols,t):
  best=(t[rows-1][0],rows-1,0)
  i=1
  while i<cols-1:
    if best[0][0]<t[rows-1][i][0]:
      best=(t[rows-1][i],rows-1,i) 
    i=i+1
  i=0
  while i<=rows-1:
    if best[0][0]<t[i][cols-1][0]:
      best=(t[i][cols-1],i,cols-1)  
    i=i+1
  return best

def showSolution(best,t):
  i=1
  solution=list()
  while True:
    solution=solution+[ str(best[1])+' '+str(best[2])]
    #print str.format("({},{})",best[1],best[2])
    best=t[best[1]][best[2]]
    i=i+1
    if best[1]==t[best[1]][best[2]][1] and best[2]==t[best[1]][best[2]][2]:
        #print str.format("({},{})",best[1],best[2])
        solution=solution+[ str(best[1])+' '+str(best[2])]
        break
  print i
  while i>0:
    print solution[i-1]
    i=i-1


def readfile(path):
  A=[]
  f=open(path)
  rows=int(f.readline())
  cols=int(f.readline())
  while 1:
    lines=f.readlines(rows)
    if not lines:
      break
    for line in lines:
      A=A+[[int(s) for s in line.split()]]
  return A,rows,cols


A,rows,cols=readfile("example-input-4.txt")
t=fillTable(rows,cols,A)
best=findBest(rows,cols,t)
print best[0][0]
showSolution(best,t)









