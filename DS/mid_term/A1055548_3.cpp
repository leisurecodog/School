#include<iostream>
#include<fstream>
#include<string>
using namespace std;
class node
{
	friend class stack;
	private:
		int data;
		class node*next;
};
class stack
{
	public:
		void INS(int&reg);
		void DES(int&reg);
		void Print(int a,int b,int c,int d);
	private:
		node* first=NULL;
		node* top=NULL;
};
void stack::INS(int&reg)
{
	node*c=first;
	if(first==NULL)
	{
		node*x=new node;
		x->data=reg;
		x->next=NULL;
		first=x;
		top=x;
	}
	else if(first!=top)
	{
		while(c!=top)
			c=c->next;
			
		node*x=new node;
		c->next=x;
		x->data=reg;
		x->next=NULL; 
		top=x;
	}
	else
	{
		c=first;
		node*x=new node;
		x->data=reg;
		x->next=NULL;
		c->next=x;
		top=x;
	}
		
}
void stack::DES(int&reg)
{
	node*d=top;
	if(first==top)
	{
		
		reg=top->data;
		first=NULL;
		top=NULL;
		delete d;
		
	}
	else
	{
		d=top;
		node*c=first;
		while(c->next!=top)
			c=c->next;
		top=c;
		reg=d->data;
		top->next=NULL;
		delete d;
	}
}
void stack::Print(int a,int b,int c,int d)
{
	node*cc=first;
	cout<<"Stack:";
	while(cc!=NULL)
	{
		cout<<cc->data<<" ";
		cc=cc->next;
	}
	cout<<endl;
	
	cout<<"A="<<a<<"\nB="<<b<<"\nC="<<c<<"\nD="<<d<<endl;
}
int main()
{	
	fstream f;
	int i=0;
	int num;
	stack s;
	int A=(65+97)%26,B=(66+98)%26,C=(67+99)%26,D=(68+100)%26;
	string read;
	f.open("Question_3.txt",ios::in);
	f>>num;
	getline(f,read);
	while(f.eof()!=1)
	{
		getline(f,read);
			i=0;
			if(read!="")
			while(i!=read.length()-1)
			{
				if(read[i]=='I')
					{
						i+=4;
						if(read[i]=='A')
							s.INS(A);
						else if(read[i]=='B')
							s.INS(B);
						else if(read[i]=='C')
							s.INS(C);
						else if(read[i]=='D')
							s.INS(D);
					}
				else if (read[i]=='D')
					{
						i+=4;
						if(read[i]=='A')
							s.DES(A);
						else if(read[i]=='B')
							s.DES(B);
						else if(read[i]=='C')
							s.DES(C);
						else if(read[i]=='D')
							s.DES(D);
					} 
				if(i!=read.length()-1)
					i+=2;
					
			}
			if(read!="")
			s.Print(A,B,C,D);
	}
	return 0;
 } 
