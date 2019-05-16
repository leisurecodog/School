#include<iostream>
using namespace std;

class node
{
	friend class chain; 
	private:
		int data;
		class node*next;
};
class chain
{
	public:
		chain(){first=NULL;}
		void Create();
		void Insert(int element,int order);
		void Delete(int order);
		void Print();
	private:
		node*first;
};
void chain:: Create()
{
	node*x=new node;
	node*c=first;
	x->data=0;
	x->next=NULL;
	if(first==NULL)
	first=x;
	else
	{
		while(c->next!=NULL)
		c=c->next;
		c->next=x;
	}
}
void chain::Insert(int element,int order)
{
	int count=0;
	node* c=first;
	while(c->next!=NULL)
	{c=c->next;count++;}
	if(order>count || order<0)
	{
		cout<<"Wrong order!"<<endl;
		return;
	}
	else
	{
		c=first;
		count=0;
		while(count!=order){c=c->next;count++;}
		c->data=element;
	}
}
void chain::Delete(int order)
{
	node*c=first;
	node*d;
	int count=0;
	while(c->next!=NULL)
	{c=c->next;count++;}
	if(order>count || order<0)
		cout<<"Wrong order!"<<endl;
	
	else if(order==0){d=first;first=first->next;}
	else
	{
		count=0;
		c=first;
		while(count!=order-1){c=c->next;count++;}
		d=c->next;
		c->next=d->next;
	}
	delete d;
} 
void chain::Print()
{
	node*c=first;
	while(c!=NULL)
	{
		cout<<c->data<<" ";
		c=c->next;
	}
	cout<<endl;
}
int main ()
{
	node *first=NULL;
	chain l;
	for(int i=0;i<6;i++)
		l.Create();
	l.Insert(5,0);
	l.Insert(7,1);
	l.Insert(11,2);
	l.Insert(64,3);
	l.Insert(666,4);
	l.Insert(888,5);
	l.Delete(2);
	l.Print();
	return 0;
 } 
