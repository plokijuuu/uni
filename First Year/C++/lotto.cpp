#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

bool czy_pierwsza(short int n);
void losowanie(short int * t);

int main()
{
	short int tab2[49];
	short int tab[6];
	
	for(short int i = 0; i < 49; i++)
	{
		tab2[i] = i + 1;
	}
	
	losowanie(tab2);
	
	for(short int i = 0; i < 6; i++)
	{
		tab[i] = tab2[i];
	}
	
	short int mini = 50;
	short int maxi = 0;
	short int poz_max = 50;
	short int poz_min = 50;
	
	cout<<"Wylosowany zbior liczb Lotto: ";
	for(short int i = 0; i < 6; i++)
	{
		cout<<tab[i]<<" ";
		if(tab[i] > maxi)
		{
			maxi = tab[i];
			poz_max = i;
		}
		if(tab[i] < mini)
		{
			mini = tab[i];
			poz_min = i;
		}
	}
	
	cout<<endl<<endl<<"Informacja na temat minimum w wylosowanym zbiorze:"<<endl;
	cout<<"1. Wartosc liczby: "<<mini<<endl;
	cout<<"2. Pozycja nr: "<<(poz_min + 1)<<endl;
	cout<<"3. Czy jest to liczba pierwsza? (0 - Nie, 1 - Tak): "<<czy_pierwsza(mini)<<endl;
	
	cout<<endl<<"Informacja na temat maksimum w wylosowanym zbiorze:"<<endl;
	cout<<"1. Wartosc liczby: "<<maxi<<endl;
	cout<<"2. Pozycja nr: "<<(poz_max + 1)<<endl;
	cout<<"3. Czy jest to liczba pierwsza? (0 - Nie, 1 - Tak): "<<czy_pierwsza(maxi)<<endl;
	
	return 0;
}
void losowanie(short int * t)
{
	srand(time(0));
	
	for(short int i = 48; i > 0; i--)
	{
		short int j = rand() % (i + 1);
		swap(t[i], t[j]);
	}
}
bool czy_pierwsza(short int n)
{
	if(n < 2) return false; 
		
	for(short int i = 2; (i * i) <= n ; i++)
	{
		if(n % i == 0) return false;
	}
	return true;
}

