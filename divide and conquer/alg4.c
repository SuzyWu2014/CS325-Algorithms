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

#define LINENUM 100



int m[LINENUM]={-990, -941, -940, -939, -864, -841, -840, -825, -814, -807, -805, -803, -791, -767, -726, -721, -719, -714, -702, -619, -610, -538, -537, -522, -512, -510, -491, -482, -474, -461, -422, -408, -386, -360, -341, -336, -319, -311, -273, -270, -257, -255, -240, -216, -159, -148, -146, -133, -113, -54, -52, -28, 61, 68, 82, 124, 134, 189, 205, 224, 248, 253, 270, 306, 310, 312, 325, 327, 335, 336, 347, 352, 355, 361, 364, 375, 378, 385, 396, 397, 418, 463, 470, 472, 485, 501, 545, 552, 561, 564, 613, 619, 679, 704, 708, 853, 859, 869, 876, 994};
int b[LINENUM]={-73, -393, -363, -443, -259, 142, -93, 807, 927, -703, 396, 462, -29, 877, 171, -476, 864, -738, 372, 150, 620, -885, 411, -385, 589, 901, -211, 286, -303, 521, -366, 976, -293, 561, 903, 364, -889, -114, 381, -258, -927, -422, 724, 701, 950, 218, 843, -48, -971, -827, 594, -518, 705, 851, -180, 575, -861, 563, -822, -779, 93, -607, -809, -579, -155, -936, -572, -17, -456, -928, -362, -208, 795, 504, -927, -826, -682, 62, -447, 503, -911, -884, -263, 784, 846, 401, -527, -137, -714, 619, 8, 259, -466, -745, 699, 750, -875, -381, 236, -814};



int v[LINENUM];

struct MyArray{
	int length;
	int *data;
};

struct MyArray* MergeVisible(struct MyArray *leftVlines, struct MyArray *rightVlines){
	int i=0;
	int j=0;
	while(i<leftVlines->length || j<rightVlines->length){
		 if((i<leftVlines->length-1 ) && (j==rightVlines->length-1 || ((b[leftVlines->data[i+1]]-b[leftVlines->data[i]])*(m[ rightVlines->data[j]]-m[ rightVlines->data[j+1]]))<=((b[ rightVlines->data[j+1]]-b[ rightVlines->data[j]])*(m[leftVlines->data[i]]-m[leftVlines->data[i+1]])))){
				//y_i(x_i_i+1)<y_j(x_i,i+1)
		
				if(m[leftVlines->data[i]]*(b[leftVlines->data[i+1]]-b[leftVlines->data[i]])+b[leftVlines->data[i]]*(m[leftVlines->data[i]]-m[leftVlines->data[i+1]]) > m[ rightVlines->data[j]]*(b[leftVlines->data[i+1]]-b[leftVlines->data[i]])+b[ rightVlines->data[j]]*(m[leftVlines->data[i]]-m[leftVlines->data[i+1]])){
					//intersect i/j found
					break;
				}
				else{

					i++;
					//if(rightVlines->length==1 ){
					//	break;
					//}
				}

			}
			else{
				//x_i_i+1>xj_j+1
				//y_i(x_j_j+1)< y_j(x_j_j+1)
				if( j==rightVlines->length-1 || m[leftVlines->data[i]]*(b[ rightVlines->data[j+1]]-b[ rightVlines->data[j]])+b[leftVlines->data[i]]*(m[ rightVlines->data[j]]-m[ rightVlines->data[j+1]])>= m[ rightVlines->data[j]]*(b[ rightVlines->data[j+1]]-b[ rightVlines->data[j]])+b[ rightVlines->data[j]]*(m[ rightVlines->data[j]]-m[ rightVlines->data[j+1]])){
					break;
				}
				else{
					j++;
					 
				}
			}

	}
	 struct MyArray *visibleLines=(struct MyArray*)malloc(sizeof(struct MyArray));;
	 visibleLines->length=i+1+rightVlines->length-j;
	 visibleLines->data= malloc(sizeof(int)*(int)visibleLines->length);
	
	for (int t =0; t <=i; ++t)
	{
		visibleLines->data[t]=leftVlines->data[t];

	}

	for (int k = 0; k <= rightVlines->length-j; ++k)
	{
		visibleLines->data[i+k+1]=rightVlines->data[j+k];
	}
	
	return visibleLines;

}

struct MyArray* GetVisibleLines(int* m, int* b, struct MyArray *lines){
	//Bases Cases
	//struct MyArray* visibleLines;
	if(lines->length==2 || lines->length==1){
	
		return lines; //both visible
	}

	//Recursive Cases
	int mid = floor(lines->length/2);

	struct MyArray *leftLines=(struct MyArray*)malloc(sizeof(struct MyArray));; 
	struct MyArray *rightLines=(struct MyArray*)malloc(sizeof(struct MyArray));;

	leftLines->length=mid;
	leftLines->data=(int*)malloc(sizeof(int*)*leftLines->length);
	rightLines->length=lines->length-mid;
	rightLines->data=(int*)malloc(sizeof(int*)*rightLines->length);
	for (int i = 0; i <mid; ++i)
	{
		leftLines->data[i]=lines->data[i];
	}
	for (int j = 0; j < lines->length; ++j)
	{
		rightLines->data[j]=lines->data[j+mid];
	}
	
	struct MyArray *leftVlines = GetVisibleLines(m, b,leftLines);
	struct MyArray *rightVlines = GetVisibleLines(m, b, rightLines);

	struct MyArray* visibleLines=MergeVisible(leftVlines, rightVlines);
/*	printf("merge visible:%d ----------------------------------\n",visibleLines->length);
	for (int r = 0; r < visibleLines->length ; ++r)
	{
		printf("vlines:%d\n", visibleLines->data[r]);
	}
*/	return visibleLines;
	}

int main(){
int i;
int indicies[LINENUM];
for(i=0;i<LINENUM;i++){
	indicies[i]=i;
}
struct MyArray *lines=(struct MyArray*)malloc(sizeof(struct MyArray)); 
lines->length=LINENUM;
lines->data=indicies;
struct MyArray *results=(struct MyArray*)malloc(sizeof(struct MyArray));;
clock_t beg, end;


srand(time(NULL));

beg = clock();

results = GetVisibleLines(m, b, lines);
end = clock();

int alllines[LINENUM];
for (i = 0; i < LINENUM; ++i)
{
	alllines[i]=0;
}
for (int t = 0; t < results->length; ++t)
{
	alllines[results->data[t]]=1;
}
printf("Visible Lines:");
for(i=0;i<LINENUM;i++){

	printf(" %d,", alllines[i]);
}
printf("\n");
printf("This algorithm took %f seconds,\n", (double)(end-beg)/CLOCKS_PER_SEC);
return(0);
}
