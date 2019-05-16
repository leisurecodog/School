#include<iostream>
#include<fstream>
using namespace std;

template <class T>
class Stack
{ 
	int top;
	T *stack;
	int MaxSize;
public:
	Stack (int MaxStackSize);
	bool IsFull();
	bool IsEmpty();
	void Push(const T& item);
	void Pop();
	T Top(){return stack[top];}
};
template<class T>
Stack<T>::Stack(int MaxStackSize):MaxSize(MaxStackSize)
{
	stack=new T[MaxSize];
	top=-1;
}
template<class T>
inline bool Stack<T>::IsFull()
{
	if (top==MaxSize-1) return true;
	else return false;
}
template<class T>
inline bool Stack<T>::IsEmpty()
{
	if (top==-1) return true;
	else return false;
}
template <class T>
void Stack<T>::Push(const T& x)
{
	if (IsFull())
		cout<<"Full"<<endl;
	else
		stack[++top]=x;
}

template <class T>
void Stack<T>::Pop()
{
	if (IsEmpty())
	{
		cout<<"empty"<<endl;
	}
	else
		stack[top--] .~T(); 
}


struct Items {
int x, y, dir;
};
struct offsets {
int a;
int b;
};
void MoveSet(offsets* m)
{
	m[0].a=-1;m[0].b=0;
	m[1].a=-1;m[1].b=1;
	m[2].a=0;m[2].b=1;
	m[3].a=1;m[3].b=1;
	m[4].a=1;m[4].b=0;
	m[5].a=1;m[5].b=-1;
	m[6].a=0;m[6].b=-1;
	m[7].a=-1;m[7].b=-1;
}
void ReadRC(int& r, int& c)
{
	fstream f;
	int rt=0,ct=1;
	string x;
	f.open("p3.in",ios::in);
	while(!f.eof())
	{
		getline(f,x);
		rt++;
	}
	f.close();
	for(int i=0;i<x.size();i++)
		if(x[i]==' ')ct++;
	
	r=rt,c=ct;
}
void SetArr(int**maze , int** mark, int r ,int c)
{
	fstream f;
	char test;
	f.open("p3.in",ios::in);
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			f>>test;
			if(test=='s' || test=='d')
			maze[i][j]=0;
			else
			maze[i][j]=(int)(test-48);
		}
	}
	for(int i=0;i<r+2;i++)
	{
		for(int j=0;j<c+2;j++)
		{
			if(j==0 || i==0 || j==c+1 || i==r+1)
			mark[i][j]=1;
			else
			mark[i][j]=0;
		}
	}
}
enum directions {N, NE, E, SE, S, SW, W, NW};
int main()
{
	fstream f;
	f.open("p3.out",ios::out);
	int g,h;
	int count=-1;
	bool dst=0;
	int dir=N;
	offsets move[8];
	int Nposx,Nposy;
	int** maze;
	int** mark;
	bool **path;
	int row,col;
	Items start;
	Items used;
	Items find;
	start.x=0;start.y=0;start.dir=dir;
	MoveSet(move);
	ReadRC(row,col);
	Stack<Items> s(row*col);
	maze=new int*[row];
	for(int i=0;i<row;i++)
		maze[i]=new int[col];
	path=new bool*[row];
	for(int i=0;i<row;i++)
		path[i]=new bool[col];
	for(int i=0;i<row;i++)
		for(int j=0;j<col;j++)
			path[i][j]=0;
	mark=new int*[row+2];
	for(int i=0;i<row+2;i++)
		mark[i]=new int[col+2];
	SetArr(maze,mark,row,col);
	s.Push(start);
	while(!s.IsEmpty())//stack is not empty ,do it
	{
		used=s.Top();
		while(dir!=NW)
		{
			g=used.x+move[dir].a;
			h=used.y+move[dir].b;
		//	if(!(g>=0 && g<row && h>=0 && h<col)){used.dir++;dir++;s.Pop();s.Push(used);continue;} //void maze array error
			if(g==row-1 && h==col-1)dst=1; //successful
			if(!mark[g+1][h+1] && !maze[g][h])
			{
				mark[g+1][h+1]=1;
				dir=N;
				find.x=g;
				find.y=h;
				find.dir=dir;
				s.Push(find);
				used=s.Top();
			}
			else dir++;
		}
		if(dst)
		{
			while(!s.IsEmpty())
			{
				count++;
				used=s.Top();
				path[used.x][used.y]=1;
				s.Pop();
			}
			for(int i=0;i<row;i++)
				{
				for(int j=0;j<col;j++)
				{
					if(i==0 && j==0 )
					f<<"s ";
					else if(i==row-1 && j== col-1)
					f<<"d ";
					else if(path[i][j])
					f<<"* ";
					else
					f<<maze[i][j]<<" ";
				}
				f<<endl;
			}
			f<<count<<endl;
			break;
		}
		s.Pop();
	}
	if(!dst)
	f<<"Can't find."<<endl;
	f.close();
	return 0;
} 
