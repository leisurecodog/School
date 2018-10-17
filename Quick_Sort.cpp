#include<iostream>
using namespace std;
int arr[]={99,5,100,7,50,38,20,55,89,15};
void swap(int& a,int& b)
{
	int tmp;
	tmp=a;
	a=b;
	b=tmp;
}
void quick_sort(int f,int l)
{
	int x,i,j;
	if(f>l)return;
	x=arr[f];
	i=f;
	j=l;
	while(i<j)
	{
		while(arr[j]>=x)
		{
			if(i>=j)
			break;
			j--;
		}
		swap(arr[i],arr[j]);
		while(arr[i]<=x)
		{
			if(i>=j)
			break;
			i++;
		}
		swap(arr[i],arr[j]);
	}
	for(int i=0;i<10;i++)
	cout<<arr[i]<<" ";
	cout<<endl;
	quick_sort(f,j-1);
	quick_sort(j+1,l);
	
}

int main()
{
	quick_sort(0,9);
	for(int i=0;i<10;i++)
	cout<<arr[i]<<" ";
	cout<<endl;
	return 0;
 } 
