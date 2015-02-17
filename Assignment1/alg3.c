 #include "stdio.h"
#include "stdlib.h"
#include <time.h>

#define LINENUM 9000

void GetVisibleLines(int* m,int* b,int n, int* lines){

    int vlines[n];
	vlines[0]=0;
	vlines[1]=1;//y1 and y2 are visible lines when we only get 2 lines
	int countVisible=2;
	for (int i = 2; i < n; ++i)
	{
		for (int j = 0; j < countVisible-1; ++j)
		{
			if(((b[vlines[j]]-b[vlines[j+1]])*m[vlines[j]]+b[vlines[j]]*(m[vlines[j+1]]-m[vlines[j]]))<(m[i]*(b[vlines[j]]-b[vlines[j+1]])+b[i]*(m[vlines[j+1]]-m[vlines[j]])))
					{
						countVisible=j+1;
						break;
					}
		}

		vlines[countVisible]=i;// yi is visible
		countVisible++;

	}

	for (int i = 0; i < countVisible; ++i)
	{
		lines[vlines[i]]=1;
	}
}

int main(){
	int m[LINENUM];
	int b[LINENUM];
	int lines[LINENUM];
	int i;
	for (int i = 0; i < LINENUM; ++i)
	{
		lines[i]=0;
	}

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
	GetVisibleLines(m,b,LINENUM,lines);

	end = clock();


	printf("Visible Lines:");
		for (int i = 0; i < LINENUM; ++i)
	{
			printf(" %d,", lines[i]);
	}
	printf("\n" );
	printf("This algorithm took %f seconds,\n", (double)(end-beg)/CLOCKS_PER_SEC);

}
