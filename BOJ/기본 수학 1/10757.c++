#include <iostream>
#include <vector>

using namespace std;
int main()
{
    vector<int> ans;
    string a,b,temp;
    int i,num1[10001], num2[10001],sum;

    cin>>a>>b;
    
    if(a.size() < b.size())
    {
        temp = a;
        a = b;
        b = temp;
    }

    for(i=0;i<a.size();i++)
    {
        num1[i+1] = a[i] - '0';
    }
    for(i=0;i<b.size();i++)
    {
        num2[i+1+(a.size() - b.size())] = b[i] - '0';
    }

    for(i=a.size();i>0;i--)
    {
        sum = num1[i] + num2[i];
        if(sum>=10)
        {
            num1[i-1]++;
            sum-=10;
        }
        ans.push_back(sum);
    }

    if(num1[0]!=0) cout<<1;
    for(i=ans.size()-1;i>=0;i--)
    {
        cout<<ans[i];
    }
     
    return 0;
}