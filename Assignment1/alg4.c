#include "stdio.h"
#include "stdlib.h"
#include <time.h>


int* MergeVisible(int* leftVlines,int* rightVlines,int countLeft,int countRight,int& countVisible){
	int i=j=0; 
	while(i<countLeft || j<countRight){
		if(i<countLeft && ((b[leftVlines[i+1]]-b[leftVlines[i]])*(m[ rightVlines[j]]-m[ rightVlines[j+1]]))<((b[ rightVlines[j+1]]-b[ rightVlines[j]])*(m[leftVlines[i]]-m[leftVlines[i+1]])) ){
			if(m[leftVlines[i]]*(b[leftVlines[i+1]]-b[leftVlines[i]])+b[leftVlines[i]]*(m[leftVlines[i]]-m[leftVlines[i+1]])>m[ rightVlines[j]]*(b[leftVlines[i+1]]-b[leftVlines[i]])+b[ rightVlines[j]]*(m[leftVlines[i]]-m[leftVlines[i+1]])){
				//intersect i/j found
				break;
			}
			else{
				i++;
			}
		
		}
		else{
			if(m[leftVlines[i]]*(b[ rightVlines[j+1]]-b[ rightVlines[j]])+b[leftVlines[i]]*(m[ rightVlines[j]]-m[ rightVlines[j+1]])>m[ rightVlines[j]]*(b[ rightVlines[j+1]]-b[ rightVlines[j]])+b[ rightVlines[j]]*(m[ rightVlines[j]]-m[ rightVlines[j+1]])){
				break;
			}
			else{
				j++;
			}
		}
	}
	 *countVisible=i+1+countRight-j; 
	int* visibleLines=int[countVisible];
	for (int t = 0; t < i; ++t)
	{
		visibleLines[t]=leftVlines[i];
	}
	for (int k = 0; k < countRight-j; ++k)
	{
		visibleLines[i+k]=rightVlines[j++];
	}
	return visibleLines;

}

int* GetVisibleLines(int* m, int* b, int n, int* lines, int* countVisible){
	if(n=2 || n=1){
		*countVisible=n;
		return lines; //both visible
	}
	else{
		mid=n/2;
		int* leftLines[mid]=rightLines[mid];
		for (int i = 0; i <mid; ++i)
		{	
			leftLines[i]=vlines[i];
		}
		for (int j = 0; j < n; ++j)
		{
			rightLines[j]=vlines[j+mid];
		}
		int* countLeft=countRight=0;
		int* leftVlines=GetVisibleLines(m,b, mid,leftLines,&countLeft);
		int* rightVlines=GetVisibleLines(m,b,n-mid,rightLines,&countRight);
		return MergeVisible(leftVlines,rightLines,countLeft,countRight
			,&countVisible);
	}

int main(){

} 


