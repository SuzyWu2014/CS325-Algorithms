#include "stdio.h"
#include "stdlib.h"
#include <time.h>

#define LINENUM 9000

void GetVisibleLines(int *m,int* b, int n, int* lines){


	for (int i = 0; i < n; ++i)
	{
		lines[i]=1;//assume line is visible
	}

	for (int i = 1; i < n-1; i++)
	{
		//printf("i=%d\n",i );
		for (int j = 0; j < i ; j++)
		{
			//line j is visible
			if(lines[j]==1){

				//printf("j=%d\n",j );
				for (int k = i+1; k < n; k++)
				{
					//printf("k=%d\n",k );
					if(((b[j]-b[k])*m[i]+b[i]*(m[k]-m[j]))<(m[j]*(b[j]-b[k])+b[j]*(m[k]-m[j])))
					{
						lines[i]=0;//not visible
						//printf("i=%d not visible\n",i );
						break;
					}
				}
				if(lines[i]==0)
				break;
			}
		}
	}


}



int main(){
	int m[LINENUM];
	int b[LINENUM];
    int count=LINENUM;
    int lines[LINENUM];
	int i;

srand(time(NULL));
	m[0] = -15000;
	b[0] = -15000 + rand() % 30000;

	for(i=1; i < LINENUM ; i++){
		m[i] = m[i-1]+ rand() % 30000;
		b[i] = -15000 + rand() % 30000;
	}

	printf("Size of array %lu\n", sizeof(m)/sizeof(int));

	clock_t beg, end;
	beg = clock();
	GetVisibleLines(m,b,count,lines);
	end = clock();

	printf("Visible Lines:");
	for(i=0;i<LINENUM;i++){
		printf(" %d,", lines[i]);
	}
	printf("\n");
	printf("This algorithm took %f seconds,\n", (double)(end-beg)/CLOCKS_PER_SEC);

}
