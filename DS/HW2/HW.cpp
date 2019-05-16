#include<iostream>
#include<fstream>
#include<string>
#include<time.h>
using namespace std;
class MatrixTerm {
	friend class SparseMatrix;
	friend class T;
	friend class FT;
	private:
	int row, col, value;
};

class SparseMatrix{
	public:
	SparseMatrix(){}
	SparseMatrix(int r, int c, int t);
	void ReadData(MatrixTerm *x);
	void setValue(int r,int c,int t);
	int getcol();
	int getrow();
	int getterm();
	MatrixTerm* getm();
	void Readm(MatrixTerm *ob);
	virtual SparseMatrix Transpose();//2D transpose
	private:
	int rows, cols, terms, capacity;
	MatrixTerm *smArray;
};
int SparseMatrix::getcol(){
	return cols;
}
int SparseMatrix::getrow(){
	return rows;
}
int SparseMatrix::getterm(){
	return terms;
}
void SparseMatrix::setValue(int r,int c,int t){
	rows=r;
	cols=c;
	terms=t;
	capacity=t;
}
MatrixTerm* SparseMatrix::getm(){
	return smArray;
}
void SparseMatrix::Readm(MatrixTerm *ob){
	smArray=ob;
}
SparseMatrix::SparseMatrix(int r,int c,int t)
{
	rows=r;
	cols=c;
	terms=t;
	capacity=t;
}
void SparseMatrix::ReadData(MatrixTerm *x)
{
		int useless;
		fstream f;
		f.open("p2.in",ios::in);
		f>>useless>>useless;
		for(int i=0;!f.eof();i++)
		{
			f>>x[i].row>>x[i].col>>x[i].value;
//			cout<<x[i].row<<" "<<x[i].col<<" "<<x[i].value<<endl;
		}
		f.close();
}
SparseMatrix SparseMatrix::Transpose(){
	double st,end;
	st=clock();
	int**use=new int*[rows];
	int cal=0;
	fstream f;
	f.open("p2.out",ios::out);
	MatrixTerm*ori;
	ori=new MatrixTerm[terms];
	ReadData(ori);
	for(int i=0;i<terms;i++)
		f<<"("<<ori[i].row<<","<<ori[i].col<<","<<ori[i].value<<")becomes("<<ori[i].col<<","<<ori[i].row<<","<<ori[i].value<<")in the transpose"<<endl;
	for(int i=0;i<rows;i++)
	use[i]=new int[cols];
	for(int i=0;i<rows;i++)
		for(int j=0;j<cols;j++)
			use[i][j]=0;
	
	for(int i=0;i<rows;i++)
		for(int j=0;j<cols;j++)
		if(ori[cal].row==i && ori[cal].col==j){
			use[j][i]=ori[cal].value;
			cal++;
		}
	end=clock();
	f<<(end-st)/(double)1000<<endl;
	f.close();
	return *this;
} 
class T : public SparseMatrix{
	public:
		T(int r,int c,int t);
	SparseMatrix Transpose();
};
T::T(int r,int c,int t){
	setValue(r,c,t);
}
SparseMatrix T::Transpose(){
	double st,end;
	st=clock();
		int useless;
		int col=getcol(),row=getrow(),term=getterm();
		MatrixTerm*ori;
		MatrixTerm*cur;
		SparseMatrix b(col, row, term); // capacity of b.smArray is terms
		if (term > 0)
		{// nonzero matrix
		cur=new MatrixTerm[term];
		ori=new MatrixTerm[term]; 
		ReadData(ori);
		int currentB = 0;
		for (int c=0; c<col; c++) // transpose by columns
		for (int i = 0; i < term; i++) // find and move terms in column c
		if (ori[i].col == c) {
		cur[currentB].row=c;
		cur[currentB].col=ori[i].row;
		cur[currentB++].value = ori[i].value;
		}
		} // end of if (terms > 0)
		end=clock();
		fstream f;
		f.open("p2.out",ios::app);
		f<<(end-st)/(double)1000<<endl;
		f.close();
		b.Readm(cur);
		return b;
}
class FT : public SparseMatrix{
	public:
		FT(int r,int c,int t);
	SparseMatrix Transpose();
};
FT::FT(int r,int c,int t){
	setValue(r,c,t);
}
SparseMatrix FT::Transpose(){
	double st,end;
	st=clock();
		int useless;
		int col=getcol(),row=getrow(),term=getterm();
		MatrixTerm*ori;
		MatrixTerm*cur;
		SparseMatrix b(col, row, term); // capacity of b.smArray is terms
		if (term > 0)
		{// nonzero matrix
		int* rowSize=new int[col];
		for(int i=0;i<col;i++)
		rowSize[i]=0;
		int* rowStart=new int[col];
		for(int i=0;i<col;i++)
		rowStart[i]=0;
		
		cur=new MatrixTerm[term];
		ori=new MatrixTerm[term]; 
		
		ReadData(ori);
		
		for (int i = 0 ; i < term ; i ++) rowSize[ori[i].col]++;
		rowStart[0] = 0;
		for (int i = 1 ; i < col ; i++) rowStart[i] = rowStart[i-1] + rowSize[i-1];
		for (int i = 0 ; i < term ; i++)
			{// copy from *this to b
			int j = rowStart[ori[i].col];
			cur[j].row= ori[i].col;
			cur[j].col = ori[i].row;
			cur[j].value = ori[i].value;
			rowStart[ori[i].col]++;
			} // end of for
			
		} // end of if (terms > 0)
		
		end=clock();
		fstream f;
		f.open("p2.out",ios::app);
		f<<(end-st)/(double)1000<<endl;
		f.close();
		
		b.Readm(cur);
		return b;
}
int main()
{
	int a,b,count=0;
	string x;
	fstream file,f;
	file.open("p2.in",ios::in);
	if(!file)cout<<"File Open Error."<<endl;
	file>>a>>b;
	while(!file.eof())
	{
		getline(file,x);
		count++;
	}
	file.close();
	count--;
	SparseMatrix m(a,b,count);
	m.Transpose();
	T tt(a,b,count);
	tt.Transpose();
	FT ft(a,b,count);
	ft.Transpose();
	f.open("p2.out",ios::in);
	while(!f.eof())
	{
		getline(f,x);
		cout<<x<<endl;
	}
	f.close();
	return 0;
}
