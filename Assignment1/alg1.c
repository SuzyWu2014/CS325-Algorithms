#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <utime.h>
#include <string.h>
#include <dirent.h>
#include <math.h>
#include <sys/un.h>
#include <limits.h>

#define LINENUM 5000

int main(){
 int i, j, k;
 int m[LINENUM];
 int b[LINENUM];
 int v[LINENUM];

 srand(time(NULL));

m[0] = -15000;
b[0] = -15000 + rand() % 30000;

  for(i=1; i < LINENUM ; i++){
     m[i] = m[i-1]+ rand() % 30000;
     b[i] = -15000 + rand() % 30000;
  }

 printf("Size of array %lu\n", sizeof(m)/sizeof(int));

 for(i=0;i<LINENUM;i++){
     v[i]=1;
 }


 clock_t beg, end;
 beg = clock();

 for(i=1; i<(LINENUM-1); i++){
     for(j=0; j<i; j++){
         for(k=i+1; k<LINENUM; k++){
             if(m[j]*(b[j]-b[k])+b[j]*(m[k]-m[j])>m[i]*(b[j]-b[k])+b[i]*(m[k]-m[j])){
                 //line is not visible
                 v[i] = 0;
             }
         }
     }
 }

 end = clock();

 printf("Visible Lines:");
 for(i=0;i<LINENUM;i++){
     printf(" %d,", v[i]);
 }
printf("\n");
printf("This algorithm took %f seconds,\n", (double)(end-beg)/CLOCKS_PER_SEC);
return(0);
}
