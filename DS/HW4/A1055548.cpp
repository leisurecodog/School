#include<iostream>
#include<time.h> 
using namespace std;
class node
{
	friend class chain;
	private:
		int num;
		class node* next;
};
class chain
{
	public:
		void FindN(int,int&);
};
void chain::FindN(int k,int&n)
{
	int count=k+1;
	int test;
	int Nnode;
	node* run;
	bool find=0;
	bool ftime=0;
	bool notn=0;
	while(!find)
	{
		notn=0;
		node* con=new node;
		con->num=1;
		run=con;
		for(int i=1;i<=2*k-1;i++)//create a 2*k nodes using ratate linked list
		{
			node* kkk=new node;
			kkk->num=i+1;
			run->next=kkk;
			run=kkk;
		}
		Nnode=2*k;
		run->next=con;
		run=con; 
		for(int i=0;i<k && !notn;i++)//kill all bad man
		{
			int re=(count-2)%Nnode;
			for(int j=0;j<re;j++)//stop at before that we want to delete
				run=run->next;
				
			if(run->next->num<=k)//good man be killed
				notn=1;
			else
			{
				run->next=run->next->next;
				run=run->next;
				Nnode--;
			}
		}
		if(!notn)
			find=1;
		else
		count++;
		
	}
	n=count;
}
int main()
{
	chain aa;
	int k,n;
	cin>>k;
	double a=clock();
		aa.FindN(k,n);
		cout<<"N="<<n<<endl;
	double b=clock()-a;
	cout<<"times="<<b/1000<<endl;
	return 0;
 } 
