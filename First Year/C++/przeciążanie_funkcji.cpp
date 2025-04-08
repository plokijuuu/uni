#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void usundup(vector<int>& vec);
void printvec(const vector<int>& vec);
vector<int> suma(const vector<int>&a, const vector<int>&b);
vector<int> suma(const vector<int>&a, const vector<int>&b, const vector<int>&c);
vector<int> roz(const vector<int>&a, const vector<int>&b);
vector<int> roz(const vector<int>&a,const vector<int>&b, const vector<int>&c);
vector <int> wspol(const vector<int>&a, const vector<int>&b);
vector <int> wspol(const vector<int>&a, const vector<int>&b, const vector<int>&c);

int main()
{
    vector <int> v1;
    vector <int> v2;
    vector <int> v3;
    cout<<"Podaj liczbe elementow zbiorow: ";
    int n;
    cin>>n;
    cout<<"Podaj pierwszy zbior roznych liczb: ";
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        v1.push_back(x);
    }
    cout<<"Podaj drugi zbior roznych liczb: ";
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        v2.push_back(x);
    }
    cout<<"Podaj trzeci zbior roznych liczb: ";
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        v3.push_back(x);
    }
    usundup(v1);
    usundup(v2);
    usundup(v3);
    cout<<"Suma v1 i v2 = ";
    printvec(suma(v1,v2));
    cout<<"Suma v1, v2, v3 = ";
    printvec(suma(v1,v2,v3));
    cout<<"Roznica v1 i v2 = ";
    printvec(roz(v1,v2));
    cout<<"Roznica v3 i sumy v1 i v2 = ";
    printvec(roz(v1,v2, v3));
    cout<< "Czesc wspolna v1 i v2 = ";
    printvec(wspol(v1,v2));
    cout<<"Czesc wspolna v1, v2 i v3 = ";
    printvec(wspol(v1,v2, v3));
    return 0;
}
void usundup(vector<int>& vec)
{
    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
}
void printvec(const vector<int>& vec)
{
    cout << "{";
    for (int i = 0; i < vec.size(); ++i)
    {
        cout << vec[i];
        if (i != vec.size() - 1) cout << ", ";
    }
    cout << "}"<<endl;
}
vector<int> suma(const vector<int>&a, const vector<int>&b)
{
    vector<int> ans = a;
    for (int i = 0; i < b.size(); i++)
    {
        bool temp = 1;
        for (int j = 0; j < a.size(); j++)
        {
            if (b[i] == a[j])
            {
                temp = 0;
                break;
            }
        }
        if (temp == 1)
        {
            ans.push_back(b[i]);
        }
    }
    return ans;
}
vector<int> suma(const vector<int>&a, const vector<int>&b, const vector<int>&c)
{
    vector<int> ans = suma(a, b);
    for (int i = 0; i < c.size(); i++)
    {
        bool temp = 1;
        for (int j = 0; j < ans.size(); j++)
        {
            if (c[i] == ans[j])
            {
                temp = 0;
                break;
            }
        }
        if (temp == 1)
        {
            ans.push_back(c[i]);
        }
    }
    return ans;
}
vector<int> roz(const vector<int>&a, const vector<int>&b)
{
    vector<int> ans;
    for (int i = 0; i < a.size(); i++)
    {
        bool temp = 1;
        for (int j = 0; j < b.size(); j++)
        {
            if (a[i] == b[j])
            {
                temp = 0;
                break;
            }
        }
        if (temp == 1)
        {
            ans.push_back(a[i]);
        }
    }
    return ans;
}
vector<int> roz(const vector<int>&a,const vector<int>&b, const vector<int>&c)
{
    vector<int> ans;
    vector <int> sum = suma(a, b);
    for (int i = 0; i < c.size(); i++)
    {
        bool temp = 1;
        for (int j = 0; j < sum.size(); j++)
        {
            if (c[i] == sum[j])
            {
                temp = 0;
                break;
            }
        }
        if (temp == 1)
        {
            ans.push_back(c[i]);
        }
    }
    return ans;
}
vector <int> wspol(const vector<int>&a, const vector<int>&b)
{
    vector <int> ans;
    for (int i = 0; i < a.size(); i++)
    {
        for (int j = 0; j < b.size(); j++)
        {
            if (a[i] == b[j])
            {
                ans.push_back(a[i]);
                break;
            }
        }

    }
    return ans;
}
vector <int> wspol(const vector<int>&a, const vector<int>&b, const vector<int>&c)
{
    vector <int> ans;
    vector <int> ws = wspol(a, b);
    for (int i = 0; i < c.size(); i++)
    {
        for (int j = 0; j < ws.size(); j++)
        {
            if (c[i] == ws[j])
            {
                ans.push_back(c[i]);
                break;
            }
        }

    }
    return ans;
}
