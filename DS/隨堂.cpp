#include<iostream>
using namespace std;

template <class T>
class ChainNode
{
private:
	T data;
	ChainNode<T> *link;
public:
	ChainNode(){}
	ChainNode(const T& data){this->data = data;}	
	ChainNode(const T& data, ChainNode<T>* link)
	{this->data = data;this->link = link;}
	ChainNode<T>* next(){return this->link;}
	void setdata(T d){this->data=d;}
	void setlink(ChainNode<T>* l){this->link=l;}
	T Gdata(){return this->data;}
};
template<class T>
class Chain
{
	public:
	Chain() {first = NULL;} // constructor, empty chain
	~Chain(){delete first;} // destructor
	bool IsEmpty() const {return first == NULL;}
	void Create(int);
	T Get(int);
	int Count(){int cc=1;ChainNode<T>*run=first;while(run->next()!=NULL){cc++;run=run->next();}return cc;}
	private:
	ChainNode<T>* first;
};

template<class T>
void Chain<T>::Create(int value)
{
	ChainNode<T>*x=new ChainNode<T>(value,NULL);
	if(IsEmpty())
	{
		first=x;
		return ;
	}
	else
	{
		ChainNode<T>* set=first;
		while(set->next()!=NULL)
			set=set->next();
		set->setlink(x);
		return ;
	}
}
template<class T>
T Chain<T>::Get(int pos)
{
	int sum=0;
	int counter = 0;
	ChainNode<T>* count=first;
	while(count->next()!=NULL)
	{count=count->next();sum++;}
	if(pos>sum)
	{
		cout<<"No data"<<endl;
		return -1;
	}
	ChainNode<T>* Run;
	Run=first;
	while(counter!=pos)
	{
		Run=Run->next();
		counter++;
	}  
	return Run->Gdata();
}
int main()
{
	Chain<int> Link;
	for(int i=1;i<=5;i++)
		Link.Create(i*10);
	for(int i=0;i<5;i++)
		cout<<"Get("<<i<<"):"<<Link.Get(i)<<endl;	
	return 0;
} 
