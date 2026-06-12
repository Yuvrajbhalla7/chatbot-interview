#include<iostream>
using namespace std;
int main(){
int n;
cin >> n;
int dup=n;
int rev =0;
while(n>0)
{
    int dig = n%10;
    rev = (rev*10) + dig;
    n=n/10;

}
if(rev==dup) cout<<"true";
else cout<<"false";
// 1331cout<<rev;
 }