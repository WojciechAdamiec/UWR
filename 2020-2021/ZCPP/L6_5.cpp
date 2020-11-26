#include <iostream>

using namespace std;


void permute(string str)
{
    sort(str.begin(), str.end());
    while (next_permutation(str.begin(), str.end())){
        cout << str << "\n";
    }
}

int main()
{
	permute("WOJTEK");
	return 0;
}
