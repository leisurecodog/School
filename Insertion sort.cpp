#include<iostream>
using namespace std;
#define N 10
int main()
 {
 	int arr[N]={10,78,44,14,663,100,5,452,63,91};
 	cout<<"Before Sorting:"<<endl;
	for(int i=0;i<10;i++)
 		cout<<arr[i]<<" ";
 	cout<<endl<<endl<<endl;
 	for (int j=1;j<N;j++)
 	{
 		int i=j-1;
 		int x=arr[j];
 		while(x<arr[i] && i>=0)
 		{
 			arr[i+1]=arr[i];
 			i--;
		 }
		 arr[i+1]=x;
	  }
	cout<<"After Sorting:"<<endl;
	for(int i=0;i<10;i++)
	cout<<arr[i]<<" ";
	cout<<endl;
 	return 0;
 }
