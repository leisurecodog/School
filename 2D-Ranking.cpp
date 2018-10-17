#include<iostream>
#include<cmath>
#include<time.h>
using namespace std;
struct dp2{
	int x;
	int y;
	int rank;
}; 
struct dp2 arr[10];
void swap(dp2& a,dp2& b)
{
	dp2 tmp;
	tmp=a;
	a=b;
	b=tmp;
}
void quick_sort(int f,int l,bool ju)
{
	int x,i,j;
	if(f>l)return;
	x=(ju ? arr[f].x:arr[f].y);
	i=f;
	j=l;
	while(i<j)
	{
		while((ju?arr[j].x : arr[j].y)>=x)
		{
			if(i>=j)
			break;
			j--;
		}
		swap(arr[i],arr[j]);
		while((ju?arr[i].x : arr[i].y)<=x)
		{
			if(i>=j)
			break;
			i++;
		}
		swap(arr[i],arr[j]);
	}
	quick_sort(f,j-1,ju);
	quick_sort(j+1,l,ju);
	
}

void Ranking(int f,int l){
	if(f>=l)return ;
	if(l-f==1)
	{
		if(arr[l].y>arr[f].y)arr[l].rank++;
		quick_sort(f,l,0);
		return;
	}
	int m=(f+l)/2;
	Ranking(f,m);
	Ranking(m+1,l);
	for(int i=m+1;i<=l;i++)//right point
		for(int j=f;j<m+1;j++)//left point
			if(arr[i].y>arr[j].y)arr[i].rank++;
	quick_sort(f,l,0);
}  

int main()
{
	srand(time(NULL));
	for(int i=0;i<10;i++)
		arr[i].x=(rand()%100)+1;
	for(int i=0;i<10;i++)
		arr[i].y=(rand()%100)+1;
	quick_sort(0,9,1);
	Ranking(0,9);
	quick_sort(0,9,1);
	for(int i=0;i<10;i++)
	cout<<arr[i].x<<" "<<arr[i].y<<" "<<arr[i].rank<<endl;
	cout<<endl<<endl;
	return 0;
}

