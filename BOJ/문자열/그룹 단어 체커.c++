#include <iostream>

using namespace std;
int main()
{
    int n,cnt=0;
    string word;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>word;
        bool qoduf[26] = {false,};
        qoduf[(int)(word[0])-97] = true;

        for(int j=1;j<word.size();j++)
        {
            if(word[j] == word[j-1]) continue;
            else if(word[j] != word[j-1] && qoduf[(int)(word[j])-97] == true)
            {
                cnt++;
                break;
            }
            else qoduf[(int)(word[j])-97] = true;
        }
    }
    cout<<n-cnt;
    return 0;
}