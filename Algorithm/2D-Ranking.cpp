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
void quick_sort(int f,int l)
{
	int x,i,j;
	if(f>l)return;
	x=arr[f].x;
	i=f;
	j=l;
	while(i<j)
	{
		while(arr[j].x>=x)
		{
			if(i>=j)
			break;
			j--;
		}
		swap(arr[i],arr[j]);
		while(arr[i].x<=x)
		{
			if(i>=j)
			break;
			i++;
		}
		swap(arr[i],arr[j]);
	}
	quick_sort(f,j-1);
	quick_sort(j+1,l);
	
}
void merge(int a,int b,int c)
{
	dp2 temp[10];
	int d=0,id1=a,id2=b+1;
	int idt=0;
	while(id1<=b && id2<=c)
	{
		if(arr[id1].y<arr[id2].y)
		{
			temp[idt++]=arr[id1++];
			d++;
		}
		else
		{
			temp[idt++]=arr[id2++];
			temp[idt-1].rank+=d;
		}
	}
	while(id1<=b)temp[idt++]=arr[id1++];
	while(id2<=c)
	{
		temp[idt++]=arr[id2++];
		temp[idt-1].rank+=d;
	}
	for(int i=0;i<idt;i++)
		arr[a++]=temp[i];
}
void Ranking(int f,int l){
	if(f>=l)return ;
	int m=(f+l)/2;
	Ranking(f,m);
	Ranking(m+1,l);
	merge(f,m,l);
}  

int main()
{
	srand(time(NULL));
	for(int i=0;i<10;i++)
		arr[i].x=(rand()%100)+1;
	for(int i=0;i<10;i++)
		arr[i].y=(rand()%100)+1;
	quick_sort(0,9);
	Ranking(0,9);
	for(int i=0;i<10;i++)
	cout<<arr[i].x<<" "<<arr[i].y<<" "<<arr[i].rank<<endl;
	return 0;
}

