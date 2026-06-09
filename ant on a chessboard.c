#include <stdio.h>
#include <math.h>

int main() {
    long long N;

    while (scanf("%lld", &N) == 1 && N != 0) {
        long long k = ceil(sqrt((double)N));
        long long m = k * k - k + 1;
        long long x, y;

        if (k % 2 == 0) {  // even layer
            if (N >= m) {
                x = k;
                y = k * k - N + 1;
            } else {
                x = N - (k - 1) * (k - 1);
                y = k;
            }
        } else {           // odd layer
            if (N >= m) {
                x = k * k - N + 1;
                y = k;
            } else {
                x = k;
                y = N - (k - 1) * (k - 1);
            }
        }

        // EXACT format: x space y
        printf("%lld %lld\n", x, y);
    }

    return 0;
}
