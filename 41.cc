#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isPrime(int x) {
  for(int k = 2; k * k <= x; ++k) {
    if(x % k == 0) {
      return false;
    }
  }
  return true;
}

bool check(const vector<int>& v) {
  int num = 0;
  for(int i = 0; i < v.size(); ++i) {
    num = num * 10 + v[i];
  }
  return isPrime(num);
}

int main() {
  for(int n = 9; n >= 1; --n) {
    vector<int> v;
    for(int i = 1; i <= n; ++i) {
      v.push_back(i);
    }
    do {
        if(check(v)) {
          for(int i = 0; i < n; ++i) {
            cout << v[i];
          }
          cout << endl;
          return 0;
      }
    }while(next_permutation(v.begin(), v.end()));
  }
  return 0;
}
