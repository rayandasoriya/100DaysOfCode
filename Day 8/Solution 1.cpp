#include <bits/stdc++.h>

using namespace std;

// Complete the countTriplets function below.
typedef long long ll;

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    long n,r;
    cin >> n >> r;
    
    map<int,long> mp2, mp3;
    //mp2 to hold count of needed values after this one to complete
    //2nd part of triplet
    //mp3 to hold count of needed values to complete triplet
    
    int val;
    long long res = 0;
    while(n--)
    {
        cin >> val;
        if (mp3.count(val))        //This value completes mp3[val] triplets
            res += mp3[val];
        if (mp2.count(val))        //This value is valid as 2° part of mp2[val] triplets
            mp3[val*r] += mp2[val];
        mp2[val*r]++;            //"Push-up" this value as possible triplet start
    }
    
    cout << res << endl;

return 0;
}
