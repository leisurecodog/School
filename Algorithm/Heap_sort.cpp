#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int arr[11];
int HP[11]={0,5,100,7,59,55,77,884,22,37,15};
void C_heap(int last){
	int keep=last;
	keep--;
	keep/=2;
	for(int i=keep;i>0;i--)
	{
		int temp=HP[i];
		int j=i*2;
		while(j<last)
		{
			if(j<last && j+1<last)
				if(HP[j]>HP[j+1])j++;
			if(temp>HP[j])
			{
				HP[j/2]=HP[j];
				j*=2;
			}
			else break;
		}
		swap(temp,HP[j/2]);
	}
}
void Heap(int point,int last)
{
	int temp=HP[point];
		int j=point*2;
		while(j<last)
		{
			if(j<last && j+1<last)
				if(HP[j]>HP[j+1])j++;
			if(temp>HP[j])
			{
				HP[j/2]=HP[j];
				j*=2;
			}
			else break;
		}
		swap(temp,HP[j/2]);
}
void heap_sort(int last)
{
	arr[1]=HP[1];
	HP[1]=HP[last-1];
	for(int i=2;i<last;i++)
	{
		Heap(1,last-i+1);
		arr[i]=HP[1];
		HP[1]=HP[last-i];
	}
}
int main()
{
	cout<<"Before Sorting:"<<endl;
	for(int i=1;i<11;i++)
		cout<<HP[i]<<" ";
		cout<<endl;
	C_heap(11);
	heap_sort(11);
	cout<<"After Sorting:"<<endl;
	for(int i=1;i<11;i++)
		cout<<arr[i]<<" ";
		cout<<endl;
	return 0;
}
