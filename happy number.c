#include <iostream>
using namespace std;

int nextNum(int n) {
    int sum = 0;
    while (n > 0) {
        int d = n % 10;
        sum += d * d;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow = n;
    int fast = n;

    do {
        slow = nextNum(slow);
        fast = nextNum(nextNum(fast));
    } while (slow != fast);

    return slow == 1;
}

int main() {
    int n;
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++){
        cin >> n;
        if (isHappy(n))
            cout << "Case #" << i << ": " << n << " is a Happy number." << endl;
        else
            cout << "Case #" << i << ": " << n << " is an Unhappy number." << endl;
    }
}
