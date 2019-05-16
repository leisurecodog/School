#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	fstream f;
	fstream s;
	int num;
	string read;
	f.open("Question_2.txt",ios::in); //use Question_2.txt for example
	s.open("decode.txt",ios::out);
	f>>num;
	s<<num;
	num=num%26;
	while(f.eof()!=1)
	{
		getline(f,read);
		if(read=="")
		s<<endl;
		else
		{
			int i=0;
			while(1)
			{
				if(i==read.length())
				break;
				if(read[i]==' ')
					s<<" ";
			else
			{
				if(read[i]-num<'A')
					s<<char(read[i]-num+26);
				else
					s<<char(read[i]-num);
			}
			i++;
			}
			s<<endl;
		}
	}
	return 0;
 } 
