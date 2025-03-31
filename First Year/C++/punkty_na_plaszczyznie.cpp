#include <iostream>
#include <cmath>

using namespace std;
struct punkt
{
	double x;
	double y;
};
int main()
{
	int n;
	cout<<"Podaj ilosc punktow: ";
	cin>>n;
	
	punkt* punkty = new punkt[n + 1];
	
	for(int i = 1; i <= n; i++)
	{
		cout<<"Podaj wspolrzedne punktu "<< i <<" w kolejnosc x, y: ";
		cin>>punkty[i].x>>punkty[i].y;
	}
	
	cout<<"Informacje dotyczace utworzonych punktow:"<<endl;
	cout<<"Lista utworzonych punktow: ";
	for(int i = 1; i <= n; i++)
	{
		cout<<"P"<<i<<" ("<<punkty[i].x<<", "<<punkty[i].y<<") ";
	}
	
	cout<<endl<<"Srednia odleglosc od punktu (0, 0): ";
	double maxi = 0;
	double suma = 0;
	for(int i = 1; i <= n; i++)
	{	
		double temp = sqrt(punkty[i].x * punkty[i].x + punkty[i].y * punkty[i].y);
		suma += temp;
		if(temp > maxi) maxi = temp;
	}
	cout<< suma / n <<endl;
	cout<<"Promien kola o wsp. srodka (0, 0) zawierajacego wszystkie punkty: "<<maxi;
	
	delete[] punkty;
	
	return 0;
}
