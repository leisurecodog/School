#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
struct point
{
	int x;
	int y;
};
bool cmpx(point x,point y)
{
	if(x.x==y.x)return x.y<y.y;
	return x.x<y.x;
}
bool cmpy(point a,point b)
{
	if(a.y==b.y)return a.x<b.x;
	return a.y<b.y;
}
vector<point>vpx,vpy;
double Brute(int f,int l)
{
	double mi=1e9;
	for(int i=f;i<l-1;i++)
	{
		for(int j=i+1;j<l;j++)
		{
			double pa=sqrt((vpx[i].x-vpx[j].x)*(vpx[i].x-vpx[j].x)+(vpx[i].y-vpx[j].y)*(vpx[i].y-vpx[j].y));
			mi=min(mi,pa);
		}
	}
	return mi;
}

double DC(int f,int l)
{
	if(l-f<=3)return Brute(f,l);
	int mid=(f+l)/2;
	double dl=DC(f,mid);
	double dr=DC(mid,l);
	double mind=min(dl,dr);
	double tmp=mind;
	double midLine=vpx[mid].x;
	vector<point>vl,vr;
	for(int i=f;i<mid;i++)if(vpx[i].x>=midLine-mind)vl.push_back(vpx[i]);
	for(int i=mid;i<l;i++)if(vpx[i].x<=midLine+mind)vr.push_back(vpx[i]);
	
	for(int i=0;i<vl.size();i++)
	{
		double take=vl[i].y;
		for(int j=0;j<vr.size();j++)
		{
			if(abs(take-(double)vr[j].y)<=tmp)
			{
				double re=sqrt((vl[i].x-vr[j].x)*(vl[i].x-vr[j].x)+(vl[i].y-vr[j].y)*(vl[i].y-vr[j].y));
				mind=min(re,mind);
			}
		}
	}
	return mind;
}
int main()
{
	int n;
	
	cin>>n;
	vpy.clear();
	point tmp;
	for(int i=0;i<n;i++)
	{
		cin>>tmp.x>>tmp.y;
		vpy.push_back(tmp);
	}
	vpx=vpy;
	sort(vpy.begin(),vpy.end(),cmpy);
	sort(vpx.begin(),vpx.end(),cmpx);
	cout<<DC(0,n)<<endl;
	return 0;
}
