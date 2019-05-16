#include<iostream>
#include<fstream>
#include<string>
using namespace std;
class Node{
	friend class HTree;
	public:
		string Letter="?";
		int data;
		class Node* L=NULL;
		class Node* R=NULL;
};
class HTree{
	public:
		void Read(Node*,string&);
		void Create(Node*,int);
		void Look(Node*,string,string,string&);
};
void HTree::Read(Node* arr,string& x)
{
	fstream f;
	f.open("p5.in",ios::in);
	for(int i=0;i<5;i++)
		f>>arr[i].Letter>>arr[i].data;
	f>>x;
	f.close();
}
void HTree::Create(Node*arr,int front)
{
	Node*L=new Node;
	Node*R=new Node;
	Node* N=new Node;
	for(int i=front+1;i<5;i++)
	{
		Node take=arr[i];
		int j=i;
		while(j>front && arr[j-1].data>take.data)
		{
			arr[j]=arr[j-1];
			j--;
		}
		arr[j]=take;
	}
	if(front!=4)
	{
		*L=arr[front];*R=arr[front+1];
		N->L=L;N->R=R;
		N->data=L->data+R->data;
		arr[front+1]=*N;
	}
}
void HTree::Look(Node* t,string re,string Le,string& ans)
{
	string z="0",o="1";
//	cout<<t->data<<endl;
	if(Le==t->Letter)
	{
		ans=re;
		return;
	}
	else if(t->Letter!=Le)
	{
		if(t->L!=NULL)
			Look(t->L,re+z,Le,ans);
		if(t->R!=NULL)
			Look(t->R,re+o,Le,ans); 
		return;
	}
	
}
int main()
{
	Node arr[5];
	string deco,ans[5],xx,Letter="A";
	HTree H;
	fstream f;
	f.open("p5.out",ios::out);
	H.Read(arr,deco);
	for(int i=0;i<5;i++)
		H.Create(arr,i);
	for(int i=0;i<5;i++)
	{
		H.Look(&arr[4],xx,Letter,ans[i]);
		f<<Letter<<" "<<ans[i]<<endl;
		Letter[0]++;
		cout<<ans[i]<<endl;
	}
	f<<'\n';
	for(int i=0;i<deco.size();i++)
		f<<ans[(int)(deco[i]-'A')];
	f.close();
	return 0;
 } 
