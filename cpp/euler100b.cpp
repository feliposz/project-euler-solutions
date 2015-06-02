#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <cmath>

using namespace std;

long long gcd(long long a, long long b)
{
    long long tmp;
    while (b != 0) {
        tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}

int main()
{
    time_t start = time(NULL);

    long long total, blue, red;
    long long num, den, div1, div2;
    //double sqrt2 = sqrt(2.0);
    long double sqrt2 = 1.4142135623730950488L;

    cout << setprecision(20) << sqrt2 << endl;

    blue = 15;
    //total = 1000000000000LL;

    while (true) {
        //blue = (long long)(total / sqrt2) + 1;
        total = (long long)(blue * sqrt2);
        red = total - blue;

        if ((div1 = gcd(blue, total)) > 1 && (div2 = gcd(blue-1, total-1)) > 1) {
            num = (blue / div1) * ((blue - 1) / div2);
            den = (total / div1) * ((total - 1) / div2);

            if (num <= 0 || den <= 0) {
                cerr << "Overflow!" << endl;
                exit(1);
            }

            if (num * 2 == den) {
                cout << "Blues: " << blue << " Reds: " << red;
                cout << " Total: " << total << " Time: " << (time(NULL) - start);
                cout << endl;
                if (total >= 1000000000000LL)
                    break;
            }
        }

        blue = (long long)(blue * 5.82842 - 2;
    }
    return 0;
}


/*

Values ok:
Blues: 15 Reds: 6 Total: 21 Time: 0
Blues: 85 Reds: 35 Total: 120 Time: 0
Blues: 493 Reds: 204 Total: 697 Time: 0
Blues: 2871 Reds: 1189 Total: 4060 Time: 0
Blues: 16731 Reds: 6930 Total: 23661 Time: 0
Blues: 97513 Reds: 40391 Total: 137904 Time: 0
Blues: 568345 Reds: 235416 Total: 803761 Time: 0
Blues: 3312555 Reds: 1372105 Total: 4684660 Time: 1
Blues: 19306983 Reds: 7997214 Total: 27304197 Time: 1
Blues: 112529341 Reds: 46611179 Total: 159140520 Time: 6
Blues: 655869061 Reds: 271669860 Total: 927538921 Time: 35
Blues: 3822685023 Reds: 1583407981 Total: 5406093004 Time: 194

These values might be wrong:

This is definitly not the right answer!
Blues: 707119501233 Reds: 292898487629 Total: 1000017988862 Time: 2
*/
